resource "aws_cloudfront_origin_access_control" "assets" {
  name                              = "assets-oac"
  description                       = "OAC for assets bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                 = "always"
  signing_protocol                 = "sigv4"
}

resource "aws_cloudfront_distribution" "assets" {

  enabled = true

  origin {
    domain_name              = var.bucket_regional_domain_name
    origin_id                = "assets-s3"

    origin_access_control_id = aws_cloudfront_origin_access_control.assets.id
    
  }

  default_cache_behavior {
    target_origin_id       = "assets-s3"
    viewer_protocol_policy = "redirect-to-https"

    allowed_methods = ["GET", "HEAD"]

    cached_methods = ["GET", "HEAD"]

    cache_policy_id = "658327ea-f89d-4fab-a63d-7e88639e58f6"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  price_class = "PriceClass_100"

}