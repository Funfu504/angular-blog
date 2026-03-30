variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "profile" {
    description = "aws profile"
    type        = string
    default     = "terraform"
}

variable "table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "Blog_Post"
}