resource "aws_security_group" "public" {
  name        = "patientping-public"
  description = "Allow public access"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow SSH from my computer"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip_cidr]
  }

  ingress {
    description = "Allow web traffic for PatientPing site"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
