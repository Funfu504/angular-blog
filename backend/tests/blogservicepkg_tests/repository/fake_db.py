from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.repository.dbmapper import PostDBMapper
import logging

logger = logging.getLogger(__name__)

class RepositoryFake:

    def get_post(self, post_id: str) -> BlogPost :
        
        post = None

        if (post_id == "POST#001"):
            post = BlogPost(postId="POST#001")
            post.addMetadata(title="My First Blog Post", summary="Introductory Post")
            post.addImage(fileName="FeelsTheCat.jpg", imageUrl="/users/Moe/FeelsTheCat.jpg", altText="Feels The Cat")
            post.addContent(content="Wall of text")
            post.addPostDate(postDate="1/29/2026")
            post.addFeaturedFlag(featured="0")

        if (post_id == "POST#002"):
            post = BlogPost(postId="POST#002")
            post.addMetadata(title="My Python Journey", summary="My Python Experience")
            post.addImage(fileName="PythonLogo.png", imageUrl="/users/Moe/PythonLogo.png", altText="Official Python Logo")
            post.addContent(content="Wall of text")
            post.addPostDate(postDate="2/1/2026")
            post.addFeaturedFlag(featured="1")

        if (post_id == "POST#003"):
            post = BlogPost(postId="POST#003")
            post.addMetadata(title="My Python Journey", summary="My Python Experience")
            post.addImage(fileName="PythonLogo.png", imageUrl="/users/Moe/PythonLogo.png", altText="Official Python Logo")
            post.addImage(fileName="PythonLogo.png", imageUrl="/users/Moe/PythonLogo.png", altText="Official Python Logo")
            post.addContent(content="Wall of text")
            post.addPostDate(postDate="2/1/2026")
            post.addFeaturedFlag(featured="1")

        return post
    
    def get_posts(self, post_element_type: str, limit: int) -> list[str] :

        postIds = []
        postIds.append("POST#001")
        return postIds
    
    def get_featured_posts(self, post_element_type: str, limit: int) -> list[str] :

        postIds = []
        postIds.append("POST#002")
        return postIds
        