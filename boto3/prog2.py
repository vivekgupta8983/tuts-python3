import boto3
aws_con=boto3.session.Session(profile_name="default")
s3_con=aws_con.resource('s3')

for each_bucket in s3_con.buckets.all():
    print(each_bucket)