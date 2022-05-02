from pprint import pprint
from turtle import reset
from urllib import response
import boto3

aws_mgm_con = boto3.Session(profile_name="default")

ec2_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")

response = ec2_cli.describe_instance()['Reservation']
for each_items in response:
    for each_instance_info in each_items["Instances"]:
        pprint("The Image is: {}\n The Instance Id is: {}\n The Instance Launch Time is: {}".format(
            each_items['ImageID'], each_items['InstanceId'], each_items['LaunchTime'].strftime("%Y-%m-%d")))

response = ec2_cli.client.describe_volumes()
for each_items in response():
    print("The Volume id is: {}\n The AZ is: {}\n The Volume Type is: {}\n".format(
        each_items['VolumeId'], each_items['AvailabilityZone'], each_items['VolumeType']))
