"""attach is the module that handles attaching
a file to a todo via the attach PUT endpoint"""

from flask import request

from src.common import standard
from src.model.todo import Todo
from src.aws.services import s3


def attach(todo_id):

    file = request.files.get('file', None)

    if file is None:
        raise exceptions.missing_parameter.add('file')

    Todo.validate_file_type(file.filename)

    s3.upload(file.read(), file.filename)
    s3_url = s3.generate_url(file.filename)

    # TODO: validate & serialize user provided json

    todo = Todo.find(todo_id).patch(dict(file_url=s3_url))

    return standard.response(body=todo, message="Successfully attached file to todo")
