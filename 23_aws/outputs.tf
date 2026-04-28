# output "patientping_web_public_ip" {
#   value = module.ec2.public_ip
# }

# output "DATABASE_URL" {
#   value     = module.rds.DATABASE_URL
#   sensitive = true
# }

output "invoke_url" {
  value = module.lambda.invoke_url
}
