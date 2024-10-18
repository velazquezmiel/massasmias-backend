from fastapi import HTTPException
from passlib.hash import bcrypt
from datetime import datetime, timedelta
import jwt
from typing import Optional
from models.usuario import UsuarioDB  # Ajuste conforme a estrutura do projeto

# Configurações de segurança
SECRET_KEY = "sua_chave_secreta"  # Substitua por uma chave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

def get_user(email: str):
    return UsuarioDB.get_or_none(UsuarioDB.email_usuario == email)

def authenticate_user(email: str, password: str):
    user = get_user(email)
    if not user or not verify_password(password, user.senha_usuario):
        return False
    return user

def is_root(usuario) -> bool:
    """Verifica se o usuário é do tipo root (tipo_usuario = 0)."""
    return usuario.tipo_usuario == "0"

def is_admin(usuario) -> bool:
    """Verifica se o usuário é do tipo admin (tipo_usuario = 1)."""
    return usuario.tipo_usuario == "1"

def get_user_from_token(token: str):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    usuario = get_user(email=email)
    if usuario is None:
        raise credentials_exception
    return usuario