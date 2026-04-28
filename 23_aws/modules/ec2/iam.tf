resource "aws_iam_policy" "ec2_readonly" {
  name        = "patientping-ec2-readonly"
  description = "Read-only EC2 access for PatientPing"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["ec2:Describe*"]
      Resource = "*"
    }]
  })
}

resource "aws_iam_role" "ec2_readonly" {
  name = "patientping-ec2-readonly-role"

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

resource "aws_iam_role_policy_attachment" "ec2_readonly" {
  role       = aws_iam_role.ec2_readonly.name
  policy_arn = aws_iam_policy.ec2_readonly.arn
}

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

resource "aws_iam_instance_profile" "ec2_readonly" {
  name = "patientping-ec2-readonly-role"
  role = aws_iam_role.ec2_readonly.name
}
