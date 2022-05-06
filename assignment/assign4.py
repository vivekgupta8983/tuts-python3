'''
Write a Python script to export IAM User Details into a csv file.
'''
import boto3
import argparse
import csv
import os

# output_file_path = "tagged-ec2-resources.csv"
field_names = ['ResourceArn', 'TagKey', 'TagValue']


def get_iam_client_object():
    session = boto3.session.Session(profile_name="default")
    iam_client = session.client(service_name="iam", region_name="us-east-1")
    return iam_client


def writeToCsv(writer, args, tag_list):
    for resource in tag_list:
        print("Extracting tags for resource: " +
              resource['ResourceARN'] + "...")
        for tag in resource['Tags']:
            row = dict(
                ResourceArn=resource['ResourceARN'], TagKey=tag['Key'], TagValue=tag['Value'])
            writer.writerow(row)


def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True,
                        help="Output CSV file (eg, /tmp/tagged-resources.csv)")
    return parser.parse_args()


def main():
    # List all regions
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    all_regions = []

    for each_regions in ec2_client.describe_regions()['Regions']:
        all_regions.append(each_regions.get('RegionName'))

    args = input_args()

    for regions in all_regions:
        print("Working on {} region".format(regions))
        restag = boto3.client('resourcegroupstaggingapi', region_name=regions)
        with open(args.output, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL,
                                    delimiter=',', dialect='excel', fieldnames=field_names)
            writer.writeheader()
            response = restag.get_resources(ResourcesPerPage=50)
            writeToCsv(writer, args, response['ResourceTagMappingList'])
            while 'PaginationToken' in response and response['PaginationToken']:
                token = response['PaginationToken']
                response = restag.get_resources(
                    ResourcesPerPage=50, PaginationToken=token)
                writeToCsv(writer, args, response['ResourceTagMappingList'])


if __name__ == '__main__':
    main()
