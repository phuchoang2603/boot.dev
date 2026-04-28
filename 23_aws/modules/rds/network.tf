resource "aws_db_subnet_group" "private" {
  name        = "patientping-private-subnet-group"
  description = "Private subnets for RDS DB instances"
  subnet_ids  = var.private_subnet_ids
}


resource "aws_security_group" "db" {
  name        = "patientping-rds-sg"
  description = "PatientPing RDS security group"
  vpc_id      = var.vpc_id

  ingress {
    description     = "Allow PostgreSQL from app server"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [var.app_security_group_id]
  }
}

