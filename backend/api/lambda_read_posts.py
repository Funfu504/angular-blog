from blogservicepkg.service.handlers import readPost, readFeaturedPosts, readBlogPosts
import json

def handler(event, context):
    
    result = readBlogPosts(event["num_posts"])
    
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }