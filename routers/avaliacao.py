from fastapi import APIRouter, HTTPException
from models.avaliacao import AvaliacaoDB
from schemas.avaliacao import (
    AvaliacaoCreate,
    AvaliacaoRead,
    AvaliacaoReadList,
)
from datetime import datetime

router = APIRouter(prefix='/avaliacoes', tags=['AVALIAÇÕES'])

# Criar nova avaliação
@router.post(path='', response_model=AvaliacaoRead)
def criar_avaliacao(nova_avaliacao: AvaliacaoCreate):
    nova_avaliacao.data_avaliacao = datetime.now()  # Adiciona data automaticamente
    avaliacao = AvaliacaoDB.create(**nova_avaliacao.model_dump())
    return avaliacao

# Listar todas avaliações
@router.get(path='', response_model=AvaliacaoReadList)
def listar_avaliacoes():
    avaliacoes = AvaliacaoDB.select()
    return {'avaliacoes': list(avaliacoes)}

# Listar uma avaliação específica
@router.get(path='/{avaliacao_id}', response_model=AvaliacaoRead)
def listar_uma_avaliacao(avaliacao_id: int):
    avaliacao = AvaliacaoDB.get_or_none(AvaliacaoDB.id_avaliacao == avaliacao_id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao

# Excluir avaliação
@router.delete(path='/{avaliacao_id}', response_model=AvaliacaoRead)
def excluir_avaliacao(avaliacao_id: int):
    avaliacao = AvaliacaoDB.get_or_none(AvaliacaoDB.id_avaliacao == avaliacao_id)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    avaliacao.delete_instance()
    return avaliacao

@router.post("/comentarios/")
async def registrar_comentario(novo_comentario: AvaliacaoCreate):
    comentario = AvaliacaoDB.create(**novo_comentario.model_dump())
    return {"message": "Comentário registrado com sucesso!"}

