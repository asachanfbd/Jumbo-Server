from fastapi import FastAPI
from src.app.api import brain

app = FastAPI(title="Jumbo Server", version="0.1.0")

app.include_router(brain.router)

@app.get("/")
def health_check():
    return {"status": "ok", "app": "Jumbo Server"}
