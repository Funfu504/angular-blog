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
        "postDate": items[0]["Post_Date"]
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
def get_post(post_id):
    table = get_post_table()
    response = table.query(
        KeyConditionExpression=Key("Post_Id").eq(post_id))
    items = response["Items"]
    return items

def put_post(post: dict) -> list[dict]:
    items = [{}]

    if "postId" in post:
        print("post id is there")

    if "postDate" in post:
        print("post date is there")

    if "meta" in post:
        print("meta is there")
    
    if "content" in post:
        print("content is there")
    
    if "images" in post:
        print("images are there")

    return items