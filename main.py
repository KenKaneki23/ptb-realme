import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from messages import *
from postgres import PostgresPersistence
from utils import remove_message

##########################################
# this file serves as an entry point to the program.
# here all the stuff is initialized.
##########################################

PORT = int(os.environ.get('PORT', 5000))
DATABASE_URL = os.environ['DATABASE_URL']
TOKEN = os.environ['TOKEN']

OFFTOPIC_GROUP = -1001415779011
GROUP = -1001374176745  # -1001327617858 for test group

ADMINS = (703453307,  # Nyx
          984010225  # Phoenix
          )
VERIFIED_USERS = ADMINS + (
    92429516,  # Lucky
    1038099761  # Abhiskek
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start_session() -> scoped_session:
    engine = create_engine(  # "postgresql://blpxjuiwemaqpm"
        # ":4c9a03691098bb7a6f615d510652c7c355b030da52e24b2cb48653a145082205@ec2-54-220-35-19.eu"
        # "-west-1.compute.amazonaws.com:5432/dcu1jgmr7u3uv3"
        str(os.environ["DATABASE_URL"])  # mehh
        , client_encoding="utf8")
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(-1001338514957,
                             "<b>🤖 Affected Bot</b>\n@" + context.bot.username +
                             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
                             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
                             ParseMode.HTML)


if __name__ == '__main__':
    session = start_session()
    updater = Updater(TOKEN, persistence=PostgresPersistence(session), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(
        Filters.text(["/help@CoronaVirusRobot", "/victims@CoronaVirusRobot", "/infect@CoronaVirusRobot"]),
        remove_message))  # gg

    dp.add_handler(CommandHandler("android11", android11, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("gcam", gcam, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("cleaners", cleaners, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("help", commands, Filters.chat(GROUP)))
    # dp.add_handler(CommandHandler("files", files, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("admins", admins, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("experts", experts, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("debloat", debloat, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("ask", ask, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("form", form, Filters.chat(GROUP)))
    dp.add_handler(CommandHandler("date", date, Filters.chat(GROUP) & Filters.user(VERIFIED_USERS)))
    dp.add_handler(CommandHandler("offtopic", offtopic, Filters.chat(GROUP) & Filters.user(ADMINS)))
    dp.add_handler(CommandHandler("polls", polls))
    #   dp.add_handler(MessageHandler(Filters.text & Filters.chat(OFFTOPIC_GROUP), postgress2))

    dp.add_handler(MessageHandler(Filters.chat_type.private, private_not_available))
    #  add commands below. follow this scheme:  "command", function

    # add commands above this comment
    #  dp.add_error_handler(error) #comment this one out for full stacktrace

    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://ptb-realme.herokuapp.com/' + TOKEN)
    updater.idle()
