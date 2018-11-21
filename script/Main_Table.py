from __future__ import print_function
import DynamoDBClient
import Table_Counter

client = DynamoDBClient.get_client()

current_id = Table_Counter.get_id()
response = client.put_item(
    TableName='CounterCase',
    Item={
        'ID': {
            'N': str(current_id)
        },
        'Info': {
            'S': 'Testing Auto ID.'
        }
    }
)

[Table_Counter.update_id(current_id) for resp in response]
print(response)
