module "cognito" {
  source = "../../modules/cognito"

  app_name = "blog"
  env      = "dev"

  callback_urls = [
    "http://localhost:4200"
  ]

  logout_urls = [
    "http://localhost:4200"
  ]
}