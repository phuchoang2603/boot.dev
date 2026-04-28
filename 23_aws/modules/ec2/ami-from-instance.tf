resource "aws_ami_from_instance" "web" {
  name               = "patientping-web-base"
  source_instance_id = aws_instance.web.id
}

output "ami_id" {
  value = aws_ami_from_instance.web.id
}
