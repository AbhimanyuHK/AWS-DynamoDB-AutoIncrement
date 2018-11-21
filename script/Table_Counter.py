from __future__ import print_function
import DynamoDBClient

dynamo_db = DynamoDBClient.get_client()

table_name = "Counter"


def create_table():
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': "IncrementID", 'KeyType': "HASH"}  # Partition key
        ],
        'AttributeDefinitions': [
            {'AttributeName': "IncrementID", 'AttributeType': "N"}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }

    # Create the table
    dynamo_db.create_table(**params)

    # Wait for the table to exist before exiting
    print('Waiting for', table_name, '...')
    waiter = dynamo_db.get_waiter('table_exists')
    waiter.wait(TableName=table_name)


def set_initial_value():
    dynamo_db.put_item(
        TableName=table_name,

        Item={
            'IncrementID': {'N': str(1)}
        }
    )


def get_id():
    response = dynamo_db.scan(TableName=table_name)
    x = [item['ID'] for item in response['Items']][0]['N']
    # print(x)
    return x


def update_id(current_id):
    response = dynamo_db.update_item(
        TableName=table_name,
        Key={
            'IncrementID': {'N': str(1)}
        },
        UpdateExpression="set ID = :r ",
        ExpressionAttributeValues={
            ':r': {'N': str(int(current_id) + 1)}
        },
        ReturnValues='UPDATED_NEW'
    )
    print(response)


# create_table()
# set_initial_value()
# get_id()
# update_id(1)
