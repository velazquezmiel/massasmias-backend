from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.usuario import (
    UsuarioRead,
    UsuarioCreate,
    UsuarioReadList,
    UsuarioUpdate
)
from models.usuario import UsuarioDB
from auth import (
    create_access_token,
    authenticate_user,
    get_user_from_token,
)
from passlib.hash import bcrypt

router = APIRouter(
    prefix='/usuarios', tags=['USUÁRIOS']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

# Rota para criar um novo usuário
@router.post('', response_model=UsuarioRead)
def criar_usuario(novo_usuario: UsuarioCreate):
    novo_usuario.senha_usuario = bcrypt.hash(novo_usuario.senha_usuario)
    usuario = UsuarioDB.create(**novo_usuario.model_dump())
    return usuario

# Rota para listar todos os usuários
@router.get('', response_model=UsuarioReadList)
def listar_usuario():
    usuarios = UsuarioDB.select()
    return {'usuarios': usuarios}

# Rota para listar usuário por ID
@router.get('/{id_usuario}', response_model=UsuarioRead)
def listar_usuario_por_id(id_usuario: int):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Rota para atualizar um usuário
@router.patch('/{id_usuario}', response_model=UsuarioRead)
def atualizar_usuario(id_usuario: int, usuario_atualizado: UsuarioUpdate):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.nome_usuario = usuario_atualizado.nome_usuario
    usuario.email_usuario = usuario_atualizado.email_usuario
    usuario.telefone_usuario = usuario_atualizado.telefone_usuario
    usuario.endereco_usuario = usuario_atualizado.endereco_usuario
    usuario.tipo_usuario = usuario_atualizado.tipo_usuario

    if usuario_atualizado.senha_usuario:
        usuario.senha_usuario = bcrypt.hash(usuario_atualizado.senha_usuario)

    usuario.save()
    return usuario

# Rota para excluir um usuário
@router.delete('/{id_usuario}', response_model=UsuarioRead)
def excluir_usuario(id_usuario: int):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.delete_instance()
    return usuario

# Rota de login
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

    access_token = create_access_token(data={"sub": user.email_usuario})
    return {"access_token": access_token, "token_type": "bearer"}

# Rota para obter usuário logado
@router.get("/logado", response_model=UsuarioRead)
def obter_usuario_logado(token: str = Depends(oauth2_scheme)):
    return get_user_from_token(token)  # Usa a função de autenticação
