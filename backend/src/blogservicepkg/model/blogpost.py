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

    fileName = None
    imageUrl = None
    altText = None    

    def __init__(self, fileName : str, imageUrl : str, altText : str):
        self.fileName = fileName
        self.imageUrl = imageUrl
        self.altText = altText

    def isValid(self):
        return (
            self.fileName and self.fileName.strip()
            and self.imageUrl and self.imageUrl.strip()
        )

    def __eq__(self, other):
        if not isinstance(other, Image):
            return NotImplemented

        return (
            self.fileName == other.fileName
            and self.imageUrl == other.imageUrl
            and self.altText == other.altText
        )

    def __str__(self):
        return f"{self.imageUrl} is an image of {self.altText}.  It's name is {self.fileName}."

class BlogPost:

    postId = None    
    metadata = None
    content = None    
    images: list[Image] = None
    postDate = None
    featured = None

    def __init__(self, postId : str,):
        self.postId = postId
        self.images = []
        
    def addPostDate(self, postDate : str):
        self.postDate = postDate

    def addFeaturedFlag(self, featured : str):
        self.featured = featured

    def addMetadata(self, title: str, summary: str):
        self.metadata = Metadata(title, summary)

    def addContent(self, content: str):
        self.content = Content(content)

    def addImage(self, fileName: str, imageUrl: str, altText: str):
        newImage = Image(fileName, imageUrl, altText)

        if (newImage.isValid() and newImage not in self.images):
            self.images.append(newImage)

    def getImage(self, index) -> Image | None:

        try:
            return self.images[index]
        except:
            return None
    


    
