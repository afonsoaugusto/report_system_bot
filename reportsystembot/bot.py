from users import Users
from report import ReportSO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

rso = ReportSO()
    
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def uname(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=rso.get_uname())

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
def command(bot, update, args):
    command_args = args
    bot.send_message(chat_id=update.message.chat_id, text=rso.get_return_command(command_args))

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Comando nao localizado")

def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    
    updater = Updater(token='793286572:AAGDQRwdShcrw3HCqGSqWkejiv6Fm6XmeS4')
    dispatcher = updater.dispatcher
    
    command_handler = CommandHandler('command', command,filters=Filters.user(username=Users().get_list_users()), pass_args=True)
    start_handler = CommandHandler('start', start,filters=Filters.user(username=Users().get_list_users()))
    uname_handler = CommandHandler('uname', uname,filters=Filters.user(username=Users().get_list_users()))
    echo_handler = MessageHandler(Filters.text, echo)
    unknown_handler = MessageHandler(Filters.command, unknown)
    
    dispatcher.add_handler(uname_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(command_handler)
    dispatcher.add_handler(echo_handler)    
    dispatcher.add_handler(unknown_handler)
    
    updater.start_polling()


if __name__ == '__main__':
    main()