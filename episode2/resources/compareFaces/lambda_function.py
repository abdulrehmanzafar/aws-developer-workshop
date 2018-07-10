from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib
import os

print('Loading function')
this_region = os.environ['AWS_DEFAULT_REGION'];
DDBTableName = os.environ['TableName']
print("region: " + this_region)

sns = boto3.client('sns')
s3 = boto3.client('s3')
ddb = boto3.resource('dynamodb')
table = ddb.Table(DDBTableName)
rekognition = boto3.client('rekognition', this_region)


def lambda_handler(event, context):
    '''Demonstrates S3 trigger that uses
    Rekognition APIs to detect faces, labels and index faces in S3 Object.
    '''

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    targetFile = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    print("bucket: " + bucket)
    print('targetFile: ' + targetFile)
