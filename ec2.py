import boto3

REGION = "ap-south-1"
ec2 = boto3.resource("ec2", region_name=REGION)

def create_ec2_instance():
    try:
        instances = ec2.create_instances(
            ImageId="ami-0e38835daf6b8a2b9",
            InstanceType="t2.micro",
            MinCount=1,
            MaxCount=1,
            KeyName="Mys",
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": "Boto3-Automation-EC2"}
                    ]
                }
            ]
        )

        print("✅ EC2 Instance Created:", instances[0].id)

    except Exception as e:
        print("EC2 Error:", e)