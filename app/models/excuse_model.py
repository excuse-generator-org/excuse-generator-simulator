from pydantic import BaseModel

class ExcuseRequest(BaseModel):
    scenario: str
    authority: str
    tone: str
    severity: str
    user_id: str
