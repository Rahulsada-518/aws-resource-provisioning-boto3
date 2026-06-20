from iam import create_iam_user
from s3 import create_s3_bucket
from ec2 import create_ec2_instance

print("🚀 AWS Automation Started")

create_iam_user()
create_s3_bucket()
create_ec2_instance()

print("🎉 AWS Automation Completed")