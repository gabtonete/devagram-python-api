from fastapi import APIRouter, Body

from models.UsuarioModel import UsuarioModel
from repositories.UsuarioRepository import create

router = APIRouter()

@router.post("/", response_description="Rota para criar novo usuário")
async def create(usuario: UsuarioModel = Body(...)):
    resultado = await create(usuario)

    return resultado