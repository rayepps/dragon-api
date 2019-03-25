
from src.dal.model.schema import schema
from src.dal.dynamo import get_dynamo
from src.common.config import Config

if __name__ == '__main__':

    Config.setup()
    dynamodb = get_dynamo('local')

    table = dynamodb.create_table(**schema)
    table.meta.client.get_waiter('table_exists').wait(TableName=schema['TableName'])

    print('############')
    print('Dynamo Ready')
    print('############')
