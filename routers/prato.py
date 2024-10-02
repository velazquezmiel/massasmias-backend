from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
import os

# Supondo que você tenha um modelo de banco de dados definido
from models.prato import PratoDB
from schemas.prato import PratoCreate, PratoUpdate, PratoRead, PratoReadList

router = APIRouter(
    prefix='/pratos', tags=['PRATOS']
)

@router.post('', response_model=PratoRead)
async def criar_prato(
        nome_prato: str = Form(...),
        valor_prato: float = Form(...),
        imagem_prato: UploadFile = File(...),
        descricao_prato: str = Form(...),
        id_categoria_prato: int = Form(...)
):
    os.makedirs('images', exist_ok=True)

    caminho_imagem = os.path.join('images', imagem_prato.filename)

    with open(caminho_imagem, 'wb') as f:
        f.write(await imagem_prato.read())

    prato = PratoDB.create(
        nome_prato=nome_prato,
        valor_prato=valor_prato,
        imagem_prato=caminho_imagem,
        descricao_prato=descricao_prato,
        id_categoria_prato=id_categoria_prato
    )
    return prato

@router.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = os.path.join("images", image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path)
    raise HTTPException(status_code=404, detail="Imagem não encontrada")

@router.get(path='', response_model=PratoReadList)
def listar_pratos():
    pratos = PratoDB.select()
    return {'pratos': pratos}

@router.get(path='/{id_prato}', response_model=PratoRead)
def obter_prato(id_prato: int):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")
    return prato

@router.patch(path='/{id_prato}', response_model=PratoRead)
def atualizar_prato(id_prato: int, prato_atualizado: PratoUpdate):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    prato.nome_prato = prato_atualizado.nome_prato
    prato.valor_prato = prato_atualizado.valor_prato
    prato.imagem_prato = prato_atualizado.imagem_prato
    prato.descricao_prato = prato_atualizado.descricao_prato
    prato.id_categoria_prato = prato_atualizado.id_categoria_prato
    prato.save()

    return prato

@router.delete(path='/{id_prato}', response_model=PratoRead)
def excluir_prato(id_prato: int):
    prato = PratoDB.get_or_none(PratoDB.id_prato == id_prato)
    if not prato:
        raise HTTPException(status_code=404, detail="Prato não encontrado")

    prato.delete_instance()
    return prato
