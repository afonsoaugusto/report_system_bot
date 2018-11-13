from reportso import ReportSO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='793286572:AAGDQRwdShcrw3HCqGSqWkejiv6Fm6XmeS4')

dispatcher = updater.dispatcher
rso = ReportSO()

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

caps_handler = CommandHandler('caps', caps, pass_args=True)
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
