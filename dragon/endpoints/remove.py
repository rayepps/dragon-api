"""remove module handles DELETE requests
from the client and does the work of
finding the specified todos and deleting
it from the database"""

from dragon.common import standard

from dragon.model.todo import Todo


def remove(todo_id):

    Todo.find(todo_id).delete()

    return standard.response(body=f'Successfully removed todo: {todo_id}')
