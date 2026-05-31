from fastapi import FastAPI
from fastapi import WebSocket

from app.api.health import router as health_router
from app.api.events import router as events_router
from app.api.voice import router as voice_router
from app.api.tts import router as tts_router
from app.api.metrics import router as metrics_router

from app.websocket.chat_socket import (
    websocket_chat
)

app = FastAPI(
    title="Realtime Voice AI Platform"
)

app.include_router(
    health_router,
    prefix="/api"
)

app.include_router(
    events_router,
    prefix="/api"
)

app.include_router(
    voice_router,
    prefix="/api"
)

app.include_router(
    tts_router,
    prefix="/api"
)

app.include_router(
    metrics_router,
    prefix="/api"
)


@app.websocket("/ws/chat")
async def chat_endpoint(
    websocket: WebSocket
):
    await websocket_chat(
        websocket
    )