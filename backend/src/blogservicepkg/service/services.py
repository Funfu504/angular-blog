from blogservicepkg.repository.db import getBlogPost, getBlogPosts, getFeaturedBlogPosts, putBlogPost
from blogservicepkg.model.blogpost import BlogPost

def readBlogPost(post_id: str) -> BlogPost:
    return getBlogPost(post_id)

def readFeaturedBlogPosts(numPosts: int) -> list[BlogPost]:
    return getFeaturedBlogPosts(numPosts)

def readAllBlogPosts(numPosts: int) -> list[BlogPost]:
    return getBlogPosts(numPosts)

def createBlogPost(post: BlogPost):
    putBlogPost(post)