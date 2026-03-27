class Metadata:

    title = None
    summary = None

    def __init__(self, title : str, summary : str):
        self.title = title
        self.summary = summary

    def updateSummary(self, newSummary : str):
        self.summary = newSummary

    def __str__(self):
        return f"The blog post {self.title}, in summarization is about {self.summary}"

class Content:

    blogtext = None

    def __init__(self, blogtext : str):
        self.blogtext = blogtext  # Instance attribute

    def __str__(self):
        return f"{self.blogtext}"

class Image:

    imageUrl = None
    altText = None

    def __init__(self, imageUrl : str, altText : str):
        self.imageUrl = imageUrl
        self.altText = altText

    def updateImageUrl(self, imageUrl : str):
        self.imageUrl = imageUrl        

    def __str__(self):
        return f"{self.imageUrl} is an image of {self.altText}"

class BlogPost:

    postId = None    
    metadata = None
    content = None    
    images: list[Image] = []
    postDate = None
    featured = None

    def __init__(self, postId : str):
        self.postId = postId
        
    def addPostDate(self, postDate : str):
        self.postDate = postDate

    def addFeaturedFlag(self, featured : str):
        self.featured = featured

    def addMetadata(self, title: str, summary: str):
        self.metadata = Metadata(title, summary)

    def addContent(self, content: str):
        self.content = Content(content)

    def addImage(self, imageUrl: str, altText: str):
        self.images.append(Image(imageUrl, altText))
    
