import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN)
updater.bot.setWebhook('https://pxnx-telegram-test.herokuapp.com/' + TOKEN)
