import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = "1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ"


def start(update: Update, context: CallbackContext):
    delay_group(update, context, "Fancy text")
   # message_html(update, context, "Even fancier text")


def delay_group(update: Update, context: CallbackContext, text: str):

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=telegram.ParseMode.HTML)
    else:
        reply_message = context.bot.send_message(
            chat_id=update.message.chat_id,
            text=text,
            parse_mode=telegram.ParseMode.HTML)
        context.job_queue.run_once(delete, 30, context=reply_message.chat_id, name=str(reply_message.message_id))

    update.message.delete()


def message_html(update: Update, context: CallbackContext, text):  # return context.bot.send_message(
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=telegram.ParseMode.HTML)
    else:
        return context.bot.send_message(
            chat_id=update.message.chat_id,
            text=text,
            parse_mode=telegram.ParseMode.HTML)


def delete(context: CallbackContext):
    telegram.Message = context.bot.delete_message(chat_id=str(context.job.context), message_id=context.job.name)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("test", start))

    PORT = int(os.environ.get('PORT', 5000))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.setWebhook('https://ptb-realme.herokuapp.com/' + TOKEN)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
