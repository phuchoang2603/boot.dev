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
