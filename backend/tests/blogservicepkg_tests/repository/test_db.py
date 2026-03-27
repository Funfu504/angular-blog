from blogservicepkg.repository.db import get_post_table, get_post, get_posts, get_featured_posts, build_post_entity

def test_table_has_data():
    table = get_post_table()
    assert table.item_count == 6

#test Post retrieval from DB.
def test_table_has_post001():
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
def test_build_BlogPost_Entity():
    postList = get_post("POST#001")
    domainEntity = build_post_entity(postList)
    assert domainEntity.postId == "POST#001"
    assert domainEntity.postDate == "1/29/2026"
    assert domainEntity.featured == "0"
    assert domainEntity.content.blogtext == "Wall of text"