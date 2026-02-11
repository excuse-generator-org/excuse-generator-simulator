from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_excuse():
    return {"msg": "Excuse route working"}
