import logging
import os
from telegram import ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from messages import *
from utils import remove_message

##########################################
# this file serves as an entry point to the program.
# here all the stuff is initialized.
##########################################

PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ.get('TOKEN')  # if you host it on Heroku, otherwise = "blablabla"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    logger.info('Bot was started by ' + update.message.from_user.name)
    update.message.reply_text("Hello! I'm a bot.\n\nUpload any document now.")


def download_document(update: Update, context: CallbackContext):
    logger.info('Downloading file.')
    update.message.reply_text("I will download this document now.")
    context.bot.get_file(update.message.document).download()  # this will download any document - not PDFs specifically


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(
        chat_id=-1001338514957,  # replace this with a group you and the bot are in
        text="<b>🤖 Affected Bot</b>\n@" + context.bot.username +
             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
        parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.document, download_document))
    #  add commands below. follow this scheme:  "command", function

    # add commands above this comment
    dp.add_error_handler(error)  # comment this line out to receive full stacktrace

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN,
                          webhook_url='https://MY-PROJECT.herokuapp.com/' + TOKEN)

    updater.start_polling()
    updater.idle()
