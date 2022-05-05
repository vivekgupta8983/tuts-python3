from http import client
from pydoc import describe
import boto3

aws_mgm_con = boto3.Session(profile_name="default")
ec2_res = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")
ec2_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")

# print(dir(ec2_res.meta))
for each in ec2_res.meta.client.describe_regions()['Regions']:
    print(each['RegionName'])
