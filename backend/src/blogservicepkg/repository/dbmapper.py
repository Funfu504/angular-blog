import json
from blogservicepkg.model.blogpost import BlogPost
from ulid import ULID
import logging

logger = logging.getLogger(__name__)

class PostDBMapper:

    @staticmethod
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
                post.addImage(value_element.get("filename"), value_element.get("url"), value_element.get("alttext"))

        logger.info("Number of Images: %s", len(post.images))
        logger.info("Image: %s", post.images[0].altText)

        return post

    @staticmethod
    #function to convert the BlogPost domain entity into fragmented database records associated to a blog post.
    def build_dynamoDb_entries(items: BlogPost) -> list[dict]:
        if not items:
            return None
        
        #if no postId is present at this point, it's a new post.  Generate a postId.
        if not items.postId or items.postId == "0":
            items.postId = str(ULID())
        
        featured=int(items.featured)


        metadata = {
            "Post_Id": f"POST#{items.postId}",
            "Post_Element_Type": "METADATA",
            "Post_Date": items.postDate,
            "Featured_Post_Date": f"{featured}#{items.postDate}",
            "Value": json.dumps({
                "title": items.metadata.title,
                "summary": items.metadata.summary
            })
        }

        content = {
            "Post_Id": f"POST#{items.postId}",
            "Post_Element_Type": "CONTENT",
            "Value": json.dumps({
                "blogtext": items.content.blogtext
            })
        }

        image = {
            "Post_Id": f"POST#{items.postId}",
            "Post_Element_Type": "IMAGE",
            "Value": json.dumps({
                "filename": items.images[0].fileName,
                "url": items.images[0].imageUrl,
                "alttext": items.images[0].altText
            })
        }

        return [metadata, content, image]