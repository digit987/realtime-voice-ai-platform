from fastapi import WebSocket

from starlette.websockets import (
    WebSocketDisconnect
)

import json
import time

from app.events.redis_streams import (
    publish_user_message
)

from app.agents.routing_agent import (
    route_message
)

from app.agents.calculator_agent import (
    run_calculator_agent
)

from app.agents.knowledge_agent import (
    run_knowledge_agent
)

from app.agents.conversation_agent import (
    run_conversation_agent
)

from app.monitoring.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
    CONVERSATION_AGENT_COUNT,
    CALCULATOR_AGENT_COUNT,
    KNOWLEDGE_AGENT_COUNT
)


async def websocket_chat(
    websocket: WebSocket
):

    await websocket.accept()

    try:

        while True:

            start_time = time.time()

            payload = json.loads(
                await websocket.receive_text()
            )

            session_id = payload[
                "session_id"
            ]

            user_message = payload[
                "message"
            ]

            REQUEST_COUNT.inc()

            publish_user_message(
                session_id,
                user_message
            )

            selected_agent = (
                route_message(
                    user_message
                )
            )

            print(
                f"Session: {session_id}"
            )

            print(
                f"Selected Agent: {selected_agent}"
            )

            if selected_agent == "calculator":

                CALCULATOR_AGENT_COUNT.inc()

                result = (
                    run_calculator_agent(
                        user_message
                    )
                )

                await websocket.send_text(
                    result
                )

                await websocket.send_text(
                    "[END]"
                )

            elif selected_agent == "knowledge":

                KNOWLEDGE_AGENT_COUNT.inc()

                result = (
                    run_knowledge_agent(
                        user_message
                    )
                )

                await websocket.send_text(
                    result
                )

                await websocket.send_text(
                    "[END]"
                )

            else:

                CONVERSATION_AGENT_COUNT.inc()

                for token in (
                    run_conversation_agent(
                        session_id,
                        user_message
                    )
                ):

                    await websocket.send_text(
                        token
                    )

                await websocket.send_text(
                    "[END]"
                )

            REQUEST_LATENCY.observe(
                time.time() - start_time
            )

    except WebSocketDisconnect:

        print(
            "Client disconnected"
        )