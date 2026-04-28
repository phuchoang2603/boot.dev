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

resource "aws_iam_instance_profile" "ec2_readonly" {
  name = "patientping-ec2-readonly-role"
  role = aws_iam_role.ec2_readonly.name
}

output "instance_profile_name" {
  value = aws_iam_instance_profile.ec2_readonly.name
}
