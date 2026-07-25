resource "aws_s3_bucket" "assets" {
  bucket = "blog-dev-assets"

  tags = merge(var.tags, {
    Name = "assets"
  })
}

resource "aws_s3_bucket_public_access_block" "assets" {
  bucket = aws_s3_bucket.assets.id

  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "assets" {
  bucket = aws_s3_bucket.assets.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "assets" {
  bucket = aws_s3_bucket.assets.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_ownership_controls" "assets" {
  bucket = aws_s3_bucket.assets.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_cors_configuration" "assets" {
  bucket = aws_s3_bucket.assets.id

  cors_rule {
    allowed_headers = ["*"]

    allowed_methods = [
      "GET",
      "HEAD",
      "PUT"
    ]

    allowed_origins = [
      var.cloudfront_distribution_code_domain, "http://localhost:4200"
    ]

    expose_headers = [
      "ETag"
    ]

    max_age_seconds = 3000
  }
}

resource "aws_s3_bucket_policy" "assets" {
  bucket = aws_s3_bucket.assets.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AllowCloudFrontAccess"
        Effect = "Allow"
        Principal = {
          Service = "cloudfront.amazonaws.com"
        }
        Action   = "s3:GetObject"
        Resource = "${aws_s3_bucket.assets.arn}/*"

        Condition = {
          StringEquals = {
            "AWS:SourceArn" = var.cloudfront_distribution_assets_arn
          }
        }
      }
    ]
  })
}

resource "aws_s3_bucket" "blog_frontend" {
  bucket = "angular-blog-dev-assets"

  tags = merge(var.tags, {
    Name = "blog_frontend"
  })
}

resource "aws_s3_bucket_public_access_block" "blog_frontend" {
  bucket = aws_s3_bucket.blog_frontend.id

  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "blog_frontend" {
  bucket = aws_s3_bucket.blog_frontend.id

  versioning_configuration {
    status = "Disabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "blog_frontend" {
  bucket = aws_s3_bucket.blog_frontend.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_ownership_controls" "blog_frontend" {
  bucket = aws_s3_bucket.blog_frontend.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}