import json
import redis

from app.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

STREAM_NAME = "voice_events"


def start_worker():

    print("Worker Started...")

    last_id = "0"

    while True:

        messages = redis_client.xread(
            {
                STREAM_NAME: last_id
            },
            block=5000
        )

        if not messages:
            continue

        for stream_name, entries in messages:

            for message_id, data in entries:

                event_type = data["type"]

                payload = json.loads(
                    data["payload"]
                )

                print(
                    f"\nProcessing {event_type}"
                )

                print(payload)

                last_id = message_id


if __name__ == "__main__":

    start_worker()