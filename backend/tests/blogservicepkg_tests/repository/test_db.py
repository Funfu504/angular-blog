from blogservicepkg.repository.db import Repository
from blogservicepkg.repository.dbmapper import PostDBMapper

dbmapper = PostDBMapper()
repo = Repository(dbmapper)

# these tests are overly generous in their asserts because they are testing
#  connectivity to the datastore, DynamoDB (DDB), not business logic.

# ensures the LOCAL database table has content in it.
def test_table_has_data():
    table = repo.get_post_table()
    assert table.item_count > 0

# test Post retrieval from of one dummy record inserted when LOCAL DDB is created.
def test_table_has_post001():
    response = repo.get_post("POST#001")
    assert response.postId == "POST#001"

# test Post retrieval from DB. Should always return results since the LOCAL database
#will always be created with content in it.
def test_gsi_get_multiple_posts():
    response = repo.get_posts("METADATA", 2)
    assert len(response) > 0

# test Post retrieval from DB. Should always return results since the LOCAL database
#will always be created with one featured post in it.
def test_gsi_get_featured_post_ids():
    response = repo.get_featured_posts("METADATA", 2)
    assert len(response) > 0    