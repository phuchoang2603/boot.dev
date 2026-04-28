module "network" {
  source = "./modules/network"

  vpc_cidr = "10.0.0.0/22"
  vpc_name = "patientping"

  public_route_table_name  = "patientping-public-rt"
  private_route_table_name = "patientping-private-rt"
  internet_gateway_name    = "patientping-igw"

  public_subnets = {
    a = {
      availability_zone = "us-east-1a"
      cidr_block        = "10.0.2.0/24"
      name              = "patientping-public-a"
    }
    b = {
      availability_zone = "us-east-1b"
      cidr_block        = "10.0.3.0/24"
      name              = "patientping-public-b"
    }
  }

  private_subnets = {
    a = {
      availability_zone = "us-east-1a"
      cidr_block        = "10.0.0.0/24"
      name              = "patientping-private-a"
    }
    b = {
      availability_zone = "us-east-1b"
      cidr_block        = "10.0.1.0/24"
      name              = "patientping-private-b"
    }
  }
}

module "ec2" {
  source = "./modules/ec2"

  key_name             = "patientping-key"
  ami_id               = "ami-078da082344936fbb"
  vpc_id               = module.network.vpc_id
  subnet_id            = module.network.public_subnet_ids["a"]
  instance_name        = "patientping-web-v2"
  my_ip_cidr           = "107.144.161.161/32"
module "rds" {
  source = "./modules/rds"

  vpc_id             = module.network.vpc_id
  private_subnet_ids = values(module.network.private_subnet_ids)
  app_security_group_id = module.ec2.security_group_id
}
}
