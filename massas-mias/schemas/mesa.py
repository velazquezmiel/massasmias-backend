from pydantic import BaseModel, Field

class MesaCreate(BaseModel):
    codigo_mesa: str
    numero_cadeira: int

class MesaUpdate(BaseModel):
    codigo_mesa: str
    numero_cadeira: int

class MesaRead(BaseModel):
    id_mesa: int
    codigo_mesa: str
    numero_cadeira: int

class MesaReadList(BaseModel):
    mesas: [MesaRead]