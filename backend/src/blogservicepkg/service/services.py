from blogservicepkg.repository.db import get_post, get_posts, get_featured_posts, put_post
from blogservicepkg.repository.dbmapper import PostDBMapper
from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.service.apimapper import PostAPIMapper
from blogservicepkg.model.post import CreatePostRequest, UploadRequest, UploadResponse
import logging
import time

logger = logging.getLogger(__name__)

#retrieves a single post tied to a Post Id.
def readPost(postId : str) -> dict :        
    thePost = get_post(postId)    
    theBlogPost = PostDBMapper.build_post_entity(thePost)
    thePost = PostAPIMapper.build_post_response(theBlogPost)    
    return thePost

#retrieves a defined number of featured posts.
def readFeaturedPosts(numPosts : int) -> list[dict] :    
    listBlogPosts = []    
    postIdList = get_featured_posts("METADATA", numPosts)    
    for postId in postIdList :        
        listBlogPosts.append(readPost(postId))    
    return listBlogPosts

#retrieves a defined number of featured posts.
def readBlogPosts(numPosts : int) -> list[dict] :    
    logger.info(f"Fetching {numPosts} posts")
    listBlogPosts = []
    start = time.perf_counter()
    postIdList = get_posts("METADATA", numPosts)    
    for postId in postIdList :        
        listBlogPosts.append(readPost(postId))
    logger.info(
    f"Fetching {numPosts} Posts response took {(time.perf_counter()-start)*1000:.0f} ms")
    return listBlogPosts


def createPost(post : CreatePostRequest):
    logger.info("Saving new post tited: %s", post.title)
    logger.info("Saving new post img filename %s", post.imageFileName)
    logger.info("Saving new post img alt text %s", post.imageAltText)
    logger.info("Saving new post img url: %s", post.imageUrl)
    theBlogPost = PostAPIMapper.build_post_create(post)
    logger.info("image url: %s", theBlogPost.images[0].imageUrl)
    theDBRecordList = PostDBMapper.build_dynamoDb_entries(theBlogPost)    
    put_post(theDBRecordList)