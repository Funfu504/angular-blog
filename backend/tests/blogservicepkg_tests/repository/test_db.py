from blogservicepkg.repository.db import get_post_table, get_post, get_posts, get_featured_posts
from blogservicepkg.repository.dbmapper import PostDBMapper

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
    domainEntity = PostDBMapper.build_post_entity(postList)
    assert domainEntity.postId == "POST#001"
    assert domainEntity.postDate == "1/29/2026"
    assert domainEntity.featured == "0"
    assert domainEntity.content.blogtext == "Wall of text"

#test transform of Domain entity to DB records (UPDATES).
def test_build_DynamoDB_Records():
    postList = get_post("POST#001")
    domainEntity = PostDBMapper.build_post_entity(postList)
    dbList = PostDBMapper.build_dynamoDb_entries(domainEntity)

    assert len(dbList) == 3
    assert dbList[0]["Post_Element_Type"] == "METADATA"
    assert dbList[1]["Post_Element_Type"] == "CONTENT"
    assert dbList[2]["Post_Element_Type"] == "IMAGE"

#test transform of Domain entity to DB records (CREATES).
def test_build_DynamoDB_Records():
    postList = get_post("POST#001")
    postList[0]["postId"] = None
    domainEntity = PostDBMapper.build_post_entity(postList)
    dbList = PostDBMapper.build_dynamoDb_entries(domainEntity)

    assert len(dbList) == 3
    assert dbList[0]["Post_Element_Type"] == "METADATA"
    assert dbList[1]["Post_Element_Type"] == "CONTENT"
    assert dbList[2]["Post_Element_Type"] == "IMAGE"