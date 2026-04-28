resource "aws_s3_bucket" "favicon" {
  bucket = "patientping-favicon-bucket-${var.codename}"
}

resource "aws_s3_bucket_public_access_block" "favicon" {
  bucket                  = aws_s3_bucket.favicon.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
