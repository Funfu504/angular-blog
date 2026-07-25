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
    domain_name              = var.asset_bucket_regional_domain_name
    origin_id                = "assets-s3"

    origin_access_control_id = aws_cloudfront_origin_access_control.assets.id    
  }

  tags = merge(var.tags, {
    Bucket = "Blog-Assets"
  })

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

resource "aws_cloudfront_origin_access_control" "blog_frontend" {
  description                       = "Created by CloudFront"
  name                              = "oac-angular-blog-dev-assets.s3.us-east-1.amazonaws.c-mk1p7azz5y1"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "blog_frontend" {
  aliases             = []
  comment             = null
  default_root_object = "index.html"
  enabled             = true
  http_version        = "http2"
  is_ipv6_enabled     = true
  price_class         = "PriceClass_All"
  retain_on_delete    = false
  staging             = false
  
  tags = merge(var.tags, {
    Bucket = "blog_frontend"
  })

  wait_for_deployment = true
  web_acl_id          = var.blog_frontend_waf_acl_id
  custom_error_response {
    error_caching_min_ttl = 10
    error_code            = 403
    response_code         = 200
    response_page_path    = "/index.html"
  }
  custom_error_response {
    error_caching_min_ttl = 10
    error_code            = 404
    response_code         = 200
    response_page_path    = "/index.html"
  }
  default_cache_behavior {
    allowed_methods            = ["GET", "HEAD"]
    cache_policy_id            = "658327ea-f89d-4fab-a63d-7e88639e58f6"
    cached_methods             = ["GET", "HEAD"]
    compress                   = true
    default_ttl                = 0
    max_ttl                    = 0
    min_ttl                    = 0
    smooth_streaming           = false
    target_origin_id           = "angular-blog-dev-assets.s3.us-east-1.amazonaws.com-mk1p6498vkd"
    trusted_key_groups         = []
    trusted_signers            = []
    viewer_protocol_policy     = "redirect-to-https"
    grpc_config {
      enabled = false
    }
  }
  
  origin {
    connection_attempts      = 3
    connection_timeout       = 10
    domain_name              = var.blog_frontend_bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.blog_frontend.id
    origin_id                = "angular-blog-dev-assets.s3.us-east-1.amazonaws.com-mk1p6498vkd"
  }

  restrictions {
    geo_restriction {
      locations        = []
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
    minimum_protocol_version       = "TLSv1"
  }
}