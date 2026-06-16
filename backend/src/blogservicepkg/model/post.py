from pydantic import BaseModel, ConfigDict, field_validator

#BaseModel allows for the entity to be hydrated from the JSON request automatically via 1-1 mapping.
class CreatePostRequest(BaseModel):

    #Trim attributes.  Reject request if it has extra attributes.
    model_config = ConfigDict(
        extra='forbid',
        str_strip_whitespace=True
    )

    title: str
    summary: str
    blogText: str
    imageFileName: str
    imageUrl: str
    imageAltText: str
    postDate: str
    featured: bool = False
    authorId: str | None = None

class SavePostRequest(BaseModel):

    #Trim attributes.  Reject request if it has extra attributes.
    model_config = ConfigDict(
        extra='forbid',
        str_strip_whitespace=True
    )

    postId: str
    title: str
    summary: str
    blogText: str
    imageFileName: str
    imageUrl: str
    imageAltText: str
    postDate: str
    featured: bool = False
    authorId: str | None = None

#BaseModel allows for the entity to be output as json via "model_dump()"
class GetPostResponse(BaseModel):
    postId: str
    title: str
    summary: str
    blogText: str
    imageUrl: str
    imageAltText: str
    postDate: str
    featured: bool = False
   
class UploadRequest(BaseModel):
    
    model_config = ConfigDict(
        extra='forbid',
        str_strip_whitespace=True
    )

    userId: str
    filename: str
    contentType: str

    @field_validator('contentType')
    @classmethod
    def contenttype_must_be_valid(cls, value: str) -> str:
        if value not in {"image/jpeg","image/png","image/gif"}:
            raise ValueError(f'content type {value} is invalid')
        return value

class UploadResponse(BaseModel):
    uploadUrl: str
    fileKey: str
    fileName: str



