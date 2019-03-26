
import uuid

from src.dal.dynamo import get_dynamo
from src.common.config import Config
from src.common.types import JsonSerializable

class Photo(JsonSerializable):

    schema = dict(
        TableName='dragon-photos',
        KeySchema=[
            {
                'AttributeName': 'photo_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'photo_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        })

    def __init__(self, data):
        store = dict(
            photo_id = data.get('photo_id', uuid.uuid4().hex),
            filename = data.get('filename'),
            title = data.get('title'),
            photo_url = data.get('photo_url'),
            description = data.get('description'),
            thumbnail_url = data.get('thumbnail_url'))
        super().__init__(store)

    @classmethod
    def table(cls):
        return get_dynamo(Config.exec_env).Table(Photo.schema['TableName'])

    def save(self):

        data = {}

        for key, val in self.store.items():
            if val is not None and val != '':
                data[key] = val

        res = Photo.table().put_item(Item=data)

    def patch(self, patch_obj):

        patch_else_store = lambda prop: patch_obj[prop] if prop in patch_obj else self.store[prop]

        response = Photo.table().update_item(
            Key={
                'photo_id': self.store['photo_id']
            },
            UpdateExpression="set title = :t, description = :d, photo_url = :p, thumbnail_url = :n, filename = :f",
            ExpressionAttributeValues={
                ':t': patch_else_store('title'),
                ':d': patch_else_store('description'),
                ':p': patch_else_store('photo_url'),
                ':n': patch_else_store('thumbnail_url'),
                ':f': patch_else_store('filename')
            },
            ReturnValues="UPDATED_NEW")

        return Photo(response['Attributes'])

    def delete(self):
        response = Photo.table().delete_item(
            Key={
                'photo_id': self.store['photo_id']
            })

        print('DELETE RESPONSE')
        print(response)

        return response

    @classmethod
    def find(cls, id):
        response = Photo.table().get_item(
            Key={
                'photo_id': id
            })

        return Photo(response['Item'])

    @classmethod
    def get_all(cls):
        response = Photo.table().scan()

        return [Photo(item) for item in response['Items']]
