from fastapi import APIRouter

from app.events.redis_streams import (
    get_stream_events
)

router = APIRouter()


@router.get("/events")

def get_events():

    return {
        "events": get_stream_events()
    }