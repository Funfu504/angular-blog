from blogservicepkg.service.services import PostService
from blogservicepkg.repository.db import Repository
from blogservicepkg.repository.dbmapper import PostDBMapper
from blogservicepkg.service.uploads import AssetService
from blogservicepkg.model.post import CreatePostRequest, UploadRequest, UploadResponse
from blogservicepkg.service.apimapper import PostAPIMapper
from core.transport.api_request import parse_event_model, logRequest
from core.transport.api_response import success_response, failure_response
from pydantic import ValidationError
from core.logging import setup_logging
import logging

setup_logging()

dbmapper = PostDBMapper()
repo = Repository(dbmapper)
postSvc = PostService(repo)
assetSvc = AssetService()

logger = logging.getLogger(__name__)

def processPostRequest(event):
    request = parse_event_model(event, CreatePostRequest)
    blogPost = PostAPIMapper.build_post_create(request)
    postSvc.createPost(blogPost)
    return success_response(request.model_dump())

def processUploadRequest(event):
    request = parse_event_model(event, UploadRequest)
    
    logger.info("generate S3 url for %s", request.filename)    
    response = assetSvc.generateS3UploadUrl(request)
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
    
