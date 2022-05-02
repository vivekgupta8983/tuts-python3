from http import client
from urllib import response
import boto3


aws_con = boto3.session.Session(profile_name="default")
sts_cli = aws_con.client(service_name="sts", region_name="us-east-1")
response = sts_cli.get_caller_identity()
print(response['Account'])
