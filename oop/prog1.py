import boto3
import csv

AWS_REGION = "us-west-2"

filename = input("Enter the path of inventry file: ")
s3_client = boto3.client('s3', region_name=AWS_REGION)
ec2_client = boto3.client('ec2', region_name=AWS_REGION)

aws_resource = input("Please Enter either s3 or ec2:")

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file,)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Keys are {", ".join(row)}')
            line_count += 1

            tags = {'VantaNonProd': str(row['VantaNonProd']), 'VantaDescription': str(row['VantaDescription']), 'VantaContainsUserData': str(
                row['VantaContainsUserData']), 'VantaUserDataStored': str(row['VantaUserDataStored']), 'VantaNoAlert': str(row['VantaNoAlert'])}
        line_count += 1

        old_tags = {}

        old = s3_client.get_bucket_tagging(Bucket=row['name'])
        old_tags = {i['Key']: i['Value'] for i in old['TagSet']}

        new_tags = {**old_tags, **tags}

        if aws_resource == "s3|S3":
            response = s3_client.put_bucket_tagging(
                Bucket=row['name'],
                Tagging={
                    'TagSet': [{'Key': str(k), 'Value': str(v)} for k, v in new_tags.items()]
                }
            )
            print(response)
        elif aws_resource == "ec2|EC2":
            response = ec2_client.create_tags(
                Resources=[
                    str(row['name']),
                ],
                Tags=[
                    {'Key': str(k), 'Value': str(v)} for k, v in tags.items()
                ]
            )
            print(response)
        else:
            print("Please Enter either s3 or ec2: ")
    line_count += 1
