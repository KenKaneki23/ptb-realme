import logging
import os
import re

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

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
    private_next(update.message,
                 "Hey, human 🤖"
                 "\nI will guide you through finding a solution."
                 "\n\nPlease provide as many details as possible for every question to make it easier for the "
                 "community to understand your problem and give you a better answer quicker. "
                 "\n\nIf you face any issues with this bot, contact @pentexnyx",
                 InlineKeyboardButton("Proceed ➡", callback_data='1'))


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    position = int(query.data)
    proceed_button = InlineKeyboardButton("Next ➡", callback_data=str(position + 1))

    if position == 0:
        message_text = "Hey, human 🤖" \
                       "\nI will guide you through finding a solution." \
                       "\n\nPlease provide as many details as possible for every question to make it easier for the " \
                       "community to understand your problem and give you a better answer quicker." \
                       "\n\nIf you face any issues with this bot, contact @pentexnyx"

        query.edit_message_text(text=message_text, reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("Proceed ➡", callback_data='1')))
        return

    elif position == 1:
        message_text = "Question 1" \
                       "\n\nWhich device are you using?"

    elif position == 2:
        message_text = "Question 2" \
                       "\n\nWhich software update is installed?"

    elif position == 3:
        message_text = "Question 3" \
                       "\n\nWhat do you want to do?"

    elif position == 4:
        message_text = "Question 4" \
                       "\n\nWhat have you tried already?"

    elif position == 5:
        message_text = "Question 5" \
                       "\n\nWhy do you want to do that?"

    elif position == 6:
        message_text = "Question 6" \
                       "\n\nWhat benefits do you expect?"

    elif position == 7:
        message_text = "Question 7" \
                       "\n\nWhat output did you get?"

    else:
        message_text = "Thanks for your time. 🤖" \
                       "\n\nNow ask in the community support group."

        proceed_button = InlineKeyboardButton("Join »", url="https://t.me/realme_support")

    buttons = InlineKeyboardMarkup.from_row(
        [InlineKeyboardButton("⬅ Back", callback_data=str(position - 1)), proceed_button])

    query.edit_message_text(text=message_text, reply_markup=buttons)


def ask(update, context):
    """Send a message when the command /help is issued."""
    group_button_html(update.message, "<u>How to ask</u>"
                                      "\n\n<b>1. Formulate the question</b>"
                                      "\nMake sure to include:"
                                      "\n· Which device you are using"
                                      "\n· Which software update is installed"
                                      "\n· What you want to do"
                                      "\n· What you have tried already"
                                      "\n· Why you want to do that"
                                      "\n· What benefits you expect from it"
                                      "\n· What output you got"
                                      "\n\n<b>2. Wait for a response</b>"
                                      "\nGive the community 48h to answer your question. The needed expert might not "
                                      "available all the time, so receiving an answer might take a bit. "
                                      "\n\n<b>3. No answer yet</b>"
                                      "\nUse /experts and tag the experts, whose segment fits your issue."
                                      "\nIf you didn't receive an answer after a week, use /form and fill out the "
                                      "linked form. "
                                      "\n\nThese suggestions enable us to provide you with better answers quicker and "
                                      "will keep this chat more focused.",
                      InlineKeyboardMarkup.from_button(
                          InlineKeyboardButton(text="Message me 💬",
                                               url="https://t.me/realme_community_support_bot?start=0")))


def offtopic(update, context):
    """Send a message when the command /help is issued."""
    html(update.message, "Will reply to continue in offtopic group and move message to it")


def help(update, context):
    """Send a message when the command /help is issued."""
    html(update.message, "<u>Commands</u>"
                         "\n\n<b>/help</b>"
                         "\nDisplay this message"
                         "\n\n<b>/admins</b>"
                         "\nShow this group\'s staff"
                         "\n\n<b>/rules</b>"
                         "\nShow this group\'s rules"
                         "\n\n<b>/experts</b>"
                         "\nList experts for different segments"
                         "\n\n<b>/gcam</b>"
                         "\nLatest GCam release and configurations"
                         "\n\n<b>/ask</b>"
                         "\nHow to ask questions properly")


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
                          "\n@Abhishek2376"
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
                          "\n· <a href='https://t.me/realme_support/47467'>Urnyx05-v2.4</a>"
                          "\n\nUrnyx05's releases work well on most Realme devices. Take a look at @googlecameraport "
                          "for other releases. "
                          "\n\n\n<b>Configurations</b>"
                          "\n· <a href='https://t.me/realme_support/20129'>new-natural</a>"
                          "\n· <a href='https://t.me/realme_support/20127'>X2 Pro terev</a>"
                          "\n\nTo enable these configurations, place them in <b>Internal Storage > GCam > Configs7</b>."
                          "\n\nThen go to your GCam and press on the bottom left (next to the camera switch button) a "
                          "few times. A dialog should appear where your can select the desired configuration. "
                          "\n\nFeel free to fiddle around with LibPatcher (in GCam's settings) a little to "
                          "shape the image output so that it fits your needs.")


