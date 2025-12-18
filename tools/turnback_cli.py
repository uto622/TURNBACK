#!/usr/bin/env python3
# TURNBACK v0.1 - minimal CLI
# transcript -> turnback report JSON + optional GitHub issue markdown

import argparse
import json
import re
import uuid
from datetime import datetime, timezone

ISSUE_TYPES = ("SPEAKER_FOCUS", "INTERRUPTION_TIMING")

def _now_iso():
    return datetime.now(timezone.utc).isoformat()

def redact_basic(text: str) -> str:
    """Basic optional redaction (very conservative)."""
    # email
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '<REDACTED_EMAIL>', text)
    # phone-like (very rough)
    text = re.sub(r'(\+?\d[\d\-\s]{7,}\d)', '<REDACTED_PHONE>', text)
    return text

def detect_signals(transcript: str) -> dict:
    """
    Rule-level signals (text-only baseline).
    We assume transcripts may include markers like:
      [noise], [overlap], (background), Speaker A/B, etc.
    """
    t = transcript.lower()

    overlap = any(k in t for k in ["[overlap]", "(overlap)", "overlapping", "同时说话"])
    background = any(k in t for k in ["background", "旁人", "背景", "[noise]", "(noise)", "环境音"])
    speaker_markers = len(re.findall(r'\b(speaker\s*[ab]|\bspk\s*\d+|说话人\s*\d+)\b', t))
    interruption_markers = any(k in t for k in ["interrupt", "打断", "插话", "you cut me off", "stop talking"])
    thinking_pause_markers = any(k in t for k in ["...", "呃", "嗯", "let me think", "我想一下", "停顿"])

    return {
        "overlap_detected": overlap,
        "background_speech_or_noise": background,
        "speaker_marker_count": speaker_markers,
        "interruption_markers": interruption_markers,
        "thinking_pause_markers": thinking_pause_markers,
    }

def classify_issue(signals: dict) -> str:
    """
    Minimal heuristic classifier.
    - Speaker focus: background/overlap + speaker markers
    - Interruption: explicit interruption markers or thinking pause markers
    """
    speaker_score = 0
    interrupt_score = 0

    if signals["background_speech_or_noise"]:
        speaker_score += 2
    if signals["overlap_detected"]:
        speaker_score += 2
    if signals["speaker_marker_count"] >= 2:
        speaker_score += 1

    if signals["interruption_markers"]:
        interrupt_score += 3
    if signals["thinking_pause_markers"]:
        interrupt_score += 1

    return "SPEAKER_FOCUS" if speaker_score >= interrupt_score else "INTERRUPTION_TIMING"

def build_report(transcript: str, strict_redaction: bool, issue_type: str | None) -> dict:
    raw = transcript
    sanitized = redact_basic(raw) if strict_redaction else raw

    signals = detect_signals(sanitized)
    inferred_type = classify_issue(signals)
    chosen_type = issue_type if issue_type in ISSUE_TYPES else inferred_type

    report = {
        "report_id": str(uuid.uuid4()),
        "timestamp_utc": _now_iso(),
        "issue": {
            "type": chosen_type,
            "severity": 2,
            "expected_behavior": "",
            "actual_behavior": "",
            "reproduction_steps": [],
        },
        "evidence": {
            "sanitized_transcript": sanitized.strip(),
            "signals": signals,
        },
        "privacy": {
            "redaction_enabled": strict_redaction,
        },
        "labels": [
            "turnback",
            "conversation-failure",
            "voice"  # can be edited by reporter
        ],
    }
    return report

def to_github_issue_markdown(report: dict) -> str:
    issue_type = report["issue"]["type"]
    signals = report["evidence"]["signals"]

    md = []
    md.append(f"## 1. Issue Type\n- **{issue_type}**\n")
    md.append("## 2. Expected Behavior\n(Describe what should happen)\n")
    md.append("## 3. Actual Behavior\n(Describe what actually happened)\n")
    md.append("## 4. Reproduction Steps\n1.\n2.\n3.\n")
    md.append("## 5. Conversation Evidence (Sanitized)\n```text\n")
    md.append(report["evidence"]["sanitized_transcript"][:4000])  # guard length
    md.append("\n```\n")
    md.append("## 6. Observed Signals\n")
    for k, v in signals.items():
        md.append(f"- `{k}`: `{v}`")
    md.append("\n## 7. Severity\n- [ ] 1  - [x] 2  - [ ] 3  - [ ] 4\n")
    md.append("## 8. Consent & Responsibility\nSubmitted content is sanitized or submitted at the reporter’s responsibility.\n")
    return "\n".join(md)

def main():
    p = argparse.ArgumentParser(description="TURNBACK v0.1 - transcript to feedback report")
    p.add_argument("input", help="Path to transcript .txt")
    p.add_argument("--out", default="turnback_report.json", help="Output JSON file")
    p.add_argument("--issue-md", default="", help="Optional output GitHub issue markdown file")
    p.add_argument("--type", default="", help="Force issue type: SPEAKER_FOCUS or INTERRUPTION_TIMING")
    p.add_argument("--redact", action="store_true", help="Enable basic redaction (email/phone)")
    args = p.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        transcript = f.read()

    report = build_report(transcript, strict_redaction=args.redact, issue_type=args.type)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    if args.issue_md:
        md = to_github_issue_markdown(report)
        with open(args.issue_md, "w", encoding="utf-8") as f:
            f.write(md)

    print(f"[OK] wrote: {args.out}")
    if args.issue_md:
        print(f"[OK] wrote: {args.issue_md}")

if __name__ == "__main__":
    main()

Sample usage（可运行示例）

python tools/turnback_cli.py examples/transcript.txt --redact --out report.json --issue-md issue.md


Sample output（JSON 片段）

{
  "report_id": "c9c5e5e7-6b50-4e5d-8f39-8c2f0c0b2f1d",
  "issue": { "type": "SPEAKER_FOCUS", "severity": 2, "expected_behavior": "", "actual_behavior": "", "reproduction_steps": [] },
  "evidence": {
    "signals": {
      "overlap_detected": true,
      "background_speech_or_noise": true,
      "speaker_marker_count": 2,
      "interruption_markers": false,
      "thinking_pause_markers": true
    }
  }
}
