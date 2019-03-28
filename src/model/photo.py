"""photo model module contains the logic for handling,
manipulating, storing, etc. photo objects"""

import uuid

from werkzeug.utils import secure_filename

from src.common.types import JsonSerializable
from src.common import exceptions
from src.common import constants
from src.aws.services import dynamo, s3


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
            photo_id=data.get('photo_id', uuid.uuid4().hex),
            filename=data.get('filename'),
            title=data.get('title'),
            photo_url=data.get('photo_url'),
            description=data.get('description'),
            thumbnail_url=data.get('thumbnail_url'))
        super().__init__(store)

    @classmethod
    def upload(cls, file):
        """uploads a file to s3 (does not save it locally)
        @param file: werkzeug.datastructures.FileStorage
        @return str: A string with the full s3 path to the file
        """

        filename = secure_filename(file.filename)

        s3.upload(data=file.read(), filename=filename)

        return s3.generate_url(filename)

    @classmethod
    def validate_file_type(cls, filename):
        is_valid = '.' in filename and filename.rsplit('.', 1)[1].lower() in constants.FILE_TYPE_WHITELIST
        if not is_valid:
            raise exceptions.invalid_file_type.add(filename)

    @classmethod
    def table(cls):
        return Photo.schema['TableName']

    def save(self):

        data = {}

        for key, val in self.store.items():
            if val is not None and val != '':
                data[key] = val

        dynamo.add(table_name=Photo.table(), attributes=data)

    def patch(self, patch_obj):

        patch_else_store = lambda prop: patch_obj[prop] if prop in patch_obj else self.store[prop]

        result = dynamo.update(
            table_name=Photo.table(),
            key={
                'photo_id': self.store['photo_id']
            },
            attributes={
                'title': patch_else_store('title'),
                'description': patch_else_store('description'),
                'photo_url': patch_else_store('photo_url'),
                'thumbnail_url': patch_else_store('thumbnail_url'),
                'filename': patch_else_store('filename')
            })

        return Photo(result)

    def delete(self):

        result = dynamo.delete(
            table_name=Photo.table(),
            key={
                'photo_id': self.store['photo_id']
            })

        return result

    @classmethod
    def find(cls, photo_id):
        result = dynamo.find(table_name=Photo.table(), key={
            'photo_id': photo_id
        })

        return Photo(result)

    @classmethod
    def get_all(cls):
        result = dynamo.scan(table_name=Photo.table())

        return [Photo(item) for item in result]
