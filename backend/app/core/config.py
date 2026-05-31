from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

    REDIS_HOST = os.getenv("REDIS_HOST")

    REDIS_PORT = int(os.getenv("REDIS_PORT"))


settings = Settings()