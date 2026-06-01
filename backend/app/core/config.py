from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    REDIS_HOST = os.getenv(
        "REDIS_HOST",
        "localhost"
    )

    REDIS_PORT = int(
        os.getenv(
            "REDIS_PORT",
            "6379"
        )
    )


settings = Settings()