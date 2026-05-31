import json
import redis

from app.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

STREAM_NAME = "voice_events"


def publish_user_message(
    session_id: str,
    message: str
):

    redis_client.xadd(
        STREAM_NAME,
        {
            "type": "user_message",
            "payload": json.dumps(
                {
                    "session_id": session_id,
                    "message": message
                }
            )
        }
    )


def get_stream_events():

    return redis_client.xrange(
        STREAM_NAME
    )