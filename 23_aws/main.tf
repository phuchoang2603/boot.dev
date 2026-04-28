module "vpc" {
  source = "./modules/vpc"

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

# module "ec2" {
#   source = "./modules/ec2"
#
#   key_name              = "patientping-key"
#   ami_id                = "ami-078da082344936fbb"
#   vpc_id                = module.vpc.vpc_id
#   subnet_id             = module.vpc.public_subnet_ids["a"]
#   instance_name         = "patientping-web-v2"
#   my_ip_cidr            = "107.144.161.161/32"
#   instance_profile_name = module.iam.instance_profile_name
# }

# module "rds" {
#   source = "./modules/rds"
#
#   vpc_id                = module.vpc.vpc_id
#   private_subnet_ids    = values(module.vpc.private_subnet_ids)
#   app_security_group_id = module.ec2.security_group_id
# }

# module "iam" {
#   source = "./modules/iam"
# }

# module "ssm" {
#   source = "./modules/ssm"
#
#   database_url = module.rds.DATABASE_URL
#   cmo_name     = "Dr. Strangelove"
# }

# module "cloudwatch" {
#   source = "./modules/cloudwatch"
#
#   instance_id = module.ec2.instance_id
#   alarm_email = "xuanphuc.a1gv@gmail.com"
# }

# module "route53" {
#   source = "./modules/route53"
#
#   vpc_id = module.vpc.vpc_id
#   www_ip = "10.0.10.50"
# }

# module "route53" {
#   source = "./modules/route53"
#
#   vpc_id   = module.vpc.vpc_id
#   www_ip   = "10.0.10.50"
#   cdn_name = module.cloudfront.domain_name
# }

# module "s3" {
#   source = "./modules/s3"
#
#   codename = "abc123"
# }

# module "cloudfront" {
#   source = "./modules/cloudfront"
#
#   bucket_name = module.s3.bucket_name
# }
