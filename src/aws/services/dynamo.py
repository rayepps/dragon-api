"""dynamo service provides a single source interface for
interacting with dynamo via the boto3 dynamo resource

similar to a so called repository
in the repository pattern
"""

from src.aws import client as aws


LETTERS = [chr(l) for l in range(97, 123)]

def update(table_name, key, attributes):
    metas = build_update_metadata(attributes)
    dynamo = aws.dynamo()
    table = dynamo.Table(table_name)
    result = table.update_item(
        Key=key,
        UpdateExpression=build_update_expression(metas),
        ExpressionAttributeValues=build_expression_attributes(metas),
        ReturnValues="UPDATED_NEW")

    return result['Attributes']

def delete(table_name, key):
    dynamo = aws.dynamo()
    table = dynamo.Table(table_name)

    return table.delete_item(Key=key)

def add(table_name, attributes):
    dynamo = aws.dynamo()
    table = dynamo.Table(table_name)

    table.put_item(Item=attributes)

def find(table_name, key):
    dynamo = aws.dynamo()
    table = dynamo.Table(table_name)

    res = table.get_item(Key=key)

    return res['Item'] if 'Item' in res else None

def scan(table_name):
    dynamo = aws.dynamo()
    table = dynamo.Table(table_name)

    return table.scan()['Items']


def build_update_metadata(attributes):
    if len(attributes) > len(LETTERS):
        pass # TODO: raise an exception

    return [UpdateMeta(key, f':{LETTERS[i]}', attributes[key]) for i, key in enumerate(attributes)]

def build_update_expression(metas):
    expressions = ', '.join([f'{meta.name} = {meta.key}' for meta in metas])

    return f'set {expressions}'

def build_expression_attributes(metas):
    values = {}
    for meta in metas:
        values[meta.key] = meta.value

    return values

class UpdateMeta:
    def __init__(self, name, key, value):
        self.name = name
        self.key = key
        self.value = value
