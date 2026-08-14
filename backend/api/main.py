#FastAPI endpoint
from fastapi import FastAPI, HTTPException
from blogservicepkg.service.services import PostService
from blogservicepkg.repository.db import Repository
from blogservicepkg.repository.dbmapper import PostDBMapper
from blogservicepkg.service.uploads import AssetService
from blogservicepkg.model.post import CreatePostRequest, UploadRequest
from core.transport.api_response import success_response, failure_response
from blogservicepkg.service.apimapper import PostAPIMapper
from fastapi.middleware.cors import CORSMiddleware
from core.logging import setup_logging
import logging
import json

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()
dbmapper = PostDBMapper()
repo = Repository(dbmapper)
postSvc = PostService(repo)
assetSvc = AssetService()

#added to fix issue where UI and Service couldn't communicate because it appeared to be
#running on 2 different domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # allow your Angular app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def read_posts(
        num_posts: int | None = 0,
        featured: bool | None = False
    ):

    if featured == True:
        thePosts = postSvc.readFeaturedPosts(num_posts)
    else:
        thePosts = postSvc.readBlogPosts(num_posts)

    response = []

    for post in thePosts:
        response.append(PostAPIMapper.build_post_response(post))

    return response

@app.get("/posts/{post_id}")
def read_post(post_id: str | None = None):        
    return PostAPIMapper.build_post_response(postSvc.readPost(post_id))

@app.post("/post")
def save_post(request: CreatePostRequest):
    try:
        blogPost = PostAPIMapper.build_post_create(request)
        postSvc.createPost(blogPost)
        return request
    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error"
        )

@app.post("/assets/upload-url")
def generate_S3_upload_url(request: UploadRequest):
    try:
        response = assetSvc.generateS3UploadUrl(request)
        return response
    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error"
        )  