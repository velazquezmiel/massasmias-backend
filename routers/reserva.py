from fastapi import APIRouter, HTTPException
from models.reserva import ReservaDB
from schemas.reserva import (
    ReservaCreate,
    ReservaUpdate,
    ReservaRead,
    ReservaReadList,
)

router = APIRouter(
    prefix='/reservas', tags=['RESERVAS']
)


@router.post(path='', response_model=ReservaRead)
def criar_reserva(nova_reserva: ReservaCreate):
    reserva = ReservaDB.create(**nova_reserva.dict())
    return reserva


@router.get(path='', response_model=ReservaReadList)
def listar_reservas():
    reservas = ReservaDB.select()
    return {'reservas': reservas}


@router.get(path='/{id_reserva}', response_model=ReservaRead)
def obter_reserva(id_reserva: int):
    reserva = ReservaDB.get_or_none(ReservaDB.id_reserva == id_reserva)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reserva


@router.patch(path='/{id_reserva}', response_model=ReservaRead)
def atualizar_reserva(id_reserva: int, reserva_atualizada: ReservaUpdate):
    reserva = ReservaDB.get_or_none(ReservaDB.id_reserva == id_reserva)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    reserva.mesa_id = reserva_atualizada.mesa_id
    reserva.data_reservada = reserva_atualizada.data_reservada
    reserva.save()
    return reserva


@router.delete(path='/{id_reserva}', response_model=ReservaRead)
def excluir_reserva(id_reserva: int):
    reserva = ReservaDB.get_or_none(ReservaDB.id_reserva == id_reserva)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    reserva.delete_instance()
    return reserva
