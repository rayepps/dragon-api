
from src.aws import client as aws
from src.common.config import Config

from src.model.photo import Photo


if __name__ == '__main__':

    Config.setup()

    table = aws.dynamo().create_table(**Photo.schema)
    table.meta.client.get_waiter('table_exists').wait(TableName=Photo.schema['TableName'])

    print('############')
    print('Dynamo Ready')
    print('############')
