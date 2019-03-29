"""attach is the module that handles attaching
a file to a todo via the attach PUT endpoint"""

from flask import request

from werkzeug.utils import secure_filename

from src.common import standard
from src.common import exceptions
from src.model.todo import Todo
from src.aws.services import s3


def attach(todo_id):

    file = request.files.get('file', None)

    if file is None:
        raise exceptions.missing_parameter.add('file')

    Todo.validate_file_type(file.filename)
    filename = secure_filename(file.filename)

    s3.upload(file.read(), filename)
    s3_url = s3.generate_url(filename)

    todo = Todo.find(todo_id).patch(dict(attachment=dict(
        s3_url=s3_url,
        filename=filename)))

    return standard.response(body=todo, message="Successfully attached file to todo")
