"""find module handles GET requests from
the client and does the work of finding
the specified todo and returning its
metadata"""

from dragon.common import standard

from dragon.model.todo import Todo


def find(todo_id):

    todo = Todo.find(todo_id)

    return standard.response(body=todo, message=f'Successfully retrieved todo: {todo_id}')
