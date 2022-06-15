from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "OK!"
    }