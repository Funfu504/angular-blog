from blogservicepkg.service.services import PostService
from blogservicepkg_tests.repository.fake_db import RepositoryFake

fakeRepo = RepositoryFake()
postSvc = PostService(fakeRepo)

#test transform of post from DB records to UI post.
def test_readBlogPost():
    result = postSvc.readPost("POST#001")
    assert result.postId == "POST#001"
    assert result.content.blogtext == "Wall of text"
    assert result.postDate == "1/29/2026"
    assert result.featured == "0"

def test_readFeaturedBlogPosts():
    result = postSvc.readFeaturedPosts(2)
    assert len(result) == 1
    


    