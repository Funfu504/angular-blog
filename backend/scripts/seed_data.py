import boto3

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-east-1"
)

table = dynamodb.Table("Blog_Post")

posts = [
    {"Post_Id": "POST#001", "Post_Element_Type": "IMAGE", "Post_Date": "1/29/2026", "Value": "{ \"url\": \"/assets/images/FeelsTheCat.jpg\", \"alttext\": \"Feels The Cat\" }"},
    {"Post_Id": "POST#001", "Post_Element_Type": "CONTENT", "Post_Date": "1/29/2026", "Value": "{ \"blogtext\": \"Wall of text\" }"},
    {"Post_Id": "POST#002", "Post_Element_Type": "IMAGE", "Post_Date": "2/1/2026", "Value": "{ \"url\": \"/assets/images/PythonLogo.png\", \"alttext\": \"Official Python Logo\" }"},
    {"Post_Id": "POST#002", "Post_Element_Type": "CONTENT", "Post_Date": "2/1/2026", "Value": "{ \"blogtext\": \"Wall of text\" }"},
]

for post in posts:
    table.put_item(Item=post)

print("Seed complete.")