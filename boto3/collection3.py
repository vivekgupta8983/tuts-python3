import boto3

aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
server_ids=[]
f1 = {"Name": "tag:Name", "Values":['Server1'] }
for each in ec2_con_re.instances.filter(Filters=[f1]):
    server_ids.append(each.id)
    
print(server_ids)
print("-------------------------------")

for each in ec2_con_cl.describe_instances()['Reservations']:
    for each_items in each['Instances']:
        print(each_items['InstanceId'])
        
