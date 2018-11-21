from __future__ import print_function
import boto3


def get_client():
    dynamo_db = boto3.client('dynamodb')
    return dynamo_db
