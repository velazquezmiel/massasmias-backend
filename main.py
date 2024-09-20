from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from config.database import shutdown_db, startup_db
from routers.avaliacao import router as avaliacao_router
from routers.categoria_prato import router as categoria_prato_router
from routers.mesa import router as mesa_router
from routers.pedido import router as pedido_router
from routers.prato import router as prato_router
from routers.reserva import router as reserva_router
from routers.usuario import router as usuario_router


app = FastAPI(title='MASSAS MIAS')

app.add_event_handler(event_type='startup', func=startup_db)
app.add_event_handler(event_type='shutdown', func=shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def status():
    return {
        'status': 'ok',
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

app.include_router(avaliacao_router)
app.include_router(categoria_prato_router)
app.include_router(mesa_router)
app.include_router(pedido_router)
app.include_router(prato_router)
app.include_router(reserva_router)
app.include_router(usuario_router)