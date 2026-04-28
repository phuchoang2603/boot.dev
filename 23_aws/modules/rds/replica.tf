# resource "aws_db_instance" "replica" {
#   identifier             = "patientping-replica"
#   replicate_source_db    = aws_db_instance.patientping.arn
#   instance_class         = "db.t3.micro"
#   publicly_accessible    = false
#   db_subnet_group_name   = aws_db_subnet_group.private.name
#   vpc_security_group_ids = [aws_security_group.db.id]
#   skip_final_snapshot    = true
#
#   performance_insights_enabled = false
#   monitoring_interval          = 0
# }
#
# output "replica_endpoint" {
#   value = aws_db_instance.replica.address
# }
