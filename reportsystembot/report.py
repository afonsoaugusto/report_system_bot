try:
    from command import Command
    from command import CommandList
except ImportError:
    from .command import Command
    from .command import CommandList

class ReportSO:

    def __init__(self):
        self.command_list = CommandList()

    @staticmethod
    def get_return_command(command):
        return_command = Command(command).execute()
        return FormatText(return_command).format()

    def report(self,command,parameters=None):
        name_command = command.lower()
        if self.command_list.is_command_valid(name_command,parameters):
            command_clear = self.command_list.clear_command(name_command)
            return_command = Command(command_clear,parameters=parameters).execute()
            return FormatText(return_command).format()
        else:
            return 'Comando não valido.\nConsulte a ajuda com /help'            

    def get_list_commands(self):
        return self.command_list.get_commands_text()

    def get_list_commands_help(self):
        return self.command_list.get_commands_text_help()

class FormatText:

    def __init__(self,text):
        self.text = text

    def format(self):
        if len(self.text) == 0:
            return ''
        elif len(self.text) == 1:
            return self.text[0].decode("utf-8").replace('\n','')
        else:
            re_text = [phrase .decode("utf-8") for phrase in self.text]
            re_text[len(re_text)-1] = re_text[len(re_text)-1].replace('\n','')
            return ''.join(re_text)
