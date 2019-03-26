"""module contains custom extension of the flask api application"""

from flask import Flask
from flask_api import FlaskAPI


class FlaskDragon(FlaskAPI):
    """FlaskDragon adds the ability to insert middleware into each request and
    setup routes more easily"""

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
        """wrap handler will take the handler and iterate every
        middleware decorator - decorating the handler function in
        the middleware function

        the `og_func_name` is used to save the name of the original
        handler function and reapply it to the final wrapped function.
        Otherwise - flask freaks out because it sees the middleware
        funcs as the handler and they are all named the same to flask.
        """
        og_func_name = handler.__name__
        for func in reversed(self.middleware.functions):
            handler = func(handler)
        handler.__name__ = og_func_name
        return handler

class Middleware:
    """Middleware is a simple collection style class that
    keeps track of the middleware functions for an application.
    Each `function` should be a decorator where the handler is
    passed in and the wrapping function is returned."""

    def __init__(self):
        self.functions = []

    def add(self, func):
        self.functions.append(func)
