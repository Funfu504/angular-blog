from blogservicepkg.service.services import readFeaturedBlogPosts, readBlogPost, readAllBlogPosts
from blogservicepkg.model.blogpost import BlogPost

#function to convert the fragmented database records associated to a blog post into a single JSON response.
def build_post_response(item : BlogPost) -> dict:
    if not item:
        return None

    post = {
        "postId": item.postId,
        "title": item.metadata.title,
        "summary": item.metadata.summary,
        "blogText": item.content.blogtext,
        "imageUrl": item.images[0].imageUrl,
        "imageAltText": item.images[0].altText,
        "postDate": item.postDate,
        "featured": item.featured
    }

    return post

#retrieves a single post tied to a Post Id.
def readPost(postId : str) -> dict :
    theBlogPost = readBlogPost(postId)
    thePost = build_post_response(theBlogPost)
    return thePost

#retrieves a defined number of featured posts.
def readFeaturedPosts(numPosts : int) -> list[dict] :
    listBlogPosts = readFeaturedBlogPosts(numPosts)
    listPosts : list[dict] = []
    for blogPost in listBlogPosts:
        listPosts.append(build_post_response(blogPost))

    return listPosts

#retrieves a defined number of featured posts.
def readBlogPosts(numPosts : int) -> list[dict] :
    listBlogPosts = readAllBlogPosts(numPosts)
    listPosts : list[dict] = []
    for blogPost in listBlogPosts:
        listPosts.append(build_post_response(blogPost))

    return listPosts
    