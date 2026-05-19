#FastAPI endpoint
from fastapi import FastAPI
from blogservicepkg.service.handlers import readPost, readFeaturedPosts, readBlogPosts, createPost, generateS3UploadUrl
from blogservicepkg.model.post import CreatePostRequest, UploadRequest
from core.transport.response import success_response, failure_response
from fastapi.middleware.cors import CORSMiddleware
from core.logging import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

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
        response = readFeaturedPosts(num_posts)
    else:
        response = readBlogPosts(num_posts)

    return response

@app.get("/posts/{post_id}")
def read_post(post_id: str | None = None):
    return readPost(post_id)

@app.post("/post")
def save_post(request: CreatePostRequest):
    try:        
        createPost(request)
        return success_response(request.model_dump())    
    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return failure_response({"exception": str(e)}, 500)

@app.post("/assets/upload-url")
def generate_S3_upload_url(request: UploadRequest):
    try:
        response = generateS3UploadUrl(request)
        success_response(response.model_dump())
    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return failure_response({"exception": str(e)}, 500)    