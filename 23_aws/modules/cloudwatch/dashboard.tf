resource "aws_cloudwatch_dashboard" "patientping" {
  dashboard_name = "patientping-dashboard"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        x      = 0
        y      = 0
        width  = 12
        height = 6
        properties = {
          title  = "patientping-web-v2 CPU"
          view   = "timeSeries"
          region = "us-east-1"
          period = 300
          metrics = [
            ["AWS/EC2", "CPUUtilization", "InstanceId", var.instance_id]
          ]
          stat = "Average"
        }
      }
    ]
  })
}

