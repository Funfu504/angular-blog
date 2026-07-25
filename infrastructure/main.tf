module "cognito" {
  source = "./modules/cognito"

  app_name = "blog"
  env      = "dev"

  callback_urls = [
    "http://localhost:4200/auth/callback",
    "https://d3ecwobg2ch99d.cloudfront.net/auth/callback"
  ]

  logout_urls = [
    "http://localhost:4200",
    "https://d3ecwobg2ch99d.cloudfront.net"
  ]
}

module "s3" {
  source = "./modules/s3"

  tags = local.common_tags

  cloudfront_distribution_assets_arn = module.cloudfront.cloudfront_distribution_assets_arn
  cloudfront_distribution_code_domain = "https://d3ecwobg2ch99d.cloudfront.net"
}

module "waf" {
  source = "./modules/waf"

  tags = local.common_tags
}

module "cloudfront" {
  source = "./modules/cloudfront"

  tags = local.common_tags

  asset_bucket_regional_domain_name = module.s3.asset_bucket_regional_domain_name
  blog_frontend_bucket_regional_domain_name = module.s3.blog_frontend_bucket_regional_domain_name
  blog_frontend_waf_acl_id = module.waf.blog_frontend_acl_arn
}