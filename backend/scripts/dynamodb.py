import boto3
import yaml

# 1. Read YAML configuration
with open("../infrastructure/tables.yaml", "r") as f:
    config = yaml.safe_load(f)

# 2. Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

# 3. Create table
try:
    print(f"Creating table {config['TableName']}...")

    table = dynamodb.create_table(
        TableName=config['TableName'],
        AttributeDefinitions=config['AttributeDefinitions'],
        KeySchema=config['KeySchema'],
        BillingMode=config['BillingMode']
    )
    
    # Wait for table to be created
    dynamodb.get_waiter('table_exists').wait(TableName=config['TableName'])
    print("Table created successfully!")
except Exception as e:
    print(f"Error creating table: {e}")