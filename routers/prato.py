from fastapi import APIRouter, HTTPException
from models.prato import PratoDB
from schemas.prato import (
    PratoCreate,
    PratoUpdate,
    PratoRead,
    PratoReadList,
)
from typing import List

router = APIRouter(
    prefix='/pratos', tags=['PRATOS']
)


@router.post(path='', response_model=PratoRead)
def criar_prato(novo_prato: PratoCreate):
    prato = PratoDB.create(**novo_prato.dict())
    return prato


@router.get(path='', response_model=PratoReadList)
def listar_pratos():
    pratos = PratoDB.select()
    return {'pratos': pratos}


@router.get(path='/{id_prato}', response_model=PratoRead)
def obter_prato(id_prato: int):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato


@router.patch(path='/{id_prato}', response_model=PratoRead)
def atualizar_prato(id_prato: int, prato_atualizado: PratoUpdate):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    prato.nome_prato = prato_atualizado.nome_prato
    prato.valor_prato = prato_atualizado.valor_prato
    prato.imagem_prato = prato_atualizado.imagem_prato
    prato.descricao_prato = prato_atualizado.descricao_prato
    prato.categoria_prato = prato_atualizado.categoria_prato
    prato.save()

    return prato


@router.delete(path='/{id_prato}', response_model=PratoRead)
def excluir_prato(id_prato: int):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    prato.delete_instance()
    return prato
