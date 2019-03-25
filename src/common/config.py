




class Config:

    version = 'unknown'
    upload_folder = '/tmp'
    s3_bucket_name = 'dragon-photo-storage'

    @classmethod
    def setup(cls):
        with open('/usr/src/dragon-api/version.cfg') as f:
            cls.version = f.read().replace('\n', '')
