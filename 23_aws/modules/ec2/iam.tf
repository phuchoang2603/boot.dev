# Role
resource "aws_iam_role" "ec2" {
  name = "patientping-ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

# Policies
resource "aws_iam_role_policy" "ec2_readonly" {
  name = "patientping-ec2-readonly"
  role = aws_iam_role.ec2.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["ec2:Describe*"]
      Resource = "*"
    }]
  })
}

resource "aws_iam_role_policy" "ssm_access" {
  name = "patientping-ssm-access"
  role = aws_iam_role.ec2.id

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

resource "aws_iam_role_policy" "cloudwatch_logs_access" {
  name = "patientping-cloudwatch-logs-access"
  role = aws_iam_role.ec2.id

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
      Resource = ["arn:aws:logs:*:*:log-group:/ecs/patientping-ecs*"]
    }]
  })
}

# Profile
resource "aws_iam_instance_profile" "ec2_readonly" {
  name = "patientping-ec2-role"
  role = aws_iam_role.ec2.name
}
