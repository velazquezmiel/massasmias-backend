from fastapi import APIRouter, HTTPException
from models.usuario import UsuarioDB  # Adjust the import according to your project structure
from schemas.usuario import (
    UsuarioRead,
    UsuarioCreate,
    UsuarioReadList,
    UsuarioUpdate
)

router = APIRouter(
    prefix='/usuarios', tags=['USUÁRIOS']
)

@router.post(path='', response_model=UsuarioRead)
def criar_usuario(novo_usuario: UsuarioCreate):
    usuario = UsuarioDB.create(**novo_usuario.model_dump())
    return usuario

@router.get('', response_model=UsuarioReadList)
def listar_usuario():
    usuarios = UsuarioDB.select()
    return {'usuarios': usuarios}

@router.get('/{id_usuario}', response_model=UsuarioRead)
def listar_usuario_por_id(id_usuario: int):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.patch('/{id_usuario}', response_model=UsuarioRead)
def atualizar_usuario(id_usuario: int, usuario_atualizado: UsuarioUpdate):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.nome_usuario = usuario_atualizado.nome_usuario
    usuario.email_usuario = usuario_atualizado.email_usuario
    usuario.telefone_usuario = usuario_atualizado.telefone_usuario
    usuario.endereco_usuario = usuario_atualizado.endereco_usuario
    usuario.senha_usuario = usuario_atualizado.senha_usuario
    usuario.save()

    return usuario

@router.delete('/{id_usuario}', response_model=UsuarioRead)
def excluir_usuario(id_usuario: int):
    usuario = UsuarioDB.get_or_none(UsuarioDB.id_usuario == id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.delete_instance()
    return usuario
