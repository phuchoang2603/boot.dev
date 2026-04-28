variable "vpc_cidr" {
  type = string
}

variable "vpc_name" {
  type = string
}

variable "internet_gateway_name" {
  type = string
}

variable "public_route_table_name" {
  type = string
}

variable "private_route_table_name" {
  type = string
}

variable "public_subnets" {
  type = map(object({
    availability_zone = string
    cidr_block        = string
    name              = string
  }))
}

variable "private_subnets" {
  type = map(object({
    availability_zone = string
    cidr_block        = string
    name              = string
  }))
}
