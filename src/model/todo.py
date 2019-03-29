"""todo model module contains the logic for handling,
manipulating, storing, etc. todo objects"""

import uuid

from werkzeug.utils import secure_filename

from src.common.types import JsonSerializable
from src.common import exceptions
from src.common import constants
from src.aws.services import dynamo, s3


class Todo(JsonSerializable):

    schema = dict(
        TableName='dragon-todos',
        KeySchema=[
            {
                'AttributeName': 'todo_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'todo_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        })

    def __init__(self, data):
        store = dict(
            todo_id=data.get('todo_id', uuid.uuid4().hex),
            is_starred=data.get('is_starred'),
            title=data.get('title'),
            deadline=data.get('deadline'),
            file_url=data.get('file_url'))
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
        return Todo.schema['TableName']

    def save(self):

        data = {}

        for key, val in self.store.items():
            if val is not None and val != '':
                data[key] = val

        dynamo.add(table_name=Todo.table(), attributes=data)

    def patch(self, patch_obj):

        patch_else_store = lambda prop: patch_obj[prop] if prop in patch_obj else self.store[prop]

        result = dynamo.update(
            table_name=Todo.table(),
            key={
                'todo_id': self.store['todo_id']
            },
            attributes={
                'title': patch_else_store('title'),
                'is_starred': patch_else_store('is_starred'),
                'deadline': patch_else_store('deadline'),
                'file_url': patch_else_store('file_url')
            })

        return Todo(result)

    def delete(self):

        result = dynamo.delete(
            table_name=Todo.table(),
            key={
                'todo_id': self.store['todo_id']
            })

        return result

    @classmethod
    def find(cls, todo_id):
        result = dynamo.find(table_name=Todo.table(), key={
            'todo_id': todo_id
        })

        return Todo(result)

    @classmethod
    def get_all(cls):
        result = dynamo.scan(table_name=Todo.table())

        return [Todo(item) for item in result]
