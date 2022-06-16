from pydantic import BaseModel, EmailStr, Field


class UsuarioModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "Fulano de tal",
                "email": "fulano@gmail.com",
                "senha": "Fulano@123",
                "foto": "fulano.png"
            }
        }
