resource "aws_dynamodb_table" "blog_table" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"

  hash_key  = "Post_Id"
  range_key = "Post_Element_Type"

  attribute {
    name = "Post_Id"
    type = "S"
  }

  attribute {
    name = "Post_Element_Type"
    type = "S"
  }

  attribute {
    name = "Post_Date"
    type = "S"
  }  

  attribute {
    name = "Featured_Post_Date"
    type = "S"
  }

  # GSI: Query by PK + createdAt
  global_secondary_index {
    name            = "GSI_PostsByPostDate"
    hash_key        = "Post_Element_Type"
    range_key       = "Post_Date"
    projection_type = "ALL"
  }

  # GSI: Query featured posts
  global_secondary_index {
    name            = "GSI_PostsByFeaturePostDate"
    hash_key        = "Post_Element_Type"
    range_key       = "Featured_Post_Date"
    projection_type = "ALL"
  }

  tags = {
    Environment = "dev"
    Project     = "blog"
  }
}