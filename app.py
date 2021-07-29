#packages
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
import logging
import os
from dotenv import load_dotenv
from urllib.parse import parse_qsl ,urlparse, urlencode, urlunparse

load_dotenv()
TELE_TOKEN = os.getenv('telegramToken')

updater = Updater(token=TELE_TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

twitter = 2
reddit = 0
linkedin = 0 
slack = 0
whatsapp = 0
discord = 0


def Urlify(social_media, count):
    baseURL = "https://www.getwithub.com"
    params = {"utm_campaign":"withub-beta-access", "utm_medium": social_media, "utm_source": "website" , "utm_term": count}
    url_parse = urlparse(baseURL)
    query = url_parse.query
    url_dict = dict(parse_qsl(query))
    url_dict.update(params)
    url_new_query = urlencode(url_dict)
    url_parse = url_parse._replace(query=url_new_query)
    new_url = urlunparse(url_parse)
    return(new_url)

def echo(update, context):
    #user
    chat_id = update.effective_chat.id
    incoming_msg = update.message.text
    social_media = "did not work"
    if("twitter link" in incoming_msg.lower()):
        social_media = "twitter"
        global twitter
        twitter = twitter + 1 
        print(twitter)
        resToUser = Urlify(social_media, twitter)
        print(resToUser)

    context.bot.send_message(chat_id=update.effective_chat.id, text=resToUser)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()