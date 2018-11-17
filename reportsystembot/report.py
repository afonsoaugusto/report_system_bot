try:
    from base.command import Command
    from base.command import CommandList
except:
    from .base.command import Command
    from .base.command import CommandList

class ReportSO:

    def __init__(self):
        self.command_list = CommandList()
        pass

    @staticmethod
    def get_return_command(command):
        return_command = Command(command).execute()
        return FormatText(return_command).format()

    def report(self,name_command):
        command_text = self.command_list.get_command(name_command)
        return_command = Command(command_text).execute()
        return FormatText(return_command).format()

class FormatText:

    def __init__(self,text):
        self.text = text

    def format(self):
        if len(self.text) == 0:
            return ''
        elif len(self.text) == 1:
            return self.text[0].decode("utf-8").replace('\n','')
        else:
            re_text = []
            for phrase in self.text:
                re_text.append(phrase .decode("utf-8"))
            re_text[len(re_text)-1] = re_text[len(re_text)-1].replace('\n','')
            return ''.join(re_text)
