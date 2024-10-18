from fastapi import APIRouter, HTTPException, Depends
from models.usuario import UsuarioDB  # Ajuste conforme a estrutura do projeto
from schemas.usuario import (
    UsuarioRead,
    UsuarioCreate,
    UsuarioReadList,
    UsuarioUpdate,
    LoginData
)
from passlib.hash import bcrypt  # Para lidar com hash de senha
# from fastapi_login import LoginManager
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/usuarios', tags=['USUÁRIOS']
)
# Configure o gerenciador de login
SECRET = "123456"  # Troque isso por uma chave secreta adequada
manager = LoginManager(SECRET, token_url='/usuarios/login')

@manager.user_loader
def load_user(email: str):
    return UsuarioDB.get_or_none(UsuarioDB.email_usuario == email)

# Rota para criar um novo usuário
@router.post('', response_model=UsuarioRead)
def criar_usuario(novo_usuario: UsuarioCreate):
    # Hash da senha antes de salvar no banco de dados
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
    print(usuario_atualizado)  # Verificar os dados recebidos
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Atualizações
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
# Rota de login com resposta segura

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login")
def login(dados: LoginData):
    usuario = UsuarioDB.get_or_none(
        (UsuarioDB.email_usuario == dados.login_usuario) |
        (UsuarioDB.telefone_usuario == dados.login_usuario)
    )

    if not usuario or not bcrypt.verify(dados.senha_usuario, usuario.senha_usuario):
        raise HTTPException(status_code=400, detail="E-mail, telefone ou senha incorretos")

    # Gera um token
    access_token = manager.create_access_token(data={"sub": usuario.email_usuario})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/logado", response_model=UsuarioRead)
def obter_usuario_logado(user: UsuarioRead = Depends(manager)):
    usuario = load_user(user.email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

