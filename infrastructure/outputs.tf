output "table_name" {
  value = aws_dynamodb_table.blog_table.name
}

output "table_arn" {
  value = aws_dynamodb_table.blog_table.arn
}

output "api_id" {
  description = "The ID of the HTTP API"
  value       = aws_apigatewayv2_api.api.id
}