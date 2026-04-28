packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.2.8"
    }
  }
}

source "amazon-ebs" "patientping" {
  region        = "us-east-1"
  instance_type = "t3.micro"
  ssh_username  = "ec2-user"

  source_ami_filter {
    filters = {
      name                = "al2023-ami-*-x86_64"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
      architecture        = "x86_64"
    }
    owners      = ["amazon"]
    most_recent = true
  }

  ami_name = "patientping-{{timestamp}}"
}

build {
  sources = ["source.amazon-ebs.patientping"]

  provisioner "shell" {
    inline = [
      "sudo dnf upgrade -y",
      "sudo dnf install -y git amazon-cloudwatch-agent",
      "curl -LsSf https://astral.sh/uv/install.sh | sh",
      "cd /home/ec2-user",
      "git clone https://github.com/bootdotdev/patientping-web.git",
      "cd /home/ec2-user/patientping-web",
      "/home/ec2-user/.local/bin/uv sync"
    ]
  }

  provisioner "file" {
    source      = "files/patientping-monitoring.json"
    destination = "/tmp/patientping-monitoring.json"
  }

  provisioner "file" {
    source      = "files/patientping.service"
    destination = "/tmp/patientping.service"
  }

  provisioner "shell" {
    inline = [
      "sudo mkdir -p /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d",
      "sudo mv /tmp/patientping-monitoring.json /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/patientping-monitoring.json",
      "sudo touch /var/log/patientping.log",
      "sudo chown ec2-user:ec2-user /var/log/patientping.log",
      "sudo mv /tmp/patientping.service /etc/systemd/system/patientping.service",
      "sudo systemctl daemon-reload",
      "sudo systemctl enable amazon-cloudwatch-agent",
      "sudo systemctl enable patientping.service"
    ]
  }
}
