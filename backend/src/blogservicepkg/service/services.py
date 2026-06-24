from blogservicepkg.repository.db import get_post, get_posts, get_featured_posts, put_post
from blogservicepkg.repository.dbmapper import PostDBMapper
from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.service.apimapper import PostAPIMapper
from blogservicepkg.model.post import CreatePostRequest, UploadRequest, UploadResponse
import logging
import time

logger = logging.getLogger(__name__)

#retrieves a single post tied to a Post Id.
def readPost(postId : str) -> BlogPost :        
    theBlogPost = get_post(postId)
    return theBlogPost

#retrieves a defined number of featured posts.
def readFeaturedPosts(numPosts : int) -> list[BlogPost] :    
    listBlogPosts = []    
    postIdList = get_featured_posts("METADATA", numPosts)    
    for postId in postIdList :        
        listBlogPosts.append(readPost(postId))    
    return listBlogPosts

#retrieves a defined number of featured posts.
def readBlogPosts(numPosts : int) -> list[BlogPost] :    
    logger.info(f"Fetching {numPosts} posts")
    listBlogPosts = []
    start = time.perf_counter()
    postIdList = get_posts("METADATA", numPosts)    
    for postId in postIdList :        
        listBlogPosts.append(readPost(postId))
    logger.info(
    f"Fetching {numPosts} Posts response took {(time.perf_counter()-start)*1000:.0f} ms")
    return listBlogPosts


def createPost(post : BlogPost):
    logger.info("Saving new post tited: %s", post.metadata.title)
    logger.info("Saving new post img filename %s", post.images[0].fileName)
    logger.info("Saving new post img alt text %s", post.images[0].altText)
    logger.info("Saving new post img url: %s", post.images[0].imageUrl)       
    put_post(post)