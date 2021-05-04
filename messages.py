import time

import psycopg2
from telegram import Update, ParseMode, Message
from telegram.ext import CallbackContext

from main import GROUP, OFFTOPIC_GROUP, VERIFIED_USERS, DATABASE_URL
from utils import delay_group, delay_group_button_url, now


##########################################
# this file contains the actions that will happen once a command is called
# just replicate below schemes :)
##########################################

def private_not_available(update: Update, context: CallbackContext):
    update.message.reply_text(
        "My commands work in @realme_support only."
        "\nYou can submit some Feedback here though."
        "\n\nDo you like me? Is there any missing feature?"
        "\n\nPlease tell me 🤖")


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
    delay_group(update, context,
                "<u>How to ask</u>"
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
                "\nGive the community 48h to answer your question. The needed expert might not be available all the "
                "time, so receiving an answer might take a bit. "
                "\n\n<b>3. No answer yet</b>"
                "\nUse /experts and tag the experts, whose segment fits your issue."
                "\nIf you didn't receive an answer after a week, use /form and fill out the linked form."
                "\n\nThese suggestions enable us to provide you with better answers quicker and will keep this chat "
                "more focused.")


def commands(update: Update, context):
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
                "\n\nMessage @pentexnyx, if you face any issues with me 🤖"
                "\nRelease ")  # + str(os.environ.get('HEROKU_RELEASE_VERSION')))


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
    delay_group(update, context,
                "<u>Community experts</u>"
                "\n\n<b>Software issues</b>"
                "\n@Abhishek2376"
                "\n@NoobOf2021"
                "\n@pentexnyx"
                "\n\n<b>Hardware issues</b>"
                "\n@Abhishek2376"
                "\n\n<b>Updates and apps</b>"
                "\n@Abhishek2376"
                "\n@NoobOf2021"
                "\n\n<b>UI-Team</b>"
                "\n@Abhishek2376"
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
                "\n\n<b>Releases</b>"
                "\n· <a href='https://t.me/realme_support/113595'>PXv8.1_GCam-v1.2</a>"
                "\n· <a href='https://t.me/realme_support/113609'>Urnyx05-v2.5</a>"
                "\n\nUrnyx05's releases work well on most Realme devices. Take a look at @googlecameraport for other "
                "releases."
                "\n\n\n<b>Configurations</b>"
                "\nTaken from <a href='https://www.celsoazevedo.com/files/android/google-camera/f/configs-urnyx-02"
                "/'>Urnyx05's page</a>. These configurations are optimized for a specific device, but may work for "
                "other devices aswell. Just give them a try 😊 "
                "\n\n· <a href='https://t.me/realme_support/113610'>Realme 5 & 5 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113612'>Realme X2 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113614'>Realme X50 & X50 Pro</a>"
                "\n· <a href='https://t.me/realme_support/113616'>Realme 6 & 6 Pro</a>"
                "\n\nTo enable these configurations, place them in <b>Internal Storage > GCam > Configs7</b>."
                "\n\nThen go to your GCam and press on the bottom left (next to the camera switch button) a few "
                "times. A dialog should appear where your can select the desired configuration. "
                "\n\nFeel free to fiddle around with LibPatcher (in GCam's settings) a little to shape the image "
                "output so that it fits your needs.")


def cleaners(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Cleaners</u>"
                "\n\n<b>SD Maid</b> · <a href='https://t.me/realme_support/122153'>Download 5.1.1</a>"
                "\n\nThis is an excellent cleaning app, which also takes care of databases, duplicates, caches etc. "
                "and enables you to freeze the apps you don't need."
                "\n\n\n<b>Phone Manager</b> · <a href='https://t.me/realme_support/126160'>Download 8.6.1</a>"
                "\n\nOfficial Cleaner by Realme. Requires Android 11.")


