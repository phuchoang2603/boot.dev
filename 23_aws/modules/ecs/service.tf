resource "aws_ecs_service" "patientping" {
  name            = "patientping-svc"
  cluster         = aws_ecs_cluster.patientping.id
  task_definition = aws_ecs_task_definition.patientping.arn
  desired_count   = 1

  capacity_provider_strategy {
    capacity_provider = "FARGATE"
    weight            = 1
  }

  network_configuration {
    subnets          = var.public_subnet_ids
    security_groups  = [aws_security_group.internal.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.patientping.arn
    container_name   = "patientping-ecs"
    container_port   = 8000
  }

  depends_on = [aws_lb_listener.http]
}
