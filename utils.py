from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, Update
from telegram.ext import CallbackContext


##########################################
# feel free to ignore this file.
# it only contains some functions to simplify the rest of the code a bit.
##########################################

def message_button_url(update: Update, context: CallbackContext, text, button_text, button_url):
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(text=button_text, url=button_url)))
    else:
        return context.bot.send_message(chat_id=update.message.chat_id,
                                        text=text,
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=InlineKeyboardMarkup.from_button(
                                            InlineKeyboardButton(text=button_text, url=button_url)))


def message_html(update: Update, context: CallbackContext, text):
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=ParseMode.HTML)
    else:
        return context.bot.send_message(
            chat_id=update.message.chat_id,
            text=text,
            parse_mode=ParseMode.HTML)


def delay_group_button_url(update: Update, context: CallbackContext, text, button_text, button_url):
    update.message.delete()
    reply_message = message_button_url(update, context, text, button_text, button_url)
    context.job_queue.run_once(delete, 600, context=update.message.chat_id, name=str(reply_message.message_id))


def delay_group(update: Update, context, text):
    update.message.delete()

    if update.message.reply_to_message:
        update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=ParseMode.HTML)
    else:
        reply_message = context.bot.send_message(
            chat_id=update.message.chat_id,
            text=text,
            parse_mode=ParseMode.HTML)
        context.job_queue.run_once(delete, 600, context=reply_message.chat_id, name=str(reply_message.message_id))


def delete(context: CallbackContext):
    context.bot.delete_message(chat_id=str(context.job.context), message_id=context.job.name)


def remove_message(update: Update, context: CallbackContext):
    if update.message is not None:
        update.message.delete()
