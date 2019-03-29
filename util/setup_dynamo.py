
from src.aws import client as aws
from src.common.config import Config
from src.model.todo import Todo


if __name__ == '__main__':

    Config.setup()

    table = aws.dynamo().create_table(**Todo.schema)
    table.meta.client.get_waiter('table_exists').wait(TableName=Todo.table())

    print('############')
    print('Dynamo Ready')
    print('############')
