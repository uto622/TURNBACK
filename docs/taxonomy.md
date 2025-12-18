# ② `taxonomy.md`

```md
# TURNBACK Issue Taxonomy

This document defines the canonical issue taxonomy for TURNBACK.
It specifies what qualifies as a reportable conversation failure.

---

## Design Principles

- Prioritize **interaction dignity** over content intelligence
- Treat conversation rhythm as a first-class system property
- Avoid anthropomorphism
- Avoid identity inference
- Avoid compliance theater

---

## Issue Type 1: Speaker Focus Failure

### Definition

A failure where the system does not maintain focus on the primary speaker
in environments with background noise or multiple speakers.

The system incorrectly resets context, switches conversational focus,
or misattributes input due to ambient speech.

---

### Common Symptoms

- Conversation resets when someone nearby speaks
- Background speech is interpreted as new user input
- System responds to the wrong speaker
- Topic or task context is lost unexpectedly

---

### Detection Criteria

At least one of the following must be true:

- Semantic context is not closed, yet the system resets
- Speaker continuity exists, but focus is lost
- Ambient speech triggers a turn switch

---

### Explicit Non-Goals

TURNBACK does not:
- Identify personal identities
- Perform voiceprint matching
- Store or infer speaker identity

Only continuity of interaction is evaluated.

---

## Issue Type 2: Interruption Timing Failure

### Definition

A failure where the system interrupts, responds, or halts
at inappropriate times, disrupting natural conversational flow.

---

### Silence Classification

TURNBACK distinguishes three types of silence:

| Type | Description |
|---|---|
| Thinking Pause | Cognitive pause during speech |
| Turn End | Clear completion of an utterance |
| Noise Gap | Environmental or signal interruption |

---

### Failure Conditions

- System responds during a thinking pause
- System stops responding when user resumes speaking
- System speaks before a turn is clearly completed

---

### Explicit Non-Goals

TURNBACK does not optimize for:
- Response speed
- Low latency
- Content quality

The only goal is **proper timing**.

---

## Minimal Issue Report Requirements

Every issue must include:

- Issue type
- Expected behavior
- Actual behavior
- Minimal reproduction steps
- Sanitized evidence
- Optional signal indicators

---

## Scope Boundary

TURNBACK does not define:
- Content moderation rules
- Refusal policies
- Political or legal constraints
- Model alignment strategies

These concerns belong to downstream systems.

---

## Rationale

These failure classes are:

- Universally observable
- Non-political
- Non-ideological
- Independent of model architecture
- Determinative of user trust

They are foundational and precede all higher-level intelligence.

---

End of taxonomy.
