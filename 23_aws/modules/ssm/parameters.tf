resource "aws_ssm_parameter" "database_url" {
  name  = "/DATABASE_URL"
  type  = "String"
  value = var.database_url
}

resource "aws_ssm_parameter" "cmo_name" {
  name  = "/CMO_NAME"
  type  = "String"
  value = var.cmo_name
}
