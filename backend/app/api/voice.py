from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.services.stt_service import (
    transcribe_audio
)

router = APIRouter()


@router.post("/transcribe")
async def transcribe(
    audio: UploadFile = File(...)
):

    audio_bytes = (
        await audio.read()
    )

    transcript = (
        transcribe_audio(
            audio_bytes
        )
    )

    return {
        "transcript": transcript
    }