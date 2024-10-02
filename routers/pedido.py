from fastapi import APIRouter, HTTPException
from models.pedido import PedidoDB
from schemas.pedido import (
    PedidoCreate,
    PedidoUpdate,
    PedidoRead,
    PedidoReadList,
)
from typing import List

router = APIRouter(
    prefix='/pedidos', tags=['PEDIDOS']
)


@router.post(path='', response_model=PedidoRead)
def criar_pedido(novo_pedido: PedidoCreate):
    pedido = PedidoDB.create(**novo_pedido.model_dump())
    return pedido


@router.get(path='', response_model=PedidoReadList)
def listar_pedidos():
    pedidos = PedidoDB.select()
    return {'pedidos': pedidos}


@router.get(path='/{id_pedido}', response_model=PedidoRead)
def obter_pedido(id_pedido: int):
    pedido = PedidoDB.get_or_none(PedidoDB.id_pedido == id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido


@router.patch(path='/{id_pedido}', response_model=PedidoRead)
def atualizar_pedido(id_pedido: int, pedido_atualizado: PedidoUpdate):
    pedido = PedidoDB.get_or_none(PedidoDB.id_pedido == id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    pedido.usuario_id = pedido_atualizado.usuario_id
    pedido.prato_id = pedido_atualizado.prato_id
    pedido.status_pedido = pedido_atualizado.status_pedido
    pedido.data_pedido = pedido_atualizado.data_pedido
    pedido.save()

    return pedido


@router.delete(path='/{id_pedido}', response_model=PedidoRead)
def excluir_pedido(id_pedido: int):
    pedido = PedidoDB.get_or_none(PedidoDB.id_pedido == id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    pedido.delete_instance()
    return pedido
