resource "aws_iam_group" "ec2_readers" {
  name = "patientping-ec2-readers"
}

resource "aws_iam_group_policy_attachment" "ec2_readers" {
  group      = aws_iam_group.ec2_readers.name
  policy_arn = aws_iam_policy.ec2_readonly.arn
}

resource "aws_iam_group_membership" "ec2_readers" {
  name = "patientping-ec2-readers-membership"

  users = ["patientping-admin-vinny"]
  group = aws_iam_group.ec2_readers.name
}
