import boto3
import csv
aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

csv_ob = open("ec2_inventry_info.csv", "w", newline='')
csv_w = csv.writer(csv_ob)
csv_w.writerow(["SR_No", "Instance ID", "Instance Type", "Architecture", "Created Date", "VpcId", "PublicIpAddress"
                "Private IP", "State", "Volume_Id"])
count = 0

for each_instances in ec2_con_cl.describe_instances()['Reservations']:
    for each_items in each_instances['Instances']:
        print(each_items['InstanceId'], each_items['InstanceType'], each_items['Architecture'], each_items['LaunchTime'], each_items['VpcId'],
              each_items['PublicIpAddress'],  each_items['PrivateIpAddress'], each_items['State']['Name'], each_items['BlockDeviceMappings'][0]['Ebs']['VolumeId'])
        csv_w.writerow([count, each_items['InstanceId'], each_items['InstanceType'], each_items['Architecture'], each_items['LaunchTime'], each_items['VpcId'],
                       each_items['PublicIpAddress'],  each_items['PrivateIpAddress'], each_items['State']['Name'], each_items['BlockDeviceMappings'][0]['Ebs']['VolumeId']])
        count = +1
csv_ob.close()
