
from src.dal.dynamo import get_dynamo
from src.common.config import Config

from src.dal.model.photo import Photo


if __name__ == '__main__':

    Config.setup()
    dynamodb = get_dynamo('local')

    table = dynamodb.create_table(**Photo.schema)
    table.meta.client.get_waiter('table_exists').wait(TableName=Photo.schema['TableName'])

    print('############')
    print('Dynamo Ready')
    print('############')
