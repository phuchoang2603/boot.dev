resource "tls_private_key" "this" {
  algorithm = "ED25519"
}

resource "aws_key_pair" "this" {
  key_name   = var.key_name
  public_key = tls_private_key.this.public_key_openssh
}

resource "local_file" "private_key" {
  filename        = pathexpand("~/.ssh/${var.key_name}")
  content         = tls_private_key.this.private_key_openssh
  file_permission = "0600"
}
