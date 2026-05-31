from openai import OpenAI

from app.core.config import settings

from app.memory.redis_memory import (
    get_history,
    add_message
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_response(
    session_id: str,
    message: str
):

    history = get_history(
        session_id
    )

    messages = history + [
        {
            "role": "user",
            "content": message
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=messages
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    add_message(
        session_id,
        "user",
        message
    )

    add_message(
        session_id,
        "assistant",
        answer
    )

    return answer


def stream_response(
    session_id: str,
    message: str
):

    history = get_history(
        session_id
    )

    messages = history + [
        {
            "role": "user",
            "content": message
        }
    ]

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    )

    full_response = ""

    for chunk in stream:

        delta = (
            chunk
            .choices[0]
            .delta
            .content
        )

        if delta:

            full_response += delta

            yield delta

    add_message(
        session_id,
        "user",
        message
    )

    add_message(
        session_id,
        "assistant",
        full_response
    )
    