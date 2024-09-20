from enum import Enum
from pydantic import BaseModel
from datetime import date

class TipoUsuario(str, Enum):
    cliente = '0'
    admin = '1'
    ser_supremo = '2'

class UsuarioCreate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str  # Change to str to avoid int limits
    data_nascimento: date
    endereco_usuario: str
    senha_usuario: str
    tipo_usuario: TipoUsuario

class UsuarioUpdate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str  # Change to str
    endereco_usuario: str
    senha_usuario: str
    tipo_usuario: TipoUsuario

class UsuarioRead(BaseModel):
    id_usuario: int
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str  # Change to str
    data_nascimento: date
    endereco_usuario: str
    senha_usuario: str
    tipo_usuario: TipoUsuario

class UsuarioReadWithAvaliacao(BaseModel):
    id_usuario: int
    nome_usuario: str
    email_usuario: str


class UsuarioReadList(BaseModel):
    usuarios: list[UsuarioRead]
