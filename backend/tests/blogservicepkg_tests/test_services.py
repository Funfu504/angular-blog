from blogservicepkg.services import get_post, build_post_response, deconstruct_post, get_featured_posts, get_posts

#test Post retrieval from DB.
def test_table_has_data():
    response = get_post("POST#001")
    assert len(response) == 3

#test Post retrieval from DB.
def test_gsi_get_multiple_posts():
    response = get_posts("METADATA", 2)
    assert len(response) == 2

#test Post retrieval from DB.
def test_gsi_get_featured_post_ids():
    response = get_featured_posts("METADATA", 2)
    assert len(response) == 1
    assert response[0] == "POST#002"

#test transform of post from DB records to UI post.
def test_build_response():
    postList = get_post("POST#001")
    response = build_post_response(postList)
    assert response["postId"] == "POST#001"
    assert response["content"] == "Wall of text"
    assert response["postDate"] == "1/29/2026"
    assert response["featured"] == "0"

#test transform of UI post to DB records
def test_deconstruct_post():
    postList = get_post("POST#001")
    thePost = build_post_response(postList)
    response = deconstruct_post(thePost)
    assert len(response) == 3
    


    