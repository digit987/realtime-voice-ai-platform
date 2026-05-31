from fastapi import FastAPI

from fastapi import WebSocket

from app.api.health import router as health_router

from app.websocket.chat_socket import websocket_chat


app = FastAPI(
    title="Realtime Voice AI Platform"
)


app.include_router(
    health_router,
    prefix="/api"
)


@app.websocket("/ws/chat")
async def chat_endpoint(
    websocket: WebSocket
):

    await websocket_chat(
        websocket
    )