from fastapi import FastAPI
from app.routes import excuse   # import module

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Excuse Simulator API running"}

# Register router
app.include_router(excuse.router, prefix="/excuse", tags=["Excuse"])
