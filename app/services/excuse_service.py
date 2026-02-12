import random

def generate_excuse_logic(data):

    reasons = {
        "technical": [
            "my laptop crashed unexpectedly",
            "my internet was down due to maintenance",
            "a software error corrupted my file"
        ],
        "medical": [
            "I had a sudden migraine",
            "I was not feeling well and had to rest",
            "I had a minor health issue"
        ],
        "personal": [
            "a family matter needed my attention",
            "an urgent personal issue came up",
            "an unexpected responsibility at home"
        ]
    }

    category = random.choice(list(reasons.keys()))
    reason = random.choice(reasons[category])

    excuse = f"I was unable to complete it on time because {reason}."

    return {
        "text": excuse,
        "category": category
    }


def calculate_believability(category, severity):

    base_scores = {
        "medical": 85,
        "personal": 75,
        "technical": 65
    }

    score = base_scores.get(category, 60)

    if severity == "high":
        score += 5
    elif severity == "low":
        score -= 5

    # human randomness
    score += random.randint(-5, 5)

    return max(0, min(score, 100))
