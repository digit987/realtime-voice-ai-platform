from app.services.llm_service import (
    stream_response
)


def run_conversation_agent(
    session_id: str,
    message: str
):

    return stream_response(
        session_id,
        message
    )