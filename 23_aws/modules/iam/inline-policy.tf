/*
resource "aws_iam_role_policy" "ssm_access" {
  name = "patientping-ssm-access"
  role = aws_iam_role.ec2_readonly.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["ssm:GetParameter", "ssm:GetParameters"]
      Resource = [
        "arn:aws:ssm:*:*:parameter/DATABASE_URL",
        "arn:aws:ssm:*:*:parameter/CMO_NAME",
      ]
    }]
  })
}
*/

resource "aws_iam_role_policy" "cloudwatch_logs_access" {
  name = "patientping-cloudwatch-logs-access"
  role = aws_iam_role.monitoring.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogStreams",
      ]
      Resource = ["arn:aws:logs:*:*:*"]
    }]
  })
}

resource "aws_iam_role_policy" "ssm_access_monitoring" {
  name = "patientping-ssm-access"
  role = aws_iam_role.monitoring.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["ssm:GetParameter"]
      Resource = [
        "arn:aws:ssm:*:*:parameter/DATABASE_URL",
        "arn:aws:ssm:*:*:parameter/CMO_NAME",
      ]
    }]
  })
}
