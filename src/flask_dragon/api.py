

from flask import Flask


class FlaskDragon(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.middleware = Middleware()

    def get(self, endpoint, handler):
        self.add_url_rule(endpoint, view_func=self.wrap_handler(handler), methods=['GET'])

    def post(self, endpoint, handler):
        self.add_url_rule(endpoint, view_func=self.wrap_handler(handler), methods=['POST'])

    def wrap_handler(self, handler):
        og_func_name = handler.__name__
        for func in self.middleware.functions:
            handler = func(handler)
        handler.__name__ = og_func_name
        return handler

class Middleware:

    def __init__(self):
        self.functions = []

    def add(self, func):
        self.functions.append(func)
