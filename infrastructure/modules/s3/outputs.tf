output "user_data_bucket_name" {
  value = aws_s3_bucket.assets.bucket
}

output "assets_bucket_arn" {
  value = aws_s3_bucket.assets.arn
}

output "asset_bucket_regional_domain_name" {
  value = aws_s3_bucket.assets.bucket_regional_domain_name
}

output "blog_frontend_bucket_arn" {
  value = aws_s3_bucket.blog_frontend.arn
}

output "blog_frontend_bucket_regional_domain_name" {
  value = aws_s3_bucket.blog_frontend.bucket_regional_domain_name
}