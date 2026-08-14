resource "aws_lambda_function" "migration_runner" {
  function_name    = "migration_runner"
  runtime          = "python3.13"
  handler          = "image_data_migration.handler"
  timeout          = 10  # seconds
  filename         = "../backend/build/image_data_migration.zip"
  source_code_hash = filebase64sha256("../backend/build/image_data_migration.zip")

  #the OS environment variables referenced in the backend/src/blogservicepkg/repository/config.py file are not overwritten
  #in this terraform lambda file because AWS defaults to the dynamo db instance present in the region during runtime.

  role = var.iam_lambda_exec_arn

  tags = var.tags
}

resource "aws_cloudwatch_log_group" "migration_runner" {
  name              = "/aws/lambda/migration_runner"
  retention_in_days = 14

  tags = merge( 
    var.tags,
    { Function = "migration-runner" }
  )

}