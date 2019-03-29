"""list_all module handles GET request
from client and does the work of fetching
all todos from the database"""


from src.common import standard
from src.model.todo import Todo


def list_all():

    todos = Todo.get_all()

    return standard.response(body=todos, message="Successfully retrieved todos")
