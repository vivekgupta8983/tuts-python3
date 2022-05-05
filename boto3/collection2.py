import boto3

aws_mag_con = boto3.session.Session(profile_name="default")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")

ec2_con_cl = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

all_instance_ids = []
for each in ec2_con_re.instances.all():
    all_instance_ids.append(each.id)

waiter=ec2_con_cl.get_waiter('instance_running')
print("Starting all your Instances---------------")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instance_ids)
print("Your all instances are in running state")    


# waiter = ec2_con_cl.get_waiter('instance_running')

# print("Starting Instances....")

# ec2_con_re.instances.start()
# waiter.wait(InstanceIds=['i-0e78e80c371c76531'])
# print("your all instance are up and running")
