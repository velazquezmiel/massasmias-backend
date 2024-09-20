from pydantic import BaseModel, Field

class MesaCreate(BaseModel):
    codigo_mesa: str
    numero_cadeiras: int

class MesaUpdate(BaseModel):
    codigo_mesa: str
    numero_cadeiras: int

class MesaRead(BaseModel):
    id_mesa: int
    codigo_mesa: str
    numero_cadeiras: int

class MesaReadList(BaseModel):
    mesas: list[MesaRead]