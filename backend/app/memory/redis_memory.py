import redis
import json

from app.core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

def get_history(session_id):

    try:

        data = redis_client.get(
            session_id
        )

        if not data:

            return []

        return json.loads(
            data
        )

    except Exception:

        return []


def add_message(
    session_id: str,
    role: str,
    content: str
):

    try:

        history = get_history(
            session_id
        )

        history.append(
            {
                "role": role,
                "content": content
            }
        )

        redis_client.set(
            session_id,
            json.dumps(history)
        )

    except Exception:

        pass