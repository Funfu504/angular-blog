#FastAPI endpoint
from fastapi import FastAPI
from blogservicepkg.service.handlers import readPost, readFeaturedPosts, readBlogPosts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#added to fix issue where UI and Service couldn't communicate because it appeared to be
#running on 2 different domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # allow your Angular app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def read_posts(
        num_posts: int | None = 0,
        featured: bool | None = False
    ):

    if featured == True:
        response = readFeaturedPosts(num_posts)
    else:
        response = readBlogPosts(num_posts)

    return response

@app.get("/posts/{post_id}")
def read_post(post_id: str | None = None):
    return readPost(post_id)