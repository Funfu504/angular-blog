import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from blogservicepkg.config import settings
from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.repository.dbmapper import PostDBMapper
import logging
import time

logger = logging.getLogger(__name__)

#function initializes the connection to the DynamoDB instance for the Blog App.
def get_dynamodb():
    try:    
        if settings.USE_LOCAL:
            return boto3.resource(
                settings.DB,
                endpoint_url=settings.DYNAMODB_ENDPOINT,
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,                
                region_name=settings.AWS_REGION
            )
        return boto3.resource("dynamodb")
    except ClientError as e:
        logger.error(f"Error reading item: {e.response['Error']['Message']}")
        raise

#function returns a handle to the DynamoDB Blog_Post table.
def get_post_table():
    return get_dynamodb().Table("Blog_Post")

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_post(post_id: str) -> BlogPost :

    start = time.perf_counter()

    table = get_post_table()
    response = table.query(
        KeyConditionExpression=Key("Post_Id").eq(post_id))
    
    logger.info(
    f"Post_Id execution took {(time.perf_counter()-start)*1000:.0f} ms")

    items = response["Items"]
    theBlogPost = PostDBMapper.build_post_entity(items)
    return theBlogPost

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_posts(post_element_type: str, limit: int) -> list[str] :
    
    dbstart = time.perf_counter()
    
    table = get_post_table()

    logger.info(
    f"DynamoDB init took {(time.perf_counter()-dbstart)*1000:.0f} ms")
    
    qrystart = time.perf_counter()

    response = table.query(
        IndexName="GSI_PostsByPostDate",
        KeyConditionExpression=Key("Post_Element_Type").eq(post_element_type),
        ScanIndexForward=False,
        Limit=limit
    )

    logger.info(
    f"GSI_PostsByPostDate execution took {(time.perf_counter()-qrystart)*1000:.0f} ms")

    #the below code retrieves the Post_Ids from the response list of dictionary items
    post_ids = [item["Post_Id"] for item in response["Items"]]

    logger.info(
    f"Gathering Post Ids took {(time.perf_counter()-dbstart)*1000:.0f} ms")

    #items = response["Items"]
    return post_ids

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_featured_posts(post_element_type: str, limit: int) -> list[str] :
    table = get_post_table()
    
    response = table.query(
        IndexName="GSI_PostsByFeaturePostDate",
        KeyConditionExpression=Key("Post_Element_Type").eq(post_element_type) 
            & Key("Featured_Post_Date").begins_with("1"),
        ScanIndexForward=False,
        Limit=limit
    )

    #the below code retrieves the Post_Ids from the response list of dictionary items
    post_ids = [item["Post_Id"] for item in response["Items"]]
    
    return post_ids

#def put_post(items: list[dict]):
def put_post(items: BlogPost):
    theDBRecordList = PostDBMapper.build_dynamoDb_entries(items) 
    table = get_post_table()
    for item in theDBRecordList:
        response = table.put_item(Item=item)



