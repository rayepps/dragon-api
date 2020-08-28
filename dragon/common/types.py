"""types exposes objects useful for creating
more dynamic and seralizable data"""


class Dynamic:
    """Dynamic overrides the build in python
    __getattr__ and __setattr__ methods allowing
    you to arbitrarially get and set data on an
    instance of this class."""

    STORE_KEY = '_store'

    def __init__(self, obj_dict=None):
        # Create our own storage object where we keep track of all the
        # properties we add. This allows us to pull _only_ our properties
        # when we want to know what we have added to our class without
        # pulling builtin attributes
        self.__dict__[self.STORE_KEY] = {}
        obj_dict = obj_dict or {}

        # Seed the store object with and properties
        # passed to the initalizer
        for key, val in obj_dict.items():
            setattr(self, key, val)

    def __getattr__(self, name):
        if name in self.store:
            return self.store[name]
        return None

    def __setattr__(self, name, value):
        self.store[name] = value

    @property
    def store(self):
        return self.__dict__[self.STORE_KEY]

class JsonSerializable(Dynamic):
    """JsonSerializable builds off the Dynamic class
    and also implements a `serialize` method that can
    be used to configure custom serialization in the
    `json.dumps` method. This allows you to write DTO
    objects that extend this class and have their properties
    be easily seralized"""

    def __init__(self, obj=None):
        super().__init__(obj)

    @staticmethod
    def serialize(obj):
        if isinstance(obj, JsonSerializable):
            return obj.json
        return str(obj)

    @property
    def json(self):
        return self.store
