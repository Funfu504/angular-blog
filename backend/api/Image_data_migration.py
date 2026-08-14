# I need to merge the Image and Metadata records in order to resolve a performance issue
# discovered during test.  Page load is taking 3 seconds due to a fan-out issue introduced
# by a change in access pattern.  This script is going to leverage the service layer to
# facilitate the data migration.

from blogservicepkg.service.services import PostService
from blogservicepkg.repository.db import Repository
from blogservicepkg.repository.dbMigrationMapper import PostDBMigrationMapper
from core.logging import setup_logging
import logging

setup_logging()

dbmapper = PostDBMigrationMapper()
repo = Repository(dbmapper)
postSvc = PostService(repo)

logger = logging.getLogger(__name__)

#entry point for lambda function.
def handler(event, context):
    try:
        logger.info("Starting Migration")

        num_posts = 0

        if "num_posts" in event:
            num_posts = event["num_posts"]
            result = execute_migration(num_posts)

        logger.info("Migration Complete")

        return result

    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return False            

def execute_migration(num_posts: int) -> bool: 
    try:        
        thePosts = postSvc.readBlogPosts(int(num_posts))

        for post in thePosts:
            logger.info("migrating post_id: %s", post.postId)
            postSvc.createPost(post)

        return True

    except Exception as e:
        logger.exception(f"Error executing migration: {repr(e)}")
        return False

#local run entry point
if __name__ == "__main__":
    execute_migration(2)