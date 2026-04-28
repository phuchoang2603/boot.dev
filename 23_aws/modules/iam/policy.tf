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
