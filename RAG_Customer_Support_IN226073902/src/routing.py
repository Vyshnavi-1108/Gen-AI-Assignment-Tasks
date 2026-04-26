def decide_route(answer):
    answer = answer.lower()

    escalation_keywords = [
        "i don't know",
        "not available",
        "unable to find",
        "insufficient context"
    ]

    for keyword in escalation_keywords:
        if keyword in answer:
            return "HITL"

    return "OUTPUT"