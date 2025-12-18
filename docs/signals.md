# TURNBACK Signal Detection Reference

This document provides **rule-level reference heuristics**
for detecting Speaker Focus Failure and Interruption Timing Failure.

These are not production requirements.
They are interpretable baselines for contributors and integrators.

---

## 1. Speaker Focus Signals

### Goal

Determine whether the system should maintain focus
on the current primary speaker despite background speech.

---

### Core Heuristics (Non-Identity-Based)

The following signals may be combined:

#### 1. Temporal Continuity
- Short pauses (< 1.5s) following user speech
- No explicit turn-ending markers

#### 2. Prosodic Similarity (Lightweight)
- Comparable speaking rate
- Similar pause distribution
- Stable volume range

> No voiceprint or biometric identification is required.

---

#### 3. Linguistic Continuity
- Sentence continuation markers
- Unfinished clauses
- Discourse particles indicating continuation

Examples:
- “所以……”
- “然后我想说……”
- “but the thing is…”

---

#### 4. Context Binding
- Ongoing Q/A pair not yet resolved
- System prompt expects continuation
- No explicit topic reset

---

### Failure Signal

A Speaker Focus Failure is flagged when:

- Background speech appears
- AND continuity signals are present
- AND the system resets or switches focus

---

## 2. Interruption Timing Signals

### Silence Classification

TURNBACK distinguishes:

#### Thinking Pause
- Silence < 2.0s
- Preceded by unfinished syntax or filler
- Followed by continuation

#### Turn End
- Falling intonation
- Explicit completion phrases
- Clear syntactic closure

#### Noise Gap
- Irregular waveform
- Environmental sound markers
- No linguistic structure

---

### Interruption Failure Conditions

An interruption failure may be flagged when:

- System responds during a Thinking Pause
- System stops output when human resumes
- System speaks before Turn End signals are present

---

## 3. Non-Goals

TURNBACK does not require:

- Perfect detection accuracy
- Low-latency optimization
- Model-specific tuning
- Access to proprietary audio features

Interpretability and portability are prioritized.

---

## 4. Implementation Notes

- Rule-based approaches are sufficient for MVP
- Statistical or ML approaches may be layered later
- Client-side detection is preferred when possible
- All signals should be explainable in issue reports

---

End of signal reference.
