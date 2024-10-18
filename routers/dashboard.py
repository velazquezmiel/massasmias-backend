from fastapi import APIRouter, HTTPException
from peewee import fn
from schemas.dashboard import DashboardRead, Estatisticas, PedidoPendentes
from models.avaliacao import AvaliacaoDB
from models.pedido import PedidoDB
from models.prato import PratoDB
from models.reserva import ReservaDB
from models.usuario import UsuarioDB
import os
from fastapi.responses import FileResponse


router = APIRouter()

@router.get("/dashboard", response_model=DashboardRead)
async def get_dashboard():
    media_avaliacoes = round(AvaliacaoDB.select(fn.AVG(AvaliacaoDB.estrela_avaliacao)).scalar() or 0, 1)
    numero_pedidos = PedidoDB.select().count()
    numero_pratos = PratoDB.select().count()
    numero_reservas = ReservaDB.select().count()
    numero_usuarios = UsuarioDB.select().count()



    estatisticas = Estatisticas(
        media_avaliacoes=media_avaliacoes,
        numero_pedidos=numero_pedidos,
        numero_pratos=numero_pratos,
        numero_reservas=numero_reservas,
        numero_usuarios=numero_usuarios
    )

    pedidos_pendentes = (
        PedidoDB.select()
        .where(PedidoDB.status_pedido == '0')
    )

    pedidos_pendentes_list = [
        PedidoPendentes(
            id=pedido.id_pedido,
            nome=pedido.prato_id.nome_prato,
            descricao=pedido.prato_id.descricao_prato,
            status=pedido.status_pedido,
        )
        for pedido in pedidos_pendentes
    ]


    return DashboardRead(estatisticas=estatisticas, pedidos_pendentes=pedidos_pendentes_list)
