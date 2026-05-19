import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB = os.getenv("DB")
    DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    USE_LOCAL = os.getenv("LOCAL")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    S3 = os.getenv("S3")
    S3_ENDPOINT = os.getenv("S3_ENDPOINT")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


settings = Settings()