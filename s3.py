import boto3

REGION = "ap-south-1"
s3 = boto3.client("s3", region_name=REGION)

def create_s3_bucket():
    bucket_name = "rahul-aws-automation-bucket-518"

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }
        )
        print("✅ S3 Bucket Created:", bucket_name)
    except Exception as e:
        print("S3 Error:", e)