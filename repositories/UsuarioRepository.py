from decouple import config
import motor.motor_asyncio

from models.UsuarioModel import UsuarioModel

MONGODB_URL = config("MONGODB_URL")

cliente = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

db = cliente.cluster0

usuarios_collection = db.get_collection("usuarios")

async def create(usuario: UsuarioModel) -> dict:
    usuario_criado = await usuarios_collection.insert_one(usuario)

    novo_usuario = await usuarios_collection.find_one({ "_id": usuario_criado.inserted_id })

    return {
        "nome": novo_usuario['nome'],
        "email": novo_usuario['email'],
        "senha": novo_usuario['senha'],
        "foto": novo_usuario['foto'],
    }
