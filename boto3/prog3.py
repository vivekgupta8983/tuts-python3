import boto3

aws_mgmt_con=boto3.session.Session(profile_name="default")


iam_con_cli=aws_mgmt_con.client(service_name='iam',region_name="us-east-1")

print(iam_con_cli)

iam_con_res=aws_mgmt_con.resource(service_name='iam',region_name="us-east-1")
print(iam_con_res)