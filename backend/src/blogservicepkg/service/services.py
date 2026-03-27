from blogservicepkg.repository.db import getBlogPost, getBlogPosts, getFeaturedBlogPosts
from blogservicepkg.model.blogpost import BlogPost

def readBlogPost(post_id: str) -> BlogPost:
    return getBlogPost(post_id)

def readFeaturedBlogPosts(numPosts: int) -> list[BlogPost]:
    return getFeaturedBlogPosts(numPosts)

def readAllBlogPosts(numPosts: int) -> list[BlogPost]:
    return getBlogPosts(numPosts)

#needs to be rewritten as it's skipping the Domain entity.
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