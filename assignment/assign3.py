'''
Write a Python script to export IAM User Details into a csv file.
'''
#!/bin/python
from itertools import count
import boto3
import sys
import csv
import datetime


def get_iam_client_object():
    session = boto3.session.Session(profile_name="default")
    iam_client = session.client(service_name="iam", region_name="us-east-1")
    return iam_client


def main():
    iam_client = get_iam_client_object()
    response = iam_client.list_users()['Users']

    csv_ob = open("iam_user_info.csv", "w", newline='')
    csv_w = csv.writer(csv_ob)
    csv_w.writerow(["SR_No", "UserName ID", "UserId", "Arn",
                   "Created Date"])

    # list_policy = iam_client.list_user_policies()
    # print(list_policy)

    for each_user in response:
        # User Name, User Id, User ARN, User Creation Date, Attached Policies and Groups associated
        print(each_user['UserName'], each_user['UserId'], each_user['Arn'],
              each_user['CreateDate'].strftime("%Y-%m-%d"))

        csv_w.writerow([each_user['UserName'], each_user['UserId'], each_user['Arn'],
                        each_user['CreateDate'].strftime("%Y-%m-%d")])


if __name__ == "__main__":
    main()
