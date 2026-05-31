from openai import OpenAI

from app.core.config import settings

import tempfile


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def transcribe_audio(
    audio_bytes: bytes
):

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=True
    ) as temp_audio:

        temp_audio.write(
            audio_bytes
        )

        temp_audio.flush()

        with open(
            temp_audio.name,
            "rb"
        ) as audio_file:

            transcript = (
                client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            )

    return transcript.text