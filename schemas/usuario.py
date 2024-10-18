from enum import Enum
from pydantic import BaseModel, constr, Field
from datetime import date

class TipoUsuario(str, Enum):
    cliente = '0'
    admin = '1'
    ser_supremo = '2'

class UsuarioCreate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str  # Alterado para str para evitar limites de int
    data_nascimento: date
    endereco_usuario: str
    senha_usuario: str
    tipo_usuario: TipoUsuario

class UsuarioUpdate(BaseModel):
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str
    endereco_usuario: str
    senha_usuario: str = Field(default=None, nullable=True)  # Torna senha opcional
    tipo_usuario: TipoUsuario


class UsuarioRead(BaseModel):
    id_usuario: int
    nome_usuario: str
    email_usuario: str
    telefone_usuario: str  # Alterado para str
    data_nascimento: date
    endereco_usuario: str
    senha_usuario: str
    tipo_usuario: TipoUsuario

class UsuarioReadWithAvaliacao(BaseModel):
    id_usuario: int
    nome_usuario: str
    email_usuario: str

class UsuarioReadPedido(BaseModel):
    id_usuario: int
    nome_usuario: str
    telefone_usuario: str
    endereco_usuario: str

class UsuarioReadReserva(BaseModel):
    id_usuario: int
    nome_usuario: str
    telefone_usuario: str
    email_usuario: str

class LoginData(BaseModel):
    login_usuario: str  # Pode ser e-mail ou telefone
    senha_usuario: str


class UsuarioReadList(BaseModel):
    usuarios: list[UsuarioRead]
