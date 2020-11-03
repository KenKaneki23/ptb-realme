import logging
import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

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
    private(update.message, "Hey, human 🤖"
                            "\nI will guide you through finding a solution."
                            "\n\nIf you face any issues with this bot, contact @pentexnyx")

    #  keyboard = [
    #       [
    #          InlineKeyboardButton("Option 1", callback_data='1'),
    #          InlineKeyboardButton("Option 2", callback_data='2'),
    #      ],
    #      [InlineKeyboardButton("Option 3", callback_data='3')],
    #  ]

    update.message.reply_text("I will ask you a few things now to find out which issue you're facing.",
                              reply_markup=InlineKeyboardMarkup.from_button(
                                  InlineKeyboardButton("Proceed ➡", callback_data='0')))


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    """Send a message when the command /help is issued."""
    html(update.message, "<u>Commands</u>"
                         "\n\n<b>/help</b>"
                         "\nDisplay this menu"
                         "\n\n<b>/admins</b>"
                         "\nShow the support group\'s staff"
                         "\n\n<b>/rules</b>"
                         "\nShow the support group\'s rules"
                         "\n\n<b>/experts</b>"
                         "\nList experts for different segments"
                         "\n\n<b>/gcam</b>"
                         "\nLatest Gcam release and configurations")


def admins(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Group's staff</u>"
                          "\n\n<b>Organization</b>"
                          "\n@aakaah00001"
                          "\n@Prashant_Choudhary"
                          "\n@PacificPC"
                          "\n\n<b>Moderators</b>"
                          "\n@pentexnyx"
                          "\n@Abhishek2376")


def experts(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Community experts</u>"
                          "\n\n<b>Software issues</b>"
                          "\n@Abhishek2376"
                          "\n@Dhairya3391"
                          "\n@pentexnyx"
                          "\n\n<b>Hardware issues</b>"
                          "\n- no expert yet -"
                          "\n\n<b>Updates and apps</b>"
                          "\n@Abhishek2376"
                          "\n@Dhairya3391"
                          "\n\n<b>Phone recommendations</b>"
                          "\n@Abhishek2376"
                          "\n@pentexnyx"
                          "\n\n<b>Flashing</b>"
                          "\n- no expert yet -"
                          "\n\n<b>Android development</b>"
                          "\n@pentexnyx"
                          "\n\n<b>Realme ecosystem</b>"
                          "\n- no expert yet -")


def gcam(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Google Camera</u>"
                          "\n\n<b>Latest Release</b>"
                          "\n<a href='https://t.me/realme_support/47467'>Urnyx05-v2.4</a>"
                          "\n\n<b>Configurations</b>")


def rules(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>Group's rules</u>"
                          "\n\n<b>1. Language</b>"
                          "\nPlease use English or Hindi as an alternative."
                          "\n\n<b>2. Links</b>"
                          "\nSending links is not permitted."
                          "\n\n<b>3. Forwarding</b>"
                          "\nForwarding messages from other channels is not permitted"
                          "\n\n<b>4. Respect</b>"
                          "\nWe're all one big community. Don't be rude."
                          "\n\n<b>5. Spam</b>"
                          "\nAvoid sending stuff multiple times. Flooding the chat won't give you more attention."
                          "\n\n<b>6. Files</b>"
                          "\nAvoid sending files over 50Mb, if not ultimately needed."
                          "\n\n<b>7. Advertisements</b>"
                          "\nSelf-promotion is not permitted."
                          "\n\n<b>8. Content</b>"
                          "\nGore, porn and anything alike is absolutely prohibited.")


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def html(message, text):
    message.reply_text(text=text, parse_mode=telegram.ParseMode.HTML)


def markdown(message, text):
    message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def html_next(message, text, button):
    message.reply_text(text=text, reply_markup=button)


def private_next(message, text, button):
    if message.chat_id > 0:
        html_next(message, text, button)
    else:
        message.reply_text("I'm shy 🤖"
                           "\nPlease talk to me in private chat:"
                           "\n@realme_community_support_bot")


def private(message, text):
    if message.chat_id > 0:
        html(message, text)
    else:
        message.reply_text("I'm shy 🤖"
                           "\nPlease talk to me in private chat:"
                           "\n@realme_community_support_bot")


def group(message, text):
    if message.chat_id == -1001374176745:
        html(message, text)
    else:
        message.reply_text("Please join the group:"
                           "\n@realme_support")


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
    dp.add_handler(CommandHandler("gcam", gcam))
    dp.add_handler(CommandHandler("experts", experts))
    dp.add_handler(CommandHandler("rules", rules))

    # on noncommand i.e message - echo the message on Telegram
    #   dp.add_handler(MessageHandler(Filters.text, echo)) yyyyyyyyyyyyyy

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
