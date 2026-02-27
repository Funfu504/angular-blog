import boto3
from botocore.exceptions import ClientError
from blogservicepkg.config import settings

#function initializes the connection to the DynamoDB instance for the Blog App.
def get_dynamodb():
    try:    
        if settings.USE_LOCAL:
            return boto3.resource(
                settings.DB,
                endpoint_url=settings.DYNAMODB_ENDPOINT,
                region_name=settings.AWS_REGION
            )
        return boto3.resource("dynamodb")
    except ClientError as e:
        print(f"Error reading item: {e.response['Error']['Message']}")
        raise

#function returns a handle to the DynamoDB Blog_Post table.
def get_post_table():
    return get_dynamodb().Table("Blog_Post")
