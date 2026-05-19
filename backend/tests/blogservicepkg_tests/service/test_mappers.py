from blogservicepkg.service.services import readBlogPost
from blogservicepkg.service.apimapper import PostAPIMapper
from blogservicepkg.model.post import SavePostRequest
from blogservicepkg.model.blogpost import BlogPost

def test_build_post_response():
    result = readBlogPost("POST#001")
    mapping = PostAPIMapper.build_post_response(result)
    assert mapping["postId"] == "POST#001"
    assert mapping["blogText"] == "Wall of text"
    assert mapping["postDate"] == "1/29/2026"
    assert mapping["featured"] == False

def test_build_post_save():
    post = SavePostRequest(postId= "123", title = "my title", summary = "summary", blogText = "Wall of Text", 
                           imageAltText= "Alt Text", imageUrl="url", postDate="1/29/2026", featured=False)
    assert post.postId == "123"
    assert post.title == "my title"
    assert post.summary == "summary"
    assert post.blogText == "Wall of Text"
    assert post.imageAltText == "Alt Text"
    assert post.imageUrl == "url"
    assert post.postDate == "1/29/2026"
    assert post.featured == False

    
    
    
