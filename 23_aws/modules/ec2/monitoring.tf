# Alert
resource "aws_sns_topic" "alerts" {
  name = "patientping-alerts"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = var.alarm_email
}

resource "aws_cloudwatch_metric_alarm" "cpu" {
  alarm_name          = "patientping-cpu-alarm"
  alarm_description   = "Alert when CPU exceeds 20%"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  threshold           = 20
  period              = 60
  statistic           = "Average"

  namespace   = "AWS/EC2"
  metric_name = "CPUUtilization"
  dimensions = {
    InstanceId = aws_instance.web.id
  }

  alarm_actions = [aws_sns_topic.alerts.arn]
}

# Dashboard
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
            ["AWS/EC2", "CPUUtilization", "InstanceId", aws_instance.web.id]
          ]
          stat = "Average"
        }
      }
    ]
  })
}

