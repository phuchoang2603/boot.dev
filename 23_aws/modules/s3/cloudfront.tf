resource "aws_cloudfront_distribution" "favicon" {
  enabled             = true
  comment             = "patientping-favicon-distro"
  default_root_object = "favicon.ico"

  origin {
    domain_name = "${aws_s3_bucket.favicon.bucket}.s3.amazonaws.com"
    origin_id   = "patientping-favicon-origin"
  }

  default_cache_behavior {
    target_origin_id       = "patientping-favicon-origin"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}

output "domain_name" {
  value = aws_cloudfront_distribution.favicon.domain_name
}
