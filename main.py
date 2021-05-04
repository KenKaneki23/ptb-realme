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
TOKEN = os.environ.get('TOKEN')
OFFTOPIC_GROUP = -1001415779011
GROUP = -1001374176745  # -1001327617858 for test group
VERIFIED_USERS = (703453307,  # Nyx
                  1038099761,  # Abhiskek
                  984010225  # Phoenix
                  )

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(-1001338514957,
                             "<b>🤖 Affected Bot</b>\n@" + context.bot.username +
                             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
                             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
                             ParseMode.HTML)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(
        Filters.text(["/help@CoronaVirusRobot", "/victims@CoronaVirusRobot", "/infect@CoronaVirusRobot"]),
        remove_message))

    dp.add_handler(CommandHandler("android11", android11, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("gcam", gcam, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("cleaners", cleaners, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("help", commands, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("files", files, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("admins", admins, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("experts", experts, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("ask", ask, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("form", form, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("date", date, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("offtopic", offtopic, Filters.chat(GROUP) & Filters.user(VERIFIED_USERS)))
    dp.add_handler(CommandHandler("polls", polls, Filters.user(VERIFIED_USERS)))

    dp.add_handler(MessageHandler(Filters.chat_type.private, private_not_available))
    #  add commands below. follow this scheme:  "command", function

    # add commands above this comment
  #  dp.add_error_handler(error)

    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://ptb-realme.herokuapp.com/' + TOKEN)

    updater.start_polling()
    updater.idle()
