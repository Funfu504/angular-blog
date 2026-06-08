import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    USE_LOCAL = os.getenv("LOCAL")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    DB = os.getenv("DB")
    DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")    
    BUCKET_STORAGE = os.getenv("BUCKET_STORAGE")
    BUCKET_STORAGE_ENDPOINT = os.getenv("BUCKET_STORAGE_ENDPOINT")
    ASSETS_BUCKET = os.getenv("ASSETS_BUCKET")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


settings = Settings()