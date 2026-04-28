resource "aws_security_group" "external" {
  name        = "patientping-external"
  description = "Allow HTTP traffic from the internet to the load balancer"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow HTTP traffic from the internet to the load balancer"
    from_port   = 80
    to_port     = 80
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

resource "aws_security_group" "internal" {
  name        = "patientping-internal"
  description = "Allow traffic from the load balancer to ECS tasks"
  vpc_id      = var.vpc_id

  ingress {
    description     = "Allow traffic from the load balancer to ECS tasks"
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    security_groups = [aws_security_group.external.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "external_security_group_id" {
  value = aws_security_group.external.id
}

output "internal_security_group_id" {
  value = aws_security_group.internal.id
}
