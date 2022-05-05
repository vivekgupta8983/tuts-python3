import boto3

aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")

# print("Using all()")
# for each in ec2_con_re.instances.all():
#     print(each)

# print("Using limit()")
# for each in ec2_con_re.instances.limit(1):
#     print(each)

f1={"Name": "instance-state-name", "Values":['running','stopped']}
f2={"Name":"instance-type","Values":['t2.micro']}

for each in ec2_con_re.instances.filter(Filters=[f1,f2]):
	print(each)
