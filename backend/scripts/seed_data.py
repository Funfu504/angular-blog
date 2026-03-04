import boto3

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-east-1"
)

table = dynamodb.Table("Blog_Post")

posts = [
    {"Post_Id": "POST#001", "Post_Element_Type": "METADATA", "Post_Date": "1/29/2026", "Featured_Post_Date": "0#1/29/2026", "Value": "{ \"title\": \"My First Blog Post\", \"summary\": \"Introductory Post\" }"},
    {"Post_Id": "POST#001", "Post_Element_Type": "IMAGE", "Value": "{ \"url\": \"/assets/images/FeelsTheCat.jpg\", \"alttext\": \"Feels The Cat\" }"},
    {"Post_Id": "POST#001", "Post_Element_Type": "CONTENT", "Value": "{ \"blogtext\": \"Wall of text\" }"},
    {"Post_Id": "POST#002", "Post_Element_Type": "METADATA", "Post_Date": "2/1/2026", "Featured_Post_Date": "1#2/1/2026", "Value": "{ \"title\": \"My Python Journey\", \"summary\": \"My Python Experience\" }"},
    {"Post_Id": "POST#002", "Post_Element_Type": "IMAGE", "Value": "{ \"url\": \"/assets/images/PythonLogo.png\", \"alttext\": \"Official Python Logo\" }"},
    {"Post_Id": "POST#002", "Post_Element_Type": "CONTENT", "Value": "{ \"blogtext\": \"Wall of text\" }"},
]

for post in posts:
    table.put_item(Item=post)

print("Seed complete.")