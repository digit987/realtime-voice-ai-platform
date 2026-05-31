from fastapi import APIRouter

from fastapi.responses import FileResponse

from pydantic import BaseModel

from app.services.tts_service import (
    generate_speech
)


router = APIRouter()


class SpeechRequest(
    BaseModel
):
    text: str


@router.post("/speak")
async def speak(
    request: SpeechRequest
):

    audio_file = (
        generate_speech(
            request.text
        )
    )

    return FileResponse(
        audio_file,
        media_type="audio/mpeg"
    )