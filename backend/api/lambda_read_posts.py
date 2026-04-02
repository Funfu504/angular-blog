from blogservicepkg.service.handlers import readPost, readFeaturedPosts, readBlogPosts
import json

def handler(event, context):
    try:
        
        # Check query string first (API Gateway)
        qs = event.get("queryStringParameters", {})
        num_posts = qs.get("num_posts")

        # Fall back to direct Lambda invocation payload
        if num_posts is None and "num_posts" in event:
            num_posts = event["num_posts"]

        result = readBlogPosts(int(num_posts))
    
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
