from operator import itemgetter
import subprocess

try:
    from config import Config, COMMAND_FILENAME
except:
    from .config import Config, COMMAND_FILENAME

class Command:
    def __init__(self, name, parameters=None, desc_help=None):
        self.name = name
        self.parameters = parameters
        self.desc_help = desc_help

    def execute(self):
        p = subprocess.Popen(self.generate_command(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout.readlines()

    def generate_command(self):
        if None == self.parameters:
            return self.name

        dirty_parameters = [p.strip() for p in self.parameters]
        parameters = ' '.join(dirty_parameters)
        comamnd = ' '.join([self.name,parameters])
        return comamnd

    def generate_command_help(self):
        if None == self.desc_help:
            return self.generate_command()

        help = '\n\t -'.join(['/'+self.generate_command(),self.desc_help.strip()])
        return help

class CommandList:

    def __init__(self):
        self.list_commands = self.get_commands()

    @staticmethod
    def clear_command(command_name):
        if '/' == command_name[0]:
            command_name = command_name[1:]
        return command_name;

    def get_command(self,command_name):
        command_name = self.clear_command(command_name)
        for command in self.list_commands:
            if command.name.lower() == command_name.lower():
                return command
        return 'Comando não encontrado'

    def is_command_valid(self,command_name, parameters=None):
        command_name = self.clear_command(command_name)
        if not parameters:
            return self.is_command_valid_without_parameters(command_name)
        else:
            return self.is_command_valid_with_parameters(command_name,parameters)
        
    def is_command_valid_without_parameters(self,command_name):
        for command in self.list_commands:
            if command.name.lower() == command_name.lower() and not command.parameters:
                return True
        return False        
        
    def is_command_valid_with_parameters(self,command_name, parameters):
        for command in self.list_commands:
            if command.name.lower() == command_name.lower() and len(command.parameters)>0:
                return True
        return False                

    @staticmethod
    def _split_string_to_command(line):
        name, parameters, help = line.split('\t')
        return Command(name,parameters, help)

    def get_commands(self):
        with open(Config().variable[COMMAND_FILENAME],'r') as file:
            commands = file.readlines()

        return [self._split_string_to_command(c) for c in commands]

    def get_commands_name_without_parameter(self):
        commands = self.get_commands()
        return [c.name for c in commands if not c.parameters]
        
    def get_commands_name_with_parameter(self):
        commands = self.get_commands()
        return [c.name for c in commands if len(c.parameters) > 0]        
        
    def get_commands_text(self):
        commands = self.get_commands()
        return '\n'.join([c.generate_command() for c in commands])

    def get_commands_text_help(self):
        commands = self.get_commands()
        return '\n\n'.join([c.generate_command_help() for c in commands])
