from blogservicepkg.repository.db import Repository
from blogservicepkg.model.blogpost import BlogPost
import logging
import time

logger = logging.getLogger(__name__)

class PostService:

    repo: Repository = None

    def __init__(self, repo: Repository):
        self.repo = repo

    #retrieves a single post tied to a Post Id.
    def readPost(self, postId : str) -> BlogPost :        
        theBlogPost = self.repo.get_post(postId)
        return theBlogPost

    #retrieves a defined number of featured posts.
    def readFeaturedPosts(self, numPosts : int) -> list[BlogPost] :    
        listBlogPosts = []    
        postIdList = self.repo.get_featured_posts("METADATA", numPosts)    
        for postId in postIdList :        
            listBlogPosts.append(self.readPost(postId))    
        return listBlogPosts

    #retrieves a defined number of featured posts.
    def readBlogPosts(self, numPosts : int) -> list[BlogPost] :    
        logger.info(f"Fetching {numPosts} posts")
        listBlogPosts = []
        start = time.perf_counter()
        postIdList = self.repo.get_posts("METADATA", numPosts)    
        for postId in postIdList :        
            listBlogPosts.append(self.readPost(postId))
        logger.info(
        f"Fetching {numPosts} Posts response took {(time.perf_counter()-start)*1000:.0f} ms")
        return listBlogPosts


    def createPost(self, post : BlogPost):
        logger.info("Saving new post tited: %s", post.metadata.title)
        logger.info("Saving new post img filename %s", post.images[0].fileName)
        logger.info("Saving new post img alt text %s", post.images[0].altText)
        logger.info("Saving new post img url: %s", post.images[0].imageUrl)       
        self.repo.put_post(post)