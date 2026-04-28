resource "aws_ecs_cluster" "patientping" {
  name = "patientping-ecs"
}

resource "aws_ecs_cluster_capacity_providers" "patientping" {
  cluster_name = aws_ecs_cluster.patientping.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    capacity_provider = "FARGATE"
    weight            = 1
  }
}
