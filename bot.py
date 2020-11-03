import logging
import os

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! 3')


def help(update, context):
    """Send a message when the command /help is issued."""
    text = "*Commands*" + \
           "\n\n*/help*" + \
           "\nDisplay this menu" + \
           "\n\n*/admins*" + \
           " \nShow the support group\'s staff" + \
           "\n\n*/experts*" + \
           "\nList experts for different segments"

    markdown(update, text)


def admins(update, context):
    """Send a message when the command /admins is issued."""
    text_admins = '*Group\'s staff*' + \
                  '\n\nOrganization' + \
                  '\n@aakaah00001' + \
                  '\n@Prashant_Choudhary' + \
                  '\n@PacificPC' + \
                  '\n\nModerators' + \
                  '\n@pentexnyx' + \
                  '\n@Abhishek2376 '

    text = "*Commands*" + \
           "\n\n*/help*" + \
           "\nDisplay this menu" + \
           "\n\n*/admins*" + \
           "\nShow the support group\'s staff" + \
           "\n\n*/experts*" + \
           "\nList experts for different segments"

    if update.message.chat_id == -337823911:
        update.message.reply_text(text=text_admins, parse_mode=telegram.ParseMode.MARKDOWN_V2)
    else:
        update.message.reply_text('Please join the group.')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def markdown(update, text):
    update.message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def check(update, text):
    if update.message.chat_id == -337823911:
        markdown(update, text)
    else:
        update.message.reply_text('Please join the group.')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("admins", admins))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://pxnx-tg-bot-test.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
