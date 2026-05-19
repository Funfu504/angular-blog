from blogservicepkg.service.handlers import readPost, readFeaturedPosts, readBlogPosts
import json
from core.logging import setup_logging
from core.transport.response import success_response, failure_response
import logging

setup_logging()

logger = logging.getLogger(__name__)

def handler(event, context):
    try:
        
        # Check query string first (API Gateway)
        qs = event.get("queryStringParameters", {})
        num_posts = qs.get("num_posts")

        # Fall back to direct Lambda invocation payload
        if num_posts is None and "num_posts" in event:
            num_posts = event["num_posts"]

        result = readBlogPosts(int(num_posts))
        return success_response(result)

    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return failure_response({"error": str(e)}, 500)
