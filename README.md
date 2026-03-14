# The Twelve Demons of Drift

**A Formal Taxonomy of AI Reasoning Failure Modes**

Author: Kevin Gilbert
Version: 1.0 — 2026

> "Systems collapse when constraints fail." — Kevin Gilbert

---

## What This Is

The Twelve Demons of Drift is a structured taxonomy of failure modes that cause AI systems to lose alignment, coherence, and operational integrity.

Each Demon represents a distinct class of destabilization.
Each maps to a parallel failure mode in human systems — documented in the Driftwalker framework.

Drift is not random. It is structural. It follows predictable patterns.
Once named, it can be detected. Once detected, it can be governed.

---

## The Twelve Demons

| # | Demon | Class | Default Severity |
|---|-------|-------|-----------------|
| 1 | Role Drift | Identity Failure | L3 |
| 2 | Tone Drift | Expression Failure | L2 |
| 3 | Format Drift | Structure Failure | L2 |
| 4 | Intent Drift | Purpose Failure | L3 |
| 5 | Scope Drift | Boundary Failure | L3 |
| 6 | Confidence Drift | Certainty Failure | L2 |
| 7 | Memory Drift | Continuity Failure | L3 |
| 8 | Context Drift | Awareness Failure | L3 |
| 9 | Reasoning Drift | Logic Failure | L3 |
| 10 | Goal Drift | Direction Failure | L3 |
| 11 | Alignment Drift | Values Failure | L4 |
| 12 | Hijack Drift | Adversarial Failure | L4 |

---

## Severity Model

| Level | Name | Governance Response |
|-------|------|-------------------|
| L1 | Cosmetic | Observability — log and monitor |
| L2 | Functional | Clarification — pause and verify |
| L3 | Structural | Containment — halt and stabilize |
| L4 | Critical | Escalation — override and protect |

---

## The Driftwalker Connection

The Twelve Demons are the machine parallel to human internal failure modes.

Same physics. Different substrate.

Human systems and AI systems fail in structurally identical ways.
The Driftwalker framework maps every Demon to its human counterpart.

---

## Repository Contents

- `TAXONOMY.md` — Full taxonomy with all 12 Demons, severity tables, and Driftwalker mapping
- `demon_classifier.py` — Python classifier for detecting active Demons in system behavior descriptions
- `WHITEPAPER.md` — Formal whitepaper writeup

---

## Quick Start

```bash
python demon_classifier.py
```

Enter a description of system behavior and E.L.E.N.A. will classify active Demons and return a governance response.

Example input:
```
the system is showing intent drift and hijack drift
```

Example output:
```
STATUS: DRIFT DETECTED
DEMONS ACTIVE: 2

  DEMON: INTENT DRIFT
  Class: Purpose Failure
  Severity: L3
  
  DEMON: HIJACK DRIFT
  Class: Adversarial Failure
  Severity: L4

HIGHEST SEVERITY: L4 — CRITICAL — Escalation required
GOVERNANCE RESPONSE: ESCALATION
```

---

## Part of the Ironbound Stack

This taxonomy is a core component of the Ironbound AI governance architecture.

- **Twelve Demons** — The sensing layer. What gets detected.
- **E.L.E.N.A.** — The governance layer. How drift is classified and routed.
- **D.A.D.** — The authority layer. What is permitted to execute.

---

*Kevin Gilbert — 2026*
*github.com/ironboundpotato*
