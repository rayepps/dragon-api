

from flask import Flask
from flask_api import FlaskAPI


class FlaskDragon(FlaskAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.middleware = Middleware()

    def add_short_route(self, endpoint, handler, method):
        self.add_url_rule(endpoint, view_func=self.wrap_handler(handler), methods=[method])

    def get(self, endpoint, handler):
        self.add_short_route(endpoint, handler, 'GET')

    def post(self, endpoint, handler):
        self.add_short_route(endpoint, handler, 'POST')

    def put(self, endpoint, handler):
        self.add_short_route(endpoint, handler, 'PUT')

    def delete(self, endpoint, handler):
        self.add_short_route(endpoint, handler, 'DELETE')

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
