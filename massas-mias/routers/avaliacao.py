from fastapi import APIRouter
from models.avaliacao import AvaliacaoDB
from schemas.avaliacao import (
    AvaliacaoCreate,
    AvaliacaoRead,
    AvaliacaoReadList,
)

router = APIRouter(prefix='/avaliacoes', tags=['AVALIAÇÕES'])


@router.post(path='', response_model=AvaliacaoRead)
def criar_avaliacao(nova_avaliacao: AvaliacaoCreate):
    avaliacao = AvaliacaoDB.create(**nova_avaliacao.model_dump())
    return avaliacao


@router.get(path='', response_model=AvaliacaoReadList)
def listar_avaliacao():
    avaliacoes = AvaliacaoDB.select()
    return {'avaliacoes': avaliacoes}


@router.get(path='/{avaliacao_id}', response_model=AvaliacaoRead)
def listar_avaliacao(avaliacao_id: int):
    avaliacao = AvaliacaoDB.get_or_none(AvaliacaoDB.id_avaliacao == avaliacao_id)
    return avaliacao

@router.delete(path='/{avaliacao_id}', response_model=AvaliacaoRead)
def excluir_avaliacao(avaliacao_id: int):
    avaliacao = AvaliacaoDB.get_or_none(AvaliacaoDB.id_avaliacao == avaliacao_id)
    avaliacao.delete_instance()
    return avaliacao