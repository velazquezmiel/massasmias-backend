from fastapi import APIRouter, HTTPException, Depends
from peewee import fn
from schemas.dashboard import DashboardRead, Estatisticas, PedidoPendentes
from models.avaliacao import AvaliacaoDB
from models.pedido import PedidoDB
from models.prato import PratoDB
from models.reserva import ReservaDB
from models.usuario import UsuarioDB
from auth import (
    get_user_by_email_or_phone,
    create_access_token,
    authenticate_user,
    is_admin,   # Certifique-se que está implementado
    is_root,    # Certifique-se que está implementado
    get_user_from_token,
    get_current_user,
    oauth2_scheme
)

router = APIRouter()

@router.get("/dashboard", response_model=DashboardRead)
async def get_dashboard(token: str = Depends(oauth2_scheme)):
    usuario = get_user_from_token(token)

    if not (is_admin(usuario) or is_root(usuario)):
        raise HTTPException(status_code=403, detail="Acesso negado. Usuário não autorizado.")

    # Agregações e contagens para o dashboard
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

    # Busca os pedidos pendentes
    pedidos_pendentes = (
        PedidoDB.select()
        .where(PedidoDB.status_pedido == '0')
    )

    # Prepara a lista de pedidos pendentes
    # Modifique o mapeamento dos pedidos pendentes para refletir corretamente os campos
    pedidos_pendentes_list = [
        PedidoPendentes(
            id=pedido.id_pedido,
            nome=pedido.prato_id.nome_prato,  # Nome do prato
            descricao=pedido.prato_id.descricao_prato,  # Descrição do prato
            status=pedido.status_pedido,
            imagem=pedido.prato_id.imagem_prato
        )
        for pedido in pedidos_pendentes
    ]

    # Retorna o conteúdo do dashboard
    return DashboardRead(
        estatisticas=estatisticas,
        pedidos_pendentes=pedidos_pendentes_list
    )
