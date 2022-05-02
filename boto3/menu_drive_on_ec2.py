import boto3
import sys

aws_mgm_con = boto3.Session(profile_name="default")
# with Client
ec2_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")

# with Resource
ec2_res = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")

while True:
    print("This Script Preform the following actions on ec2 instance")
    print("""
          1. start
          2. stop
          3. terminate
          4. Reboot
          5. Exit
          """)
    opt = int(input("Enter Your Option: "))
    if opt == 1:
        instance_id = input("Enter your EC2 Instance Id: ")
        my_instance_obj = ec2_res.instance(instance_id)
        my_instance_obj.start()
        print("Starting Ec2 Instance...")

    elif opt == 2:
        instance_id = input("Enter your EC2 Instance Id: ")
        my_instance_obj = ec2_res.instance(instance_id)
        my_instance_obj.stop()
        print("Stoping Ec2 Instance...")

    elif opt == 3:
        instance_id = input("Enter your EC2 Instance Id: ")
        my_instance_obj = ec2_res.instance(instance_id)
        my_instance_obj.terminate()
        print("Terminating Ec2 Instance...")

    elif opt == 4:
        instance_id = input("Enter your EC2 Instance Id: ")
        my_instance_obj = ec2_res.instance(instance_id)
        my_instance_obj.reboot()
        print("Rebooting Ec2 Instance...")

    elif opt == 5:
        print("Thanks for Using our Script....")
        sys.exit()

    else:
        print("Your Option is not Valid....  Please Enter Valid Options....")
