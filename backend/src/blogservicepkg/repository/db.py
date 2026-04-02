import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from blogservicepkg.config import settings
from blogservicepkg.model.blogpost import BlogPost
import json

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

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_post(post_id: str) -> list[dict] :
    table = get_post_table()
    response = table.query(
        KeyConditionExpression=Key("Post_Id").eq(post_id))
    
    items = response["Items"]
    return items

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_posts(post_element_type: str, limit: int) -> list[str] :
    table = get_post_table()
    
    response = table.query(
        IndexName="GSI_PostsByPostDate",
        KeyConditionExpression=Key("Post_Element_Type").eq(post_element_type),
        ScanIndexForward=False,
        Limit=limit
    )

    #the below code retrieves the Post_Ids from the response list of dictionary items
    post_ids = [item["Post_Id"] for item in response["Items"]]

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

def put_post(items: list[dict]):
    table = get_post_table()
    for item in items:
        response = table.put_item(Item=item)

#function to convert the fragmented database records associated to a blog post into a BlogPost domain entity.
def build_post_entity(items: list[dict]) -> BlogPost:
    if not items:
        return None
    
    post = BlogPost(items[0]["Post_Id"])

    # for each element, identify what type of element it is, convert the type's Value collection into
    # a json object and map the contents as appropriate.
    for item in items:
        element_type = item["Post_Element_Type"]
        value_element = json.loads(item.get("Value"))        

        if element_type == "METADATA":
            post.addMetadata(value_element.get("title"), value_element.get("summary"))            
            featured, postDate = item["Featured_Post_Date"].split("#", 1)
            post.addPostDate(postDate)
            post.addFeaturedFlag(featured)
        elif element_type == "CONTENT":
            post.addContent(value_element.get("blogtext"))            
        elif element_type == "IMAGE":
            post.addImage(value_element.get("url"), value_element.get("alttext"))

    return post

#fetch a post based on the post id from the database and return the domain entity.
def getBlogPost(post_id: str) -> BlogPost:
    thePost = get_post(post_id)
    return build_post_entity(thePost)

#fetch a list of featured posts from the database and return the list as domain entities.
def getFeaturedBlogPosts(numPosts: int) -> list[BlogPost]:
    postIdList = get_featured_posts("METADATA", numPosts)
    postList = []
    for postId in postIdList :        
        postList.append(getBlogPost(postId))
    return postList

#fetch a list of posts from the database and return the list as domain entities.
def getBlogPosts(numPosts: int) -> list[BlogPost]:
    postIdList = get_posts("METADATA", numPosts)
    postList = []
    for postId in postIdList :        
        postList.append(getBlogPost(postId))
    return postList


