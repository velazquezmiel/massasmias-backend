from pydantic import BaseModel
from schemas.categoria_prato import CategoriaPratoRead

class PratoCreate(BaseModel):
    nome_prato: str
    valor_prato: float
    imagem_prato: str
    descricao_prato: str
    id_categoria_prato: int

class PratoUpdate(BaseModel):
    nome_prato: str
    valor_prato: float
    imagem_prato: str
    descricao_prato: str
    id_categoria_prato: int

class PratoRead(BaseModel):
    id_prato: int
    nome_prato: str
    valor_prato: float
    imagem_prato: str
    descricao_prato: str
    id_categoria_prato: int

class PratoReadList(BaseModel):
    pratos:list[PratoRead]