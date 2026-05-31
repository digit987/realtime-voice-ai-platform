import json
import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


STREAM_NAME = "voice_events"


def publish_event(
    event_type: str,
    payload: dict
):

    redis_client.xadd(
        STREAM_NAME,
        {
            "type": event_type,
            "payload": json.dumps(
                payload
            )
        }
    )