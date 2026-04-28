resource "aws_route53_zone" "patientping_internal" {
  name = "patientping.internal"

  vpc {
    vpc_id = var.vpc_id
  }
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.patientping_internal.zone_id
  name    = "www"
  type    = "A"
  ttl     = 15
  records = [var.www_ip]
}

resource "aws_route53_record" "blog" {
  zone_id = aws_route53_zone.patientping_internal.zone_id
  name    = "blog"
  type    = "CNAME"
  ttl     = 15
  records = ["www.patientping.internal"]
}

resource "aws_route53_record" "cdn" {
  zone_id = aws_route53_zone.patientping_internal.zone_id
  name    = "cdn"
  type    = "CNAME"
  ttl     = 15
  records = [var.cdn_name]
}
