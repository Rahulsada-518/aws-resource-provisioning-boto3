import boto3

iam = boto3.client("iam")

def create_iam_user():
    user_name = "automation-user"

    try:
        iam.create_user(UserName=user_name)
        print("✅ IAM User Created:", user_name)
    except Exception as e:
        print("IAM Error:", e)