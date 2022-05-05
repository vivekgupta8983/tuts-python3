'''
Create mutliple IAM Users using python boto3

'''

#!/bin/python
import boto3
from random import choice
import sys
import csv


def get_iam_client_object():
    session = boto3.session.Session(profile_name="default")
    iam_client = session.client(service_name="iam", region_name="us-east-1")
    return iam_client


def get_random_password():
    len_of_password = 8
    valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))


def main():
    with open("iam_users.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0

        for row in csv_reader:

            iam_client = get_iam_client_object()
            Iam_user_name = str(row['IAM_User_Name'])
            passwd = get_random_password()
            PolicyArn = str(row['PolicyARN'])
            Programatic_Access = str(row['Programatic_Access'])
            Console_Access = str(row['Console_Access'])

            try:
                iam_client.create_user(UserName=Iam_user_name)
            except Exception as e:
                if e.response['Error']['Code'] == "EntityAlreadyExists":
                    print("Already Iam User with {} is exist".format(Iam_user_name))
                    sys.exit(0)
                else:
                    print("Please verify the following error and retry")
                    print(e)
                    sys.exit(0)

            if Programatic_Access == "Yes":
                response_key = iam_client.create_access_key(
                    UserName=Iam_user_name)
                iam_client.attach_user_policy(
                    UserName=Iam_user_name, PolicyArn=PolicyArn)
                
                
                csv_ob = open("Iam_user_name_credentails.csv", "w", newline='')
                csv_w = csv.writer(csv_ob)
                csv_w.writerow([count, Iam_user_name, passwd, response_key['AccessKey']
                                ['AccessKeyId'], response_key['AccessKey']['SecretAccessKey']])
                csv_ob.close()

            elif Console_Access == "Yes":
                iam_client.create_login_profile(
                    UserName=Iam_user_name, Password=passwd, PasswordResetRequired=False)

                iam_client.attach_user_policy(
                    UserName=Iam_user_name, PolicyArn=PolicyArn)
                
                
                csv_ob = open("Iam_user_name_credentails.csv", "w", newline='')
                csv_w = csv.writer(csv_ob)
                csv_w.writerow([count, Iam_user_name, passwd])
                csv_ob.close()

            elif Programatic_Access == "Yes" and Console_Access == "Yes":
                response_key = iam_client.create_access_key(
                    UserName=Iam_user_name)
                iam_client.create_login_profile(
                    UserName=Iam_user_name, Password=passwd, PasswordResetRequired=False)
                iam_client.attach_user_policy(
                    UserName=Iam_user_name, PolicyArn=PolicyArn)
                
                csv_ob = open("Iam_user_name_credentails.csv", "w", newline='')
                csv_w = csv.writer(csv_ob)
                csv_w.writerow([count, Iam_user_name, passwd, response_key['AccessKey']
                                ['AccessKeyId'], response_key['AccessKey']['SecretAccessKey']])
                csv_ob.close()
            else:
                print("NO access level defined...")

            
            return None
        count = +1


if __name__ == "__main__":
    main()
