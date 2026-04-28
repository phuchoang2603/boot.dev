output "DATABASE_URL" {
  value     = "postgresql://postgres:${random_password.db.result}@${aws_db_instance.patientping.address}:5432/patientping"
  sensitive = true
}
