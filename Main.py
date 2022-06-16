from fastapi import FastAPI
from pydantic import BaseModel
from routes.UsuarioRoute import router as UsuarioRoute

app = FastAPI()

app.include_router(UsuarioRoute, tags=["Usuario"], prefix="/api/usuario")

@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status": "OK!"
    }