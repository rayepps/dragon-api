"""upload is the module that handles file
uploads via the upload POST endpoint"""

from flask import request

from src.common import standard
from src.model.todo import Todo


def create():

    todo_data = request.get_json()

    # TODO: Validate & sanatize post data

    todo = Todo(dict(title=todo_data.get('title')))

    todo.save()

    return standard.response(body=todo, message="Successfully created todo")
