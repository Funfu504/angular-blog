from blogservicepkg.model.blogpost import BlogPost
from blogservicepkg.model.post import GetPostResponse, CreatePostRequest, SavePostRequest

class PostAPIMapper:

    @staticmethod
    #function to convert the fragmented database records associated to a blog post into a single JSON response.
    def build_post_response(item : BlogPost) -> dict:
        if not item:
            return None
        
        post = GetPostResponse(postId = item.postId, title = item.metadata.title, summary = item.metadata.summary,
                               blogText = item.content.blogtext, imageUrl = item.images[0].imageUrl, 
                               imageAltText = item.images[0].altText, postDate = item.postDate, featured = item.featured)

        return post.model_dump()
    
    @staticmethod
    #function to convert the fragmented database records associated to a blog post into a single JSON response.
    def build_post_create(item : CreatePostRequest) -> BlogPost:
        if not item:
            return None
        
        post = BlogPost("0")
        post.addMetadata(item.title, item.summary)
        post.addContent(item.blogText)
        post.addImage(item.imageUrl, item.imageAltText)
        post.addPostDate(item.postDate)
        post.addFeaturedFlag(item.featured)

        return post
    
    @staticmethod
    #function to convert the fragmented database records associated to a blog post into a single JSON response.
    def build_post_save(item : SavePostRequest) -> BlogPost:
        if not item:
            return None
        
        post = BlogPost(item.postId)
        post.addMetadata(item.title, item.summary)
        post.addContent(item.blogText)
        post.addImage(item.imageUrl, item.imageAltText)
        post.addPostDate(item.postDate)
        post.addFeaturedFlag(item.featured)

        return post    