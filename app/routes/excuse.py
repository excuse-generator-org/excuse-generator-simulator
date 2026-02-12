from fastapi import APIRouter
from app.models.excuse_model import ExcuseRequest
from app.db.mongo import excuse_collection, users_collection

def get_or_create_user(user_id):

    user = users_collection.find_one({"user_id": user_id})

    if not user:
        user = {
            "user_id": user_id,
            "trust_points": 50,
            "total_excuses": 0
        }
        users_collection.insert_one(user)

    return user

from app.services.excuse_service import (
    generate_excuse_logic,
    calculate_believability
)
from app.db.mongo import excuse_collection
from datetime import datetime

router = APIRouter()

@router.post("/generate")
def generate_excuse(req: ExcuseRequest):
    user = get_or_create_user(req.user_id)

    # Generate excuse
    result = generate_excuse_logic(req)

    # Calculate score
    score = calculate_believability(
        result["category"],
        req.severity
    )

    excuse_doc = {
        "user_id": req.user_id,
        "scenario": req.scenario,
        "authority": req.authority,
        "tone": req.tone,
        "severity": req.severity,
        "excuse_text": result["text"],
        "category": result["category"],
        "believability_score": score,
        "created_at": datetime.utcnow()
    }

    excuse_collection.insert_one(excuse_doc)

    return {
        "excuse": result["text"],
        "category": result["category"],
        "believability_score": score
    }
