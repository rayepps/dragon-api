"""list_all module handles GET request
from client and does the work of fetching
all todos from the database"""


from dragon.common import standard
from dragon.model.todo import Todo


def list_all():

    todos = Todo.get_all()

    return standard.response(body=todos, message="Successfully retrieved todos")
