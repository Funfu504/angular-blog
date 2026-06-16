from blogservicepkg.service.services import readFeaturedBlogPosts, readBlogPost, readAllBlogPosts, createBlogPost
from blogservicepkg.service.apimapper import PostAPIMapper
from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.model.post import CreatePostRequest, UploadRequest, UploadResponse
from blogservicepkg.service.uploads import GenerateS3UploadURL
import logging

logger = logging.getLogger(__name__)

#retrieves a single post tied to a Post Id.
def readPost(postId : str) -> dict :
    theBlogPost = readBlogPost(postId)
    thePost = PostAPIMapper.build_post_response(theBlogPost)
    return thePost

#retrieves a defined number of featured posts.
def readFeaturedPosts(numPosts : int) -> list[dict] :
    listBlogPosts = readFeaturedBlogPosts(numPosts)
    listPosts : list[dict] = []
    for blogPost in listBlogPosts:
        listPosts.append(PostAPIMapper.build_post_response(blogPost))

    return listPosts

#retrieves a defined number of featured posts.
def readBlogPosts(numPosts : int) -> list[dict] :
    logger.info(f"Fetching {numPosts} posts")
    listBlogPosts = readAllBlogPosts(numPosts)
    listPosts : list[dict] = []
    for blogPost in listBlogPosts:
        listPosts.append(PostAPIMapper.build_post_response(blogPost))

    return listPosts

def createPost(post : CreatePostRequest):
    logger.info("Saving new post tited: %s", post.title)
    logger.info("Saving new post img filename %s", post.imageFileName)
    logger.info("Saving new post img alt text %s", post.imageAltText)
    logger.info("Saving new post img url: %s", post.imageUrl)
    createBlogPost(PostAPIMapper.build_post_create(post))
    
def generateS3UploadUrl(item: UploadRequest) -> UploadResponse:
    return GenerateS3UploadURL(item) 
    
    
