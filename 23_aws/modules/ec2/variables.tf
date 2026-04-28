variable "key_name" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ami_id" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "subnet_id" {
  type = string
}

variable "instance_name" {
  type = string
}

variable "my_ip_cidr" {
  type = string
}

variable "alarm_email" {
  type = string
}
