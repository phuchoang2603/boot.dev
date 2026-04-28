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
