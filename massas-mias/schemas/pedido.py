from enum import Enum
from datetime import datetime
from time import time
from pydantic import BaseModel


class StatusPedido(str, Enum):
    pendente = '0'
    em_andamento = '1'
    enviado = '2'
    cancelado = '3'

class PedidoCreate(BaseModel):
    usuario_id: int
    prato_id: int
    status_pedido: StatusPedido
    data_pedido : datetime
    hora_pedido : time

class PedidoUpdate(BaseModel):
    usuario_id: int
    prato_id: int
    status_pedido: StatusPedido
    data_pedido: datetime
    hora_pedido: time

class PedidoRead(BaseModel):
    id_pedido: int
    usuario_id: int
    prato_id: int
    status_pedido: StatusPedido
    data_pedido: datetime
    hora_pedido: time

class PedidoReadList(BaseModel):
    pedidos: [PedidoRead]