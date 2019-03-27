
from src.aws import client as aws
from src.common.config import Config
from src.common import constants


if __name__ == '__main__':

    Config.setup()

    aws.ssm().put_parameter(
        Name='/dragon/api/apikey',
        Value='localhashkey',
        Type='String')

    print('############')
    print('SSM Ready')
    print('############')
