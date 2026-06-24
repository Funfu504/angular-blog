from blogservicepkg.service.services import readBlogPosts
from core.logging import setup_logging
from core.transport.request import parse_event_model, logRequest
from core.transport.response import success_response, failure_response
from blogservicepkg.service.apimapper import PostAPIMapper
import logging

setup_logging()

logger = logging.getLogger(__name__)

def handler(event, context):
    try:
        logRequest(event)
        # Check query string first (API Gateway)
        qs = event.get("queryStringParameters", {})
        num_posts = qs.get("num_posts")

        # Fall back to direct Lambda invocation payload
        if num_posts is None and "num_posts" in event:
            num_posts = event["num_posts"]

        thePosts = readBlogPosts(int(num_posts))

        result = []

        for post in thePosts:
            result.append(PostAPIMapper.build_post_response(post))        

        return success_response(result)

    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return failure_response({"error": str(e)}, 500)
