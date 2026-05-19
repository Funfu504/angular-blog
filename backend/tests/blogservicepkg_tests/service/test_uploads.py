from blogservicepkg.model.post import UploadRequest
from blogservicepkg.service.uploads import GenerateS3UploadURL

def test_GenerateS3UploadURL():
    item = UploadRequest(userId="TestUser", filename="StrangerThingsLogo.png", contentType="image/png")
    result = GenerateS3UploadURL(item)
    assert len(result) > 0
