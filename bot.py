import logging
import os

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1415969330:AAGEnSGxjYl-hd3VTkpS4uY017Wag5dDsDQ'
GROUP = -1001374176745  # -1001327617858

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        chat_id=update.message.chat_id,
        text="Hey human 🤖"
             "\n\n<b>🚧 The troubleshooting is currently under development. You can't use it yet. 🚧</b>"
             "\n\nHere we can troubleshoot issues together. I will then forward your question to the community."
             "\n\nI will ask you a few questions. Please respond in one message per each question."
             "\n\nTo restart type in /start"
             "\n\n<i>Note: Commands work in @realme_support only.</i>"
             "\n\nType /rules to get the group's rules.",
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=ReplyKeyboardMarkup([['Private chat not available yet.']], one_time_keyboard=True,
                                         resize_keyboard=True))


def admins(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Group's staff</u>"
                "\n\n<b>Organization</b>"
                "\n@aakaah00001"
                "\n@Prashant_Choudhary"
                "\n@PacificPC"
                "\n\n<b>Moderators</b>"
                "\n@pentexnyx"
                "\n@Abhishek2376")


def ask(update: Update, context: CallbackContext):
    delay_group(update, context, "<u>How to ask</u>"
                                 "\n\n<b>1. Formulate the question</b>"
                                 "\nMake sure to include:"
                                 "\n· The device you use"
                                 "\n· The latest software installed"
                                 "\n· What you want to do"
                                 "\n· What you have tried already"
                                 "\n· Why you want to do that"
                                 "\n· What benefits you expected"
                                 "\n· The output you got"
                                 "\n\n<b>2. Wait for a response</b>"
                                 "\nGive the community 48h to answer your question. The needed expert might not be "
                                 "available all the time, so receiving an answer might take a bit. "
                                 "\n\n<b>3. No answer yet</b>"
                                 "\nUse /experts and tag the experts, whose segment fits your issue."
                                 "\nIf you didn't receive an answer after a week, use /form and fill out "
                                 "the "
                                 "linked form. "
                                 "\n\nThese suggestions enable us to provide you with better answers "
                                 "quicker and "
                                 "will keep this chat more focused.")


def commands(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Commands</u>"
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
                "\n\n<b>/sdmaid</b>"
                "\nLatest release of the best cleaner out there"
                "\n\n<b>/android11</b>"
                "\nOfficial roadmap for the Early Access of RealmeUI 2.0"
                "\n\n<b>/ask</b>"
                "\nHow to ask questions properly"
                "\n\nContact @pentexnyx if you face any issues with me 🤖"
                "\n<code>version 0.8</code>")


def files(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Files</u>"
                "\n\n<b>/gcam</b>"
                "\nGoogle Camera and configs"
                "\n\n<b>/sdmaid</b>"
                "\nBest cleaning app"
                "\n\n\n<b>Any suggestions?</b>"
                "\nContact @pentexnyx")


