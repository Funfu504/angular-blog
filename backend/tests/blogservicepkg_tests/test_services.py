from blogservicepkg.services import get_post, build_post_response

def test_table_has_data():
    response = get_post("POST#001")
    assert len(response) == 2

def test_build_response():
    postList = get_post("POST#001")
    response = build_post_response(postList)
    assert response["postId"] == "POST#001"
    assert response["content"] == "Wall of text"

    