import boto3
from botocore.exceptions import ClientError

# Configure DynamoDB resource (ensure your AWS credentials are set up)
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-east-1"
)

table_name = 'Blog_Post'
table = dynamodb.Table(table_name)

# Define the primary key of the item to delete
# Example assumes a table with 'username' as the partition key and 'post_id' as the sort key
primary_keys = [{
    'Post_Id': 'POST#001',
    'Post_Element_Type': "IMAGE"
},
{
    'Post_Id': 'POST#001',
    'Post_Element_Type': "CONTENT"
},
{
    'Post_Id': 'POST#002',
    'Post_Element_Type': "IMAGE"
},
{
    'Post_Id': 'POST#002',
    'Post_Element_Type': "CONTENT"
}
]

def delete_dynamodb_item(key):
    try:
        response = table.delete_item(
            Key=key
        )
        print(f"Successfully deleted item: {key}")
        return response
    except ClientError as e:
        print(f"Error deleting item: {e.response['Error']['Message']}")
        raise

if __name__ == "__main__":
    for pks in primary_keys:
        delete_dynamodb_item(pks)