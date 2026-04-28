resource "aws_instance" "web" {
  ami                         = data.aws_ami.amazon_linux.id
  instance_type               = var.instance_type
  subnet_id                   = var.subnet_id
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.public.id]
  key_name                    = aws_key_pair.this.key_name

  tags = {
    Name = var.instance_name
  }
}
