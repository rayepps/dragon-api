import sys
import os
import argparse
import yaml


def build_parameters(version):

    pwd = os.path.dirname(os.path.realpath(__file__))

    with open(f'{pwd}/../cloudformation/parameters.yml', 'r') as param_yaml:
        try:
            params = yaml.load(param_yaml)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)

    params['DockerImageTag'] = version

    param_str = ''
    for key, val in params.items():
        param_str = f'{param_str} {key}={val}'

    return param_str


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Build cloud formation stack parameters for deployment')
    parser.add_argument('-v', '--version', help='A string specifying the source version to be set in the parameters. Ex. 0.1.2')
    args = parser.parse_args()

    parameters = build_parameters(args.version)

    print(parameters)
