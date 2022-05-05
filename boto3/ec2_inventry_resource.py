import boto3
import csv
aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

csv_ob=open("inventry_info.csv", "w", newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["SR_No", "Instance ID", "Instance Type", "Architecture", "Created Date", "Private IP"])
count=0

for each in ec2_con_re.instances.all():
    print(count, each.instance_id, each.instance_type, each.architecture, each.launch_time.strftime("%Y-%m-%d"), each.private_ip_address)
    csv_w.writerow([count, each.instance_id, each.instance_type, each.architecture, each.launch_time.strftime("%Y-%m-%d"), each.private_ip_address])
    count=+1
csv_ob.close()

