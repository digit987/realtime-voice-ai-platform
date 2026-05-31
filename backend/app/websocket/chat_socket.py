from fastapi import WebSocket

from starlette.websockets import WebSocketDisconnect

from app.services.llm_service import (
    generate_response
)


async def websocket_chat(
    websocket: WebSocket
):

    await websocket.accept()

    # session_id = str(
    #     id(websocket)
    # )

    session_id = "streamlit-user"

    try:

        while True:

            user_message = (
                await websocket.receive_text()
            )

            response = generate_response(
                session_id,
                user_message
            )

            await websocket.send_text(
                response
            )

    except WebSocketDisconnect:

        print(
            f"Session disconnected: {session_id}"
        )