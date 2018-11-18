from os import environ
from argparse import ArgumentParser
from collections import ChainMap
import configparser

TOKEN='token'
DEFAULT='DEFAULT'
INI_PATH='config.ini'

class Config:
    def __init__(self):
        # Processing of the INI configuration file
        ini_config = configparser.ConfigParser()
        ini_config.read(INI_PATH)
        self.defaults = ini_config[DEFAULT]

        parser = ArgumentParser()
        parser.add_argument('-t', '--token')

        namespace = parser.parse_args()
        linha_comando = {k: v for k, v in vars(namespace).items()
                         if v}

        self.variable = ChainMap(linha_comando, environ, self.defaults)
