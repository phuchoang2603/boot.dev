resource "aws_lb" "patientping" {
  name               = "patientping-alb"
  load_balancer_type = "application"
  internal           = false
  security_groups    = [aws_security_group.external.id]
  subnets            = var.public_subnet_ids
}

resource "aws_lb_target_group" "patientping" {
  name        = "patientping-tg"
  target_type = "ip"
  protocol    = "HTTP"
  port        = 8000
  vpc_id      = var.vpc_id

  health_check {
    path = "/"
  }
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.patientping.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.patientping.arn
  }
}

output "alb_dns_name" {
  value = aws_lb.patientping.dns_name
}
