provider "aws" {
  region                      = "eu-west-2"
  access_key                  = "test"  # LocalStack uses dummy values
  endpoints {
    s3 = "http://localstack:4566"  # Point to LocalStack for S3
  }
}