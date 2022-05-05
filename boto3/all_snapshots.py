import boto3
aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
count = 0
for each_items in ec2_con_cl.describe_snapshots(OwnerIds=['self'])['Snapshots']:
    print("Snapshot Id: ", each_items['SnapshotId'], "and size is:",
          each_items['VolumeSize'], "state:", each_items['State'])
    # ec2_con_cl.delete_snapshot(SnapshotId=each_items['SnapshotId'])
    count+1
