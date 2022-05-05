import boto3

aws_mgm_con = boto3.session.Session(profile_name="default")

# with Resource
ec2_res = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")

my_inst_ob = ec2_res.Instance("i-0e78e80c371c76531")
print("Starting given instance using resource objects ...")
# my_inst_ob.start()
# my_inst_ob.wait_until_running()  # Resource Waiter waits for 200 sec (40 Checks after every 5 sec)
my_inst_ob.stop()
my_inst_ob.wait_until_stopped()
print("Now your instance is up and running...")

# with Client
ec2_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")
ec2_cli.start_instances(InstanceIds=["i-0e78e80c371c76531"])

print("Starting given instance using Client Objects...")
waiter = ec2_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=["i-0e78e80c371c76531"])  # 40 checks after every 15 seconds
print("Now your instance is up and running...")
