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
    #Validate user inputs
    if len(sys.argv) == 1: 
        print("You need to pass in a more appropriate argument! Exiting.")
        return False
        
    file_name = sys.argv[1]
    
    if(path.exists(file_name)):
        return upload_file(file_name, "another-bucket-to-watch")
    else:
        with open(file_name, 'w'): pass
        return upload_file(file_name, "another-bucket-to-watch")


exit_code = main()

if(exit_code):
    print("Uploaded probably worked")
else:
    print("Upload for sure didn't work")