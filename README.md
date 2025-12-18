#  `README.md`

````md
# TURNBACK

**Conversation Feedback Infrastructure for Human–AI Interaction**

TURNBACK is an open-source infrastructure for reporting and structuring real-world
human–AI conversation failures—specifically failures in speaker focus and interruption timing.

This project does **not** build chatbots, agents, or models.
It exists to close the missing feedback loop between users and developers.

---

## What Problem Does TURNBACK Solve?

Modern voice and conversational AI systems fail in predictable but underreported ways:

- Losing focus on the primary speaker in noisy or multi-speaker environments
- Interrupting users during thinking pauses
- Resetting conversations due to background speech
- Breaking natural turn-taking rhythm

These failures are rarely captured by existing customer support or telemetry systems.
TURNBACK turns these failures into **reproducible, developer-actionable issues**.

---

## What TURNBACK Is (and Is Not)

### ✅ TURNBACK IS
- A **feedback infrastructure**
- A **standardized issue taxonomy**
- A **GitHub Issue–first reporting pipeline**
- A tool to convert lived interaction failures into engineering evidence

### ❌ TURNBACK IS NOT
- A chatbot or agent
- A model training framework
- A data collection or analytics platform
- A replacement for customer support
- An alignment, safety, or compliance solution

---

## Core Focus (MVP Scope)

TURNBACK v0.1 focuses on **two fundamental failure classes**:

1. **Speaker Focus Failure**  
   The system fails to maintain focus on the primary speaker when multiple voices or background noise are present.

2. **Interruption Timing Failure**  
   The system interrupts or halts responses at unnatural moments, especially during human thinking pauses.

Refusal logic, content moderation, and privacy compliance are **explicitly out of scope** for the MVP.

---

## How TURNBACK Works (Minimal Flow)

1. A user experiences a conversation failure
2. The failure is reported using a standardized GitHub Issue template
3. The report includes:
   - Expected vs actual behavior
   - Minimal reproduction steps
   - Sanitized conversation evidence
4. Developers receive structured, actionable feedback
5. Fixes can be verified against real interaction scenarios

---

## Repository Structure

```text
TURNBACK/
├── README.md                  # Project homepage
├── docs/
│   └── taxonomy.md            # Issue taxonomy and definitions
└── .github/
    └── ISSUE_TEMPLATE/
        └── turnback_issue.md  # GitHub Issue template
````

---

## Privacy & Responsibility

TURNBACK provides tooling, schemas, and conventions—not data governance.

* Conversation evidence should be sanitized by the submitter
* Optional redaction tools may be used by deployers
* Legal and compliance responsibility lies with contributors and integrators
* TURNBACK does not store or aggregate private conversations

---

## License

TURNBACK is licensed under the **Apache License 2.0**.

This allows broad adoption (including commercial use) while protecting contributors
through explicit attribution and patent provisions.

See `LICENSE` for details.

---

## Status

* [x] Core Issue Taxonomy
* [x] GitHub Issue Template
* [ ] Report generation tooling
* [ ] Community examples
* [ ] Signal detection reference implementations

