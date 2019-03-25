import json


class Dynamic:
    STORE_KEY = '_store'
    def __init__(self, obj_dict=None):
        self.__dict__[self.STORE_KEY] = {}
        obj_dict = obj_dict or {}
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
    @staticmethod
    def serialize(obj):
        if isinstance(obj, JsonSerializable):
            return obj.json
        else:
            return str(obj)
    def __init__(self, obj=None):
        super().__init__(obj)
    @property
    def json(self):
        return self.store
