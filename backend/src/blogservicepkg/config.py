import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB = os.getenv("DB")
    DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    USE_LOCAL = os.getenv("LOCAL")

settings = Settings()