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