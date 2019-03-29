"""update is the module that handles updating
todos via the update PUT endpoint"""

from flask import request

from src.common import standard
from src.model.todo import Todo


def update(todo_id):

    patch = request.get_json()

    # TODO: validate & serialize user provided json

    todo = Todo.find(todo_id).patch(patch)

    return standard.response(body=todo, message="Successfully updated todo")
