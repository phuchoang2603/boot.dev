resource "aws_route53_zone" "patientping_internal" {
  name = "patientping.internal"

  vpc {
    vpc_id = var.vpc_id
  }
}
