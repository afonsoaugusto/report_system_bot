from users import Users
from report import ReportSO, CommandList
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from audit import timed
from config import Config,COMMAND_NOT_FOUND,HELP,TOKEN,WELCOME


class Bot:

    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                             level=logging.INFO)
        self.updater = Updater(token=Config().variable[TOKEN])
        self.dispatcher = self.updater.dispatcher
        self.filter_users = Filters.user(username=Users().get_list_users())
        self.rso = ReportSO()
        self.command_list = CommandList()

    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=Config().variable[WELCOME])

    @staticmethod
    def echo(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    @staticmethod
    def echo_command(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    @staticmethod
    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=Config().variable[COMMAND_NOT_FOUND])

    def help(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=Config().variable[HELP])

    def command(self,bot, update,args):
        bot.send_message(chat_id=update.message.chat_id, text=self.rso.get_return_command(' '.join(args)))

    def command_authorized(self,bot, update):
        report = self.rso.report(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=report)

    def main(self):
        start_handler = CommandHandler('start', self.start,filters=self.filter_users)
        help_handler = CommandHandler('help', self.help,filters=self.filter_users)
        command_handler = CommandHandler('cl', self.command,pass_args=True,filters=self.filter_users)
        command_authorized_handler = MessageHandler(Filters.command & self.filter_users, self.command_authorized)
        echo_handler = MessageHandler(Filters.text, self.echo)
        unknown_handler = MessageHandler(Filters.command, self.unknown)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(command_handler)
        self.dispatcher.add_handler(echo_handler)
        self.dispatcher.add_handler(command_authorized_handler)
        self.dispatcher.add_handler(unknown_handler)

        self.updater.start_polling()


if __name__ == '__main__':
    Bot().main()
