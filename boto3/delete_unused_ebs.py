from logging import Filter
import boto3

aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

# Using Resource
# unused_ebs = {"Name": "status", "Values": ["available"]}
# for each_vol in ec2_con_re.volumes.filter(Filters=[unused_ebs]):
#     if not each_vol.tags:
#         print(each_vol.id, each_vol.state, each_vol.tags)
#         print("Deleting Unused Volumes...")
#         each_vol.delete()

# print("Deleted all unused and un tagged volumes.......")

# Using Client
for each_items in ec2_con_cl.describe_volumes()['Volumes']:
    if not "Tags" in each_items and each_items['State'] == 'available':
        print("Deleting", each_items['VolumeId'])
        ec2_con_cl.delete_volume(VolumeId=each_items['VolumeId'])
print("Deleted all unused and un tagged volumes.......")