def sdmaid(update, context):
    """Send a message when the command /admins is issued."""
    group(update.message, "<u>SD Maid</u>"
                          "\n\n<b>Latest Release - AVAILABLE SOON</b>"
                          "\n· <a href='https://t.me/realme_support/47467'>- placeholder -</a>"
                          "\n\nSD Maid is an excellent cleaning app, which also takes care of Databases, "
                          "duplicates, caches and enables you to freeze the apps you don't need.")


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


def form(update, context):
    url_button(update.message,
               "If your issue is not resolved by the community after a week, you can also contact the developers."
               "\n\nPlease don't abuse this possibility, so that Realme developers can focus on developing.",
               "Access form 📝",
               "https://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2-VGJasy8VU_BLsFA/viewform")


def android11(update, context):
    """Echo the user message."""
    html(update.message,
         "<u>Realme UI 2.0</u>"
         "\n\n<a href='https://static.c.realme.com/IN/wm-thread/1323470129358438400.jpg'>Official Roadmap</a>"
         "\n\nPlease note that the timeline is for the first wave of early access rollout only. The Early Access "
         "version for the corresponding model will be released within the above mentioned month in batches, "
         "not at the beginning of the month. The stable version will be pushed to all users over a period of time."
         "\n\nRelax and wait what happens 😎")


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def nice(update, context):
    """Echo the user message."""
    update.message.reply_text("nice")


global reply_message
global replied_message


def when_update(update, context):
    """Echo the user message."""
    #  update.message.reply_text("Just wait a few days 😊")

    #  u = Updater(TOKEN, use_context=True)
    #  j = update.job_queue
    # j.run_once(callback_30(update.message, context), 10)

    # might require bot to be admin
    # update.message.delete()

    reply_message = update.message.reply_text("Just wait a few days 😊")
    replied_message = update.message.message_id

    chat_id = update.message.chat_id
    context.job_queue.run_once(alarm,
                               10,
                               context=chat_id, name=str(update.message.message_id))


# (reply_message=update.message, replied_message=reply, context=context)
# ,name=str(chat_id)

def alarm(context):
    # replied_message, reply_message,

    """Send the alarm message."""
    #  job = context.job
    #  context.bot.delete_message(job.context)

    # time.sleep(10)

    job = context.job

    #  context.bot.delete_message(context=job.context, message_id=replied_message.message_id)
    #  context.bot.delete_message(context=job.context, message_id=reply_message.message_id)

    context.bot.delete_message(context=job.context, message_id=job.name)
    context.bot.delete_message(context=job.context, message_id=str(int(job.name) + 1))


# context.bot.delete_message(message_id=)

# replied_message.delete()
# reply_message.delete()


#  context.bot.delete_message(chat_id=message.chat_id,message_id=message.message_id)


###


def html(message, text):
    message.reply_text(text=text, parse_mode=telegram.ParseMode.HTML)


def markdown(message, text):
    message.reply_text(text=text, parse_mode=telegram.ParseMode.MARKDOWN_V2)


def url_button(message, text, button_text, button_url):
    message.reply_text(text,
                       reply_markup=InlineKeyboardMarkup.from_button(
                           InlineKeyboardButton(text=button_text, url=button_url)))


def private_next(message, text, message_button):
    if message.chat_id > 0:
        message.reply_text(text, reply_markup=InlineKeyboardMarkup.from_button(message_button))
    else:
        url_button(message, "I'm shy 🤖", "Message me 💬", "https://t.me/realme_community_support_bot?start=0")


def private(message, text):
    if message.chat_id > 0:
        html(message, text)
    else:
        url_button(message, "I'm shy 🤖", "Message me 💬", "https://t.me/realme_community_support_bot?start=0")


# "\nPlease talk to me in private chat:"
#                           "\n@realme_community_support_bot"

def group(message, text):
    if message.chat_id == -1001374176745:
        html(message, text)
    else:
        url_button(message,
                   "Command can only be used in the community support group.",
                   "Join »",
                   "https://t.me/realme_support")


def group_button_html(message, text, reply_markup):
    if message.chat_id == -1001374176745:
        message.reply_text(text=text, parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)
    else:
        url_button(message,
                   "Command can only be used in the community support group.",
                   "Join »",
                   "https://t.me/realme_support")


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
    dp.add_handler(CommandHandler("sdmaid", sdmaid))
    dp.add_handler(CommandHandler("experts", experts))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("ask", ask))
    dp.add_handler(CommandHandler("android11", android11))
    dp.add_handler(CommandHandler("offtopic", offtopic))
    dp.add_handler(CommandHandler("form", form))

    # on noncommand i.e message - echo the message on Telegram
    #   dp.add_handler(MessageHandler(Filters.text, echo)) yyyyyyyyyyyyyy

    dp.add_handler(MessageHandler(Filters.regex(re.compile("when(.*?)update", re.IGNORECASE)), when_update))

    dp.add_handler(MessageHandler(Filters.regex("69"), nice))

    dp.add_handler(CallbackQueryHandler(button))

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
