"""module contains custom extension of the flask api application"""

from functools import wraps

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

        Here the `wraps` function is required. If we don't use it
        the handler will appear to have the name of the middleware
        function that wraps it. This will break the flask router.
        `wrap` does the work of making sure the wrapped function
        retains the correct metadata from the original handler.
        """
        for func in reversed(self.middleware.functions):
            handler = wraps(handler)(func(handler))
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
