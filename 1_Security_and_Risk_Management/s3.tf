resource "aws_s3_bucket" "vulnerability_reports" {
  bucket = "vulnerability-reports-bucket"
}

resource "aws_s3_bucket_acl" "vulnerability_reports_acl" {
  bucket = aws_s3_bucket.vulnerability_reports.id
  acl    = "private"
}