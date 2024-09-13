from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class TipoUsuario(str, Enum):
    cliente = '0'
    admin = '1'
    ser_supremo = '2'

class UsuarioCreate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: int
    data_nascimento: datetime
    endereco_usuario: str
    senha_usuario: str
    tipo: TipoUsuario

class UsuarioUpdate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: int
    endereco_usuario: str
    senha_usuario: str
    tipo: TipoUsuario

class UsuarioRead(BaseModel):
    id_usuario: int
    nome_usuario: str
    email_usuario: str
    telefone_usuario: int
    data_nascimento: datetime
    endereco_usuario: str
    senha_usuario: str
    tipo: TipoUsuario

class UsuarioReadList(BaseModel):
    usuarios: list[UsuarioRead]