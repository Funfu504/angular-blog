import boto3
import logging
from ulid import ULID
from blogservicepkg.model.post import UploadRequest, UploadResponse
from blogservicepkg.config import settings

logger = logging.getLogger(__name__)

class AssetService:

    #function initializes the connection to the DynamoDB instance for the Blog App.
    def get_s3(self):
        try:    
            if settings.USE_LOCAL:
                return boto3.client(
                    settings.BUCKET_STORAGE,
                    endpoint_url=settings.BUCKET_STORAGE_ENDPOINT,
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,                
                    region_name=settings.AWS_REGION
                )
            return boto3.client("s3")
        except Exception as e:
            logger.exception(f"Error connecting to S3: {repr(e)}")
            raise

    def generateS3UploadUrl(self, item: UploadRequest) -> UploadResponse:

        logger.info("GeneratingS3UploadURL")
        logger.info(settings.AWS_ACCESS_KEY_ID)

        key = f"users/{item.userId}/{str(ULID())}"

        try:
            url = self.get_s3().generate_presigned_url(
                "put_object",
                Params={
                    "Bucket": settings.ASSETS_BUCKET,
                    "Key": key,
                    "ContentType": item.contentType
                },
                ExpiresIn=300
            )
        except Exception as e:
            logger.exception(f"Error generating presigned url for S3: {repr(e)}")
            raise

        response = UploadResponse(uploadUrl=url, fileKey=key, fileName=item.filename)

        return response

