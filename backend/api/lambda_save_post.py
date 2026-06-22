from blogservicepkg.service.handlers import createPost, generateS3UploadUrl
from blogservicepkg.model.post import CreatePostRequest, UploadRequest, UploadResponse
from core.transport.request import parse_event_model, logRequest
from core.transport.response import success_response, failure_response
from pydantic import ValidationError
from core.logging import setup_logging
import logging
import json

setup_logging()

logger = logging.getLogger(__name__)

def processPostRequest(event):
    request = parse_event_model(event, CreatePostRequest)
    createPost(request)
    return success_response(request.model_dump())

def processUploadRequest(event):
    request = parse_event_model(event, UploadRequest)
    
    logger.info("generate S3 url for %s", request.filename)    
    response = generateS3UploadUrl(request)
    logger.info("generated S3 url: %s", response.uploadUrl)
    return success_response(response.model_dump())

def handler(event, context):
    try:
        logRequest(event)
        route = event["routeKey"]

        if (route == "POST /post"):
            return processPostRequest(event)
        
        if (route == "POST /assets/upload-url"):
            return processUploadRequest(event)
        
    except ValidationError as ex:
        logger.error(f"A validation exception occured during save: {ex.json()}")
        return failure_response({"message": "Validation Error"}, 400)
    except Exception as e:
        logger.exception(str(e))
        return failure_response({"message": "Internal Server Error"}, 500)        
    