def rules(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Group's rules</u>"
                "\n\n<b>1. Language</b>"
                "\nPlease use English or Hindi as an alternative."
                "\n\n<b>2. Links</b>"
                "\nSending links is not permitted."
                "\n\n<b>3. Forwarding</b>"
                "\nForwarding messages from other channels is not permitted."
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
    delay_group_button_url(update, context,
                           "If your issue is not resolved by the community after a week, you can also contact the "
                           "developers."
                           "\n\nWe Admins collect those entries and will forward them to the developers."
                           "\n\nPlease don't abuse this possibility, so that Realme developers can focus on developing.",
                           "Access form 📝",
                           "https://docs.google.com/forms/d/e/1FAIpQLSceGI9ZaNOIb4NN-3UdJ-mbzvbRwulAh2"
                           "-VGJasy8VU_BLsFA/viewform")


def date(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        delay_group(update, context,
                    "Hey {} 🤖"
                    "\n\n<i>Realme rolls out an Update, if it works as expected - not if a certain date is met. "
                    "Therefore an exact date for when you will receive an update doesn't exist.</i> "
                    "\n\n<b>Estimating the stable release date</b>"
                    "\nUse /android11 and add a minimum of 6 months after the Early Access date. This is the "
                    "timeframe developers currently need to go from Beta to Stable. "
                    "\n\nDevelopers are working very hard currently, but it may still take some time. Please stand by."
                    .format(update.message.reply_to_message.from_user.name))
    else:
        update.message.delete()


def offtopic(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        update.message.delete()
        context.bot.send_message(OFFTOPIC_GROUP,
                                 "<i>{} <a href='{}'>wrote</a>:</i>"
                                 "\n\n{}"
                                 .format(
                                     update.message.reply_to_message.from_user.name,
                                     update.message.reply_to_message.link,
                                     update.message.reply_to_message.text),
                                 ParseMode.HTML,
                                 True)
        update.message.reply_to_message.reply_text(
            "Hey {} 🤖"
            "\nThis is getting pretty off-topic now."
            "\n\nI moved the message to @realme_offtopic"
            "\n\nPlease continue the discussion there 😉"
                .format(update.message.reply_to_message.from_user.name))
    else:
        delay_group(update, context,
                    "Hey guys 🤖"
                    "\nFeel free to join @realme_offtopic to discuss topics not related to Realme or Android."
                    "\n\nYou can also send Links and Stickers there 🥳")


def android11(update: Update, context: CallbackContext):
    delay_group(update, context,
                "<u>Realme UI 2.0</u>"
                "\n\n<i>Early Access is there to test stuff. Testing is easier with a reduced userbase. Therefore it "
                "will be rolled out to a limited number of people only 😉</i> "
                "\n\n· <a href='https://static.c.realme.com/IN/wm-thread/1374937652238790656.png'>Current Roadmap</a> "
                "\n\n· <a href='https://static.c.realme.com/IN/wm-thread/1369542731847704576.jpg'>Previous Roadmap</a> "
                "\n\n<b>Early Access</b>"
                "\nThe timeline is for the first wave of early access rollout only. The version for the corresponding "
                "model will be released within the above mentioned month in batches, not at the beginning of the "
                "month."
                "\n\n<b>Stable release</b>"
                "\nWill be pushed to all users over a period of time, a few months after early access."
                "\n\nRelax and wait what happens 😎")


def polls(update: Update, context: CallbackContext):  # GROUP

    con = psycopg2.connect(DATABASE_URL)
  #  conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    cur = con.cursor()


    print(cur.execute('SELECT version()'))

    if update.message.from_user.id in VERIFIED_USERS:
        update.message.delete()
        #  and context.chat_data["polls_previous_date"] + 3628800000 < now(): ###enable again !!

        context.chat_data["polls_previous_link"] = \
            context.bot.send_message(OFFTOPIC_GROUP, "Hey Realme Fans!"
                                                     "\n\n<b>It's once again time for Poll-Five 🖐️</b> "
                                                     "\n\nThis idea came up in @realme_offtopic a few days ago and I "
                                                     "immediately implemented it. It could just be interesting to see what the "
                                                     "community thinks about certain topics. "
                                                     "\n\nCredits go to all the ones who brought up the following questions. "
                                                     "\n\nHope you enjoy it!",
                                     parse_mode=ParseMode.HTML
                                     ).link

        context.chat_data["polls_previous_date"] = now()

        ###polls go here f

    else:
        print(context.chat_data["polls_previous_link"])
        delay_group(update, context,
                    "<b>Poll-Five</b> 🖐️"
                    "\n\nThis idea came up in @realme_offtopic. We thought it could just be interesting to see what "
                    "the community thinks about certain topics. "
                    "\n\nCredits go to all the ones who brought up the questions."
                    "\n\n<a href='{}'>current poll</a>"
                    .format(context.chat_data["polls_previous_link"]))

  #  context.bot.send_message(OFFTOPIC_GROUP, "date: {} - link: {}".format(context.chat_data["polls_previous_date"],
  #                                                                        context.chat_data["polls_previous_link"]))
