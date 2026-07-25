variable "tags" {
  type = map(string)
}

variable "asset_bucket_regional_domain_name" {
  type = string
}

variable "blog_frontend_bucket_regional_domain_name" {
  type = string
}

variable "blog_frontend_waf_acl_id" {
  type = string
}