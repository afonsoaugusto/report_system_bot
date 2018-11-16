from users import Users
from report import ReportSO, CommandList
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from audit import timed


class Bot:

    def __init__(self):
        self.logging = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                             level=logging.INFO)
        self.updater = Updater(token='793286572:AAGDQRwdShcrw3HCqGSqWkejiv6Fm6XmeS4')
        self.dispatcher = self.updater.dispatcher
        self.list_users = Filters.user(username=Users().get_list_users())
        self.rso = ReportSO()
        self.command_list = CommandList()

    @timed(logging)
    def start(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    def echo(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    def echo_command(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    def unknown(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comando nao localizado")

    def help(self,bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=self.command_list.get_commands())

    def command_authorized(self,bot, update):
        print(update.message.text)
        report = self.rso.report(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=report)

    def main(self):
        start_handler = CommandHandler('start', self.start,filters=self.list_users)
        help_handler = CommandHandler('help', self.help,filters=self.list_users)
        command_authorized_handler = MessageHandler(Filters.command & self.list_users, self.command_authorized)
        echo_handler = MessageHandler(Filters.text, self.echo)
        unknown_handler = MessageHandler(Filters.command, self.unknown)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(echo_handler)
        self.dispatcher.add_handler(command_authorized_handler)
        self.dispatcher.add_handler(unknown_handler)


        self.updater.start_polling()


if __name__ == '__main__':
    Bot().main()
