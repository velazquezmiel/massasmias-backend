from pydantic import BaseModel
from typing import List
from schemas.prato import ImagemPratoPedido

class Estatisticas(BaseModel):
    media_avaliacoes: float
    numero_pedidos: int
    numero_pratos: int
    numero_reservas: int
    numero_usuarios: int

class PedidoPendentes(BaseModel):
    id: int
    nome: str
    descricao: str
    status: str
    imagem: str

class DashboardRead(BaseModel):
    estatisticas: Estatisticas
    pedidos_pendentes: List[PedidoPendentes]
