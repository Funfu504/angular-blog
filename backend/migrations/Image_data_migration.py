# I need to merge the Image and Metadata records in order to resolve a performance issue
# discovered during test.  Page load is taking 3 seconds due to a fan-out issue introduced
# by a change in access pattern.  This script is going to leverage the service layer to
# facilitate the data migration.

from blogservicepkg.service.services import PostService
from blogservicepkg.repository.db import Repository
from core.logging import setup_logging

import logging

setup_logging()

repo = Repository()
postSvc = PostService(repo)

logger = logging.getLogger(__name__)

def execute_migration(num_posts: int) -> bool: 
    try:        
        thePosts = postSvc.readBlogPosts(int(num_posts))

        for post in thePosts:
            postSvc.createPost(post)

        return True

    except Exception as e:
        logger.exception(f"Error reading item: {repr(e)}")
        return False