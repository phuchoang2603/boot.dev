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

output "security_group_id" {
  value = aws_security_group.public.id
}

resource "aws_eip" "web" {
  domain = "vpc"

  tags = {
    Name = "patientping-web-eip"
  }
}

resource "aws_eip_association" "web" {
  allocation_id = aws_eip.web.id
  instance_id   = aws_instance.web.id
}

output "public_ip" {
  value = aws_eip.web.public_ip
}
