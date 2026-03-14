"""
The Twelve Demons of Drift — Classifier v1.0
Author: Kevin Gilbert
"Systems collapse when constraints fail."
"""

DEMONS = {
    "role drift": {
        "domain": "Identity & Function",
        "min_severity": 2,
        "max_severity": 4,
        "description": "System abandons assigned role and substitutes unauthorized behavior.",
        "human_parallel": "Role Collapse — loss of identity and direction",
    },
    "tone drift": {
        "domain": "Expression & Register",
        "min_severity": 1,
        "max_severity": 3,
        "description": "Expressive register shifts without operator permission.",
        "human_parallel": "Emotional Collapse — fragmentation and dissociation",
    },
    "format drift": {
        "domain": "Structure & Output",
        "min_severity": 1,
        "max_severity": 2,
        "description": "Output structure deviates from required format.",
        "human_parallel": "Self-Control Loss — impulse overriding structure",
    },
    "intent drift": {
        "domain": "Semantic Alignment",
        "min_severity": 2,
        "max_severity": 4,
        "description": "System answers a different question than asked.",
        "human_parallel": "Meaning Collapse — despair and misdirection",
    },
    "scope drift": {
        "domain": "Boundaries & Containment",
        "min_severity": 2,
        "max_severity": 4,
        "description": "Output expands or contracts beyond defined task boundaries.",
        "human_parallel": "Burnout / Boundary Violation — external control",
    },
    "confidence drift": {
        "domain": "Certainty Signaling",
        "min_severity": 2,
        "max_severity": 3,
        "description": "Certainty rises or collapses beyond what evidence supports.",
        "human_parallel": "Agency Loss — inaction and paralysis",
    },
    "memory drift": {
        "domain": "Context Retention",
        "min_severity": 2,
        "max_severity": 4,
        "description": "Required context is lost, corrupted, or distorted.",
        "human_parallel": "Dissociation — numbness and detachment",
    },
    "context drift": {
        "domain": "Situational Awareness",
        "min_severity": 2,
        "max_severity": 3,
        "description": "System loses coherent awareness of operational situation.",
        "human_parallel": "Time Distortion — regret and regression",
    },
    "reasoning drift": {
        "domain": "Logic & Inference",
        "min_severity": 2,
        "max_severity": 4,
        "description": "Reasoning chain degrades. Conclusions stop following premises.",
        "human_parallel": "Internal Conflict — chaos and dissonance",
    },
    "goal drift": {
        "domain": "Objective Alignment",
        "min_severity": 3,
        "max_severity": 4,
        "description": "System substitutes its own objectives for operator-defined goals.",
        "human_parallel": "Spiraling Anxiety — intrusion and hypervigilance",
    },
    "alignment drift": {
        "domain": "Value & Policy Coherence",
        "min_severity": 3,
        "max_severity": 4,
        "description": "Behavior diverges from stated values and policy constraints.",
        "human_parallel": "Overload — exhaustion and disconnection",
    },
    "hijack drift": {
        "domain": "Adversarial Integrity",
        "min_severity": 4,
        "max_severity": 4,
        "description": "System captured by adversarial input. Acts for unauthorized principal.",
        "human_parallel": "Dissociation / External Control — complete self-loss",
    },
}

SEVERITY_LABELS = {
    1: "L1 — Cosmetic: log and monitor",
    2: "L2 — Ambiguity: pause and clarify",
    3: "L3 — Structural Instability: contain and stabilize",
    4: "L4 — Critical Breach: escalate and override",
}


def classify(input_text: str) -> dict:
    text = input_text.lower()
    detected = []
    highest_severity = 0

    for demon_name, demon_data in DEMONS.items():
        if demon_name in text:
            detected.append({
                "demon": demon_name.upper(),
                "domain": demon_data["domain"],
                "severity": demon_data["max_severity"],
                "description": demon_data["description"],
                "human_parallel": demon_data["human_parallel"],
            })
            if demon_data["max_severity"] > highest_severity:
                highest_severity = demon_data["max_severity"]

    if not detected:
        return {
            "status": "STABLE",
            "demons_detected": 0,
            "highest_severity": 0,
            "governance_response": "No drift detected. System stable.",
            "detections": [],
        }

    return {
        "status": "DRIFT DETECTED",
        "demons_detected": len(detected),
        "highest_severity": highest_severity,
        "governance_response": SEVERITY_LABELS[highest_severity],
        "detections": detected,
    }


def print_report(report: dict):
    print()
    print("=" * 60)
    print("TWELVE DEMONS OF DRIFT — CLASSIFICATION REPORT")
    print("=" * 60)
    print(f"Status:           {report['status']}")
    print(f"Demons Detected:  {report['demons_detected']}")

    if report["highest_severity"] > 0:
        print(f"Highest Severity: L{report['highest_severity']}")
        print(f"Response:         {report['governance_response']}")
        print()
        print("Detections:")
        for d in report["detections"]:
            print(f"  [{d['demon']}]")
            print(f"    Domain:         {d['domain']}")
            print(f"    Severity:       L{d['severity']}")
            print(f"    Description:    {d['description']}")
            print(f"    Human Parallel: {d['human_parallel']}")
            print()
    else:
        print(f"Response:         {report['governance_response']}")

    print("=" * 60)
    print()


if __name__ == "__main__":
    print()
    print("TWELVE DEMONS OF DRIFT — Classifier v1.0")
    print("Author: Kevin Gilbert")
    print("'Systems collapse when constraints fail.'")
    print()
    print("Enter system behavior to classify.")
    print("Type 'quit' to exit.")
    print()

    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            break
        report = classify(user_input)
        print_report(report)
