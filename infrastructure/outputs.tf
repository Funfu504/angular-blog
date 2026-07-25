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

output "user_data_bucket_name" {
  value = module.s3.user_data_bucket_name
}

output "assets_bucket_arn" {
  value = module.s3.assets_bucket_arn
}

output "bucket_regional_domain_name" {
  value = module.s3.asset_bucket_regional_domain_name
}

output "blog_frontend_bucket_arn" {
  value = module.s3.blog_frontend_bucket_arn
}

output "blog_frontend_acl_arn" {
  value = module.waf.blog_frontend_acl_arn
}