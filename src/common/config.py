




class Config:

    version = 'unknown'

    @classmethod
    def setup(cls):
        with open('/usr/src/dragon-api/version.cfg') as f:
            cls.version = f.read().replace('\n', '')
