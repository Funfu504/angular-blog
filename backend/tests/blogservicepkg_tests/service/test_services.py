from blogservicepkg.service.services import deconstruct_post, readBlogPost, readFeaturedBlogPosts

#test transform of post from DB records to UI post.
def test_readBlogPost():
    result = readBlogPost("POST#001")
    assert result.postId == "POST#001"
    assert result.content.blogtext == "Wall of text"
    assert result.postDate == "1/29/2026"
    assert result.featured == "0"

def test_readFeaturedBlogPosts():
    result = readFeaturedBlogPosts(2)
    assert len(result) == 1

#test transform of UI post to DB records
#def test_deconstruct_post():
#    postList = get_post("POST#001")
#    thePost = build_post_response(postList)
#    response = deconstruct_post(thePost)
#    assert len(response) == 3
    


    