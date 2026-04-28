resource "random_password" "db" {
  length  = 16
  special = false
}

resource "aws_db_instance" "patientping" {
  identifier     = "patientping-db"
  engine         = "postgres"
  engine_version = "17"

  instance_class          = "db.t3.micro"
  allocated_storage       = 20
  storage_type            = "gp2"
  storage_encrypted       = false
  skip_final_snapshot     = true
  deletion_protection     = false
  backup_retention_period = 1

  username = "postgres"
  password = random_password.db.result
  db_name  = "patientping"

  publicly_accessible    = false
  db_subnet_group_name   = aws_db_subnet_group.private.name
  vpc_security_group_ids = [aws_security_group.db.id]
  multi_az               = false

  performance_insights_enabled = false
  monitoring_interval          = 0

  auto_minor_version_upgrade = true
}
