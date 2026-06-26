from blogservicepkg.repository.dbmapper import PostDBMapper

def get_post_test_data(post_id: str):

    post = None

    if (post_id == "POST#001"):
        post = [
            {"Post_Id": "POST#001", "Post_Element_Type": "METADATA", "Post_Date": "1/29/2026", "Featured_Post_Date": "0#1/29/2026", "Value": "{ \"title\": \"My First Blog Post\", \"summary\": \"Introductory Post\" }"},
            {"Post_Id": "POST#001", "Post_Element_Type": "IMAGE", "Value": "{ \"url\": \"/users/Moe/FeelsTheCat.jpg\", \"alttext\": \"Feels The Cat\", \"filename\": \"FeelsTheCat.jpg\" }"},
            {"Post_Id": "POST#001", "Post_Element_Type": "CONTENT", "Value": "{ \"blogtext\": \"Wall of text\" }"},
        ]

    if (post_id == "POST#002"):
        post = [
            {"Post_Id": "POST#002", "Post_Element_Type": "METADATA", "Post_Date": "2/1/2026", "Featured_Post_Date": "1#2/1/2026", "Value": "{ \"title\": \"My Python Journey\", \"summary\": \"My Python Experience\" }"},
            {"Post_Id": "POST#002", "Post_Element_Type": "IMAGE", "Value": "{ \"url\": \"/users/Moe/PythonLogo.png\", \"alttext\": \"Official Python Logo\", \"filename\": \"PythonLogo.png\" }"},
            {"Post_Id": "POST#002", "Post_Element_Type": "CONTENT", "Value": "{ \"blogtext\": \"Wall of text\" }"},
        ]

    return post

# test transform of post from DB records to UI post.
def test_build_BlogPost_Entity():
    postList = get_post_test_data("POST#001")
    domainEntity = PostDBMapper.build_post_entity(postList)
    assert domainEntity.postId == "POST#001"
    assert domainEntity.postDate == "1/29/2026"
    assert domainEntity.featured == "0"
    assert domainEntity.content.blogtext == "Wall of text"

# test transform of Domain entity to DB records (UPDATES).
def test_build_DynamoDB_Records():
    postList = get_post_test_data("POST#001")
    domainEntity = PostDBMapper.build_post_entity(postList)
    dbList = PostDBMapper.build_dynamoDb_entries(domainEntity)

    assert len(dbList) == 3
    assert dbList[0]["Post_Element_Type"] == "METADATA"
    assert dbList[1]["Post_Element_Type"] == "CONTENT"
    assert dbList[2]["Post_Element_Type"] == "IMAGE"

# test transform of Domain entity to DB records (CREATES).
def test_build_DynamoDB_Records():
    postList = get_post_test_data("POST#001")
    postList[0]["postId"] = None
    domainEntity = PostDBMapper.build_post_entity(postList)
    dbList = PostDBMapper.build_dynamoDb_entries(domainEntity)

    assert len(dbList) == 3
    assert dbList[0]["Post_Element_Type"] == "METADATA"
    assert dbList[1]["Post_Element_Type"] == "CONTENT"
    assert dbList[2]["Post_Element_Type"] == "IMAGE"