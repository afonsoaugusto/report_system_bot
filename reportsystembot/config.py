from os import environ
from argparse import ArgumentParser
from collections import ChainMap
import configparser

COMMAND_FILENAME='command_filename'
COMMAND_NOT_FOUND='messages.command_not_found'
DEFAULT={'ENVIROMENT':'DEFAULT'}
INI_PATH='config.ini'
TOKEN='token'
USER_FILENAME='user_filename'
WELCOME='messages.welcome'
HELP='messages.help'

class Config:
    def __init__(self):
        enviroment=ChainMap(environ, DEFAULT)['ENVIROMENT']
        # Processing of the INI configuration file
        ini_config = configparser.ConfigParser()
        ini_config.read(INI_PATH)
        self.defaults = ini_config[enviroment]

        parser = ArgumentParser()
        parser.add_argument('-t', '--token')

        namespace = parser.parse_args()
        linha_comando = {k: v for k, v in vars(namespace).items()
                         if v}

        self.variable = ChainMap(linha_comando, environ, self.defaults)
