import logging
import boto3
import sys
from os import path
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    file_name = sys.argv[1]
    if not file_name: return
    print("the script has the name %s" % (sys.argv[0]))
    if(path.exists(file_name)):
        upload_file(file_name, "another-bucket-to-watch")
    else:
        with open(file_name, 'w'): pass
        upload_file(file_name, "another-bucket-to-watch")


main()