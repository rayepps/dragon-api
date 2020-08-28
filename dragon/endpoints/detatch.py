"""attach is the module that handles attaching
a file to a todo via the attach PUT endpoint"""

from dragon.common import standard
from dragon.model.todo import Todo
from dragon.aws.services import s3


def detatch(todo_id):

    todo = Todo.find(todo_id)

    filename = todo.attachment['filename']

    print(filename)

    s3.remove(filename)

    todo = todo.patch(dict(attachment=None))

    return standard.response(body=todo, message="Successfully detatched file from todo")
