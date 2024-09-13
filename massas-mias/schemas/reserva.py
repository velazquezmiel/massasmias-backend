from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from time import time

class ReservaCreate(BaseModel):
    usuario_id: int
    mesa_id: int
    hora_reserva: time
    data_reservada: datetime


class ReservaUpdate(BaseModel):
    mesa_id: int
    hora_reserva: time
    data_reservada: datetime

class ReservaRead(BaseModel):
    id_reserva: int
    usuario_id: int
    mesa_id: int
    hora_reserva: time
    data_reservada: datetime


class ReservaReadList(BaseModel):
    reservas: list[ReservaRead]