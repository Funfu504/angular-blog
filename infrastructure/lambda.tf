resource "aws_lambda_function" "get_posts" {
  function_name    = "get_posts"
  runtime          = "python3.13"
  handler          = "lambda_read_posts.handler"
  timeout          = 10  # seconds
  filename         = "../backend/build/lambda_read_posts.zip"
  source_code_hash = filebase64sha256("../backend/build/lambda_read_posts.zip")

  #the OS environment variables referenced in the backend/src/blogservicepkg/repository/config.py file are not overwritten
  #in this terraform lambda file because AWS defaults to the dynamo db instance present in the region during runtime.

  role = aws_iam_role.lambda_exec.arn

  tags = local.common_tags
}