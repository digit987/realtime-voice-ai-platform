from openai import OpenAI

from app.core.config import settings

import tempfile


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_speech(
    text: str
):

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=text
    ) as response:

        response.stream_to_file(
            temp_file.name
        )

    return temp_file.name