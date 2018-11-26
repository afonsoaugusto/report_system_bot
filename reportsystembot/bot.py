from users import Users
from report import ReportSO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from audit import timed
from config import Config,COMMAND_NOT_FOUND,HELP,TOKEN,WELCOME
from command import CommandList


class Bot:

    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                             level=logging.INFO)
        self.config = Config()
        self.updater = Updater(token=self.config.get_config(TOKEN))
        self.dispatcher = self.updater.dispatcher
        self.filter_users = Filters.user(username=Users().get_list_users())
        self.rso = ReportSO()
        self.command_list = CommandList()

    
    def start(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.config.get_config(WELCOME))

    @staticmethod
    def echo(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    def unknown(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.config.get_config(COMMAND_NOT_FOUND))

    def help(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.rso.get_list_commands_help())

    def command(self,bot, update,args):
        bot.send_message(chat_id=update.message.chat_id, text=self.rso.get_return_command(' '.join(args)))

    def command_authorized(self,bot, update):
        report = self.rso.report(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=report)
        
    def command_authorized_paramter(self,bot, update,args):   
        command = update.message.text.split(' ')[0]
        report = self.rso.report(command,' '.join(args))
        bot.send_message(chat_id=update.message.chat_id, text=report)        

    def main(self):
        start_handler = CommandHandler('start', self.start,filters=self.filter_users)
        help_handler = CommandHandler('help', self.help,filters=self.filter_users)
        command_handler = CommandHandler('cl', self.command,pass_args=True,filters=self.filter_users)
        command_authorized_handler = CommandHandler(self.command_list.get_commands_name_without_parameter(), self.command_authorized, filters=self.filter_users)        
        command_authorized_parameter_handler = CommandHandler(self.command_list.get_commands_name_with_parameter(), self.command_authorized_paramter,pass_args=True,filters=self.filter_users)        
        echo_handler = MessageHandler(Filters.text, self.echo)
        unknown_handler = MessageHandler(Filters.command, self.unknown)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(command_handler)
        self.dispatcher.add_handler(echo_handler)
        self.dispatcher.add_handler(command_authorized_handler)
        self.dispatcher.add_handler(command_authorized_parameter_handler)                
        self.dispatcher.add_handler(unknown_handler)

        self.updater.start_polling()


if __name__ == '__main__':
    Bot().main()