def experts(update: Update, context: CallbackContext):
    delay_group(update, context, "<u>Community experts</u>"
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


def gcam(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Google Camera</u>"
                "\n\n<b>Latest Release</b>"
                "\n· <a href='https://t.me/realme_support/68844'>Urnyx05-v2.5</a>"
                "\n\nUrnyx05's releases work well on most Realme devices. Take a look at @googlecameraport for other "
                "releases. "
                "\n\n\n<b>Configurations</b>"
                "\n· <a href='https://t.me/realme_support/20129'>new-natural</a>"
                "\n· <a href='https://t.me/realme_support/20127'>X2 Pro terev</a>"
                "\n\nTo enable these configurations, place them in <b>Internal Storage > GCam > Configs7</b>. "
                "\n\nThen go to your GCam and press on the bottom left (next to the camera switch button) a few "
                "times. A dialog should appear where your can select the desired configuration. "
                "\n\nFeel free to fiddle around with LibPatcher (in GCam's settings) a little to "
                "shape the image output so that it fits your needs.")


def sdmaid(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>SD Maid</u>"
                "\n\n<b>Latest Release</b>"
                "\n· <a href='https://t.me/realme_support/52321'>Pro-v5.0.1</a>"
                "\n\nThis is an excellent cleaning app, which also takes care of databases, duplicates, caches etc. "
                "and enables you to freeze the apps you don't need.")


def rules(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Group's rules</u>"
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


def form(update: Update, context: CallbackContext):
    delay_group_button_url(
        update,
        context,
        "If your issue is not resolved by the community after a week, you can also contact the developers."
        "\n\nPlease don't abuse this possibility, so that Realme developers can focus on developing.",
        "Access form 📝",
        "https://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2-VGJasy8VU_BLsFA/viewform")


def android11(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Realme UI 2.0</u>"
                "\n\n<i>Early Access is there to test stuff. Testing is easier with a reduced userbase. Therefore it "
                "will be rolled out to a limited number of people only 😉</i> "
                "\n\n<a href='https://static.c.realme.com/IN/wm-thread/1323470129358438400.jpg'>Official Roadmap</a>"
                "\n\n<b>Early Access</b>"
                "\nThe timeline is for the first wave of early access rollout only. The version for the corresponding "
                "model will be released within the above mentioned month in batches, not at the beginning of the "
                "month."
                "\n\n<b>Stable release</b>"
                "\nWill be pushed to all users over a period of time, minimum 2 months after early access."
                "\n\nRelax and wait what happens 😎")


def message_button_url(update: Update, context: CallbackContext, text, button_text, button_url):
    if update.message.reply_to_message:
        return update.message.reply_to_message.reply_text(
            text=text,
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(text=button_text, url=button_url)))
    else:
        return context.bot.send_message(chat_id=update.message.chat_id,
                                        text=text,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_markup=InlineKeyboardMarkup.from_button(
                                            InlineKeyboardButton(text=button_text, url=button_url)))


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


def delay_group_button_url(update: Update, context: CallbackContext, text, button_text, button_url):
    update.message.delete()
    reply_message = message_button_url(update, context, text, button_text, button_url)

    context.job_queue.run_once(delete, 300, context=update.message.chat_id, name=str(reply_message.message_id))


def delay_group(update: Update, context: CallbackContext, text):
    update.message.delete()
    reply_message = message_html(update, context, text)
    context.job_queue.run_once(delete, 600, context=update.message.chat_id, name=str(reply_message.message_id))


def delete(context: CallbackContext):
    telegram.Message = context.bot.delete_message(chat_id=str(context.job.context), message_id=context.job.name)


def remove_message(update: Update, context: CallbackContext):
    update.message.delete()


def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    context.bot.send_message(
        chat_id=-1001338514957,
        text="<b>🤖 Affected Bot</b>\n@" + context.bot.username +
             "\n\n<b>⚠ Error</b>\n<code>" + str(context.error) +
             "</code>\n\n<b>Caused by Update</b>\n<code>" + str(update) + "</code>",
        parse_mode=telegram.ParseMode.HTML)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, filters=Filters.private))
    dp.add_handler(CommandHandler("commands", commands, filters=Filters.chat(chat_id=GROUP)))

    dp.add_handler(CommandHandler("files", files, filters=Filters.chat(chat_id=GROUP)))

    dp.add_handler(CommandHandler("admins", admins, filters=Filters.chat(chat_id=GROUP)))
    dp.add_handler(CommandHandler("rules", rules))

    dp.add_handler(CommandHandler("gcam", gcam, filters=Filters.chat(chat_id=GROUP)))
    dp.add_handler(CommandHandler("sdmaid", sdmaid, filters=Filters.chat(chat_id=GROUP)))
    dp.add_handler(CommandHandler("experts", experts, filters=Filters.chat(chat_id=GROUP)))

    dp.add_handler(CommandHandler("ask", ask, filters=Filters.chat(chat_id=GROUP)))
    dp.add_handler(CommandHandler("android11", android11, filters=Filters.chat(chat_id=GROUP)))
    dp.add_handler(CommandHandler("form", form, filters=Filters.chat(chat_id=GROUP)))

    dp.add_handler(MessageHandler(
        Filters.text(["/help@CoronaVirusRobot", "/victims@CoronaVirusRobot", "/infect@CoronaVirusRobot"]),
        remove_message))

    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://ptb-realme.herokuapp.com/' + TOKEN)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
