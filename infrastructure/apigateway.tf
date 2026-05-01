resource "aws_apigatewayv2_api" "api" {
  name          = "blog-api"
  protocol_type = "HTTP"

  cors_configuration {
    allow_origins = ["https://d3ecwobg2ch99d.cloudfront.net","http://localhost:4200"]
    allow_methods = ["GET", "POST", "OPTIONS"]
    allow_headers = ["*"]
  }

  tags = local.common_tags
}

resource "aws_apigatewayv2_integration" "lambda" {
  api_id = aws_apigatewayv2_api.api.id

  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.get_posts.invoke_arn
}

resource "aws_apigatewayv2_route" "get_posts" {
  api_id    = aws_apigatewayv2_api.api.id
  route_key = "GET /posts"
  target = "integrations/${aws_apigatewayv2_integration.lambda.id}"

  authorization_type = "JWT"
  authorizer_id      = aws_apigatewayv2_authorizer.cognito.id
}

resource "aws_apigatewayv2_authorizer" "cognito" {
  api_id           = aws_apigatewayv2_api.api.id
  authorizer_type  = "JWT"
  identity_sources = ["$request.header.Authorization"]

  name = "cognito-jwt-authorizer"

  jwt_configuration {
    issuer   = "https://${module.cognito.issuer}"
    audience = [module.cognito.user_pool_client_id]
  }
}

resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.get_posts.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
}