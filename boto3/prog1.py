import profile
import boto3
aws_con=boto3.session.Session(profile_name="default")
iam_con=aws_con.resource('iam')


for each_user in iam_con.users.all():
    print(each_user)
    
    