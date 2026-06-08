variable "tags" {
  type = map(string)
}

variable "cloudfront_distribution_assets_arn" {
  type = string
}

variable "cloudfront_distribution_code_domain" {
    type = string
}