"""todo model module contains the logic for handling,
manipulating, storing, etc. todo objects"""

import uuid

from dragon.common.types import JsonSerializable
from dragon.common import exceptions
from dragon.common import constants
from dragon.aws.services import dynamo


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
            attachment=data.get('attachment'))
        super().__init__(store)

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
                'attachment': patch_else_store('attachment')
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

        if result is None:
            raise exceptions.entity_not_found.add(f'todo_id: {todo_id}')

        return Todo(result)

    @classmethod
    def get_all(cls):
        result = dynamo.scan(table_name=Todo.table())

        return [Todo(item) for item in result]
