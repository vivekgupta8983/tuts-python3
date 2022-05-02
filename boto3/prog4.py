import boto3

aws_mgmt_con = boto3.Session(profile_name="default")

iam_cli = aws_mgmt_con.client(service_name="iam", region_name="us-east-1")
s3_cli = aws_mgmt_con.client(service_name="s3", region_name="us-east-1")
ec2_cli = aws_mgmt_con.client(service_name="ec2", region_name="us-east-1")


# List all IAM UserName
response = iam_cli.list_users()

for each_item in response['Users']:
    print(each_item['UserName'])

# # List all EC2 Instance ID
# response = ec2_cli.client.describe_instances()
# for each_item in response['Reservations']:
#     for each_instance in each_item['Instances']:
#         print(each_instance['InstanceId'])

# List all S3 Buckets:
response = s3_cli.client.list_buckets()
for each_bucket in response['Buckets']:
    print(each_bucket['Name'])
print(response)
