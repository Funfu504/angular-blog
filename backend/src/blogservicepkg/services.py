from .db import get_post_table
from boto3.dynamodb.conditions import Key
import json

#function to convert the fragmented database records associated to a blog post into a single JSON response.
def build_post_response(items: list[dict]) -> dict:
    if not items:
        return None

    post = {
        "postId": items[0]["Post_Id"],
        "meta": None,
        "content": None,
        "images": [],
        "postDate": None,
        "featured": None
    }

    # for each element, identify what type of element it is, convert the type's Value collection into
    # a json object and map the contents as appropriate.
    for item in items:
        element_type = item["Post_Element_Type"]
        value_element = json.loads(item.get("Value"))        

        if element_type == "METADATA":
            post["meta"] = {
                "title": value_element.get("title"),
                "summary": value_element.get("summary")
            }
            post["featured"], post["postDate"] = item["Featured_Post_Date"].split("#", 1)
        elif element_type == "CONTENT":
            post["content"] = value_element.get("blogtext")
        elif element_type == "IMAGE":
            post["images"].append({
                "url": value_element.get("url"),
                "caption": value_element.get("alttext")
            })

    return post

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_post(post_id: str) -> list[dict] :
    table = get_post_table()
    response = table.query(
        KeyConditionExpression=Key("Post_Id").eq(post_id))
    items = response["Items"]
    return items

def deconstruct_post(post: dict) -> list[dict]:
    items = []

    if "postId" in post:
        postId = post.get("postId")

    if "postDate" in post:
        postDate = post.get("postDate")
        
    if "featured" in post:
        featured = post.get("featured")
    else:
        featured = 0

    if "meta" in post:
        item = {}
        item["Post_Id"] = postId
        item["Post_Element_Type"] = "METADATA"
        item["Featured_Post_Date"] = f"{featured}#{postDate}"
        item["Value"] = post["meta"]
        items.append(item)
    
    if "content" in post:
        item = {}
        item["Post_Id"] = postId
        item["Post_Element_Type"] = "CONTENT"
        item["Value"] = {"blogtext": post.get("content")}
        items.append(item)
    
    if "images" in post:
        for image in post["images"] :
            item = {}
            item["Post_Id"] = postId
            item["Post_Element_Type"] = "IMAGE"
            item["Value"] = {"url": image.get("url"), "alttext" : image.get("caption")}
            items.append(item)

    return items

def put_post(items: list[dict]):
    table = get_post_table()
    for item in items:
        response = table.put_item(Item=item)

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_posts(post_element_type: str, limit: int) -> list[dict] :
    table = get_post_table()
    
    response = table.query(
        IndexName="PostsByPostDate",
        KeyConditionExpression=Key("Post_Element_Type").eq(post_element_type),
        ScanIndexForward=False,
        Limit=limit
    )

    #the below code retrieves the Post_Ids from the response list of dictionary items
    #post_ids = [item["Post_Id"] for item in response["Items"]]

    items = response["Items"]
    return items

# function passes in a target post id and returns a list of dictionaries.
# each dictionary entity contains an element of a single blog post.
def get_featured_posts(post_element_type: str, limit: int) -> list[str] :
    table = get_post_table()
    
    response = table.query(
        IndexName="PostsByFeaturePostDate",
        KeyConditionExpression=Key("Post_Element_Type").eq(post_element_type) 
            & Key("Featured_Post_Date").begins_with("1"),
        ScanIndexForward=False,
        Limit=limit
    )

    #the below code retrieves the Post_Ids from the response list of dictionary items
    post_ids = [item["Post_Id"] for item in response["Items"]]
    
    return post_ids