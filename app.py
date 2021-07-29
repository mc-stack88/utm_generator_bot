#packages
from telegram.ext import Updater, MessageHandler, Filters
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
    if("twitter" in incoming_msg.lower()):
        social_media = "twitter"
        global twitter
        twitter = twitter + 1 
        resToUser = Urlify(social_media, twitter)

    elif("reddit" in incoming_msg.lower()):
        social_media = "reddit"
        global reddit
        reddit = reddit + 1 
        resToUser = Urlify(social_media, reddit)

    elif("linkedin" in incoming_msg.lower()):
        social_media = "linkedin"
        global linkedin
        linkedin = linkedin + 1 
        resToUser = Urlify(social_media, linkedin)

    elif("discord" in incoming_msg.lower()):
        social_media = "discord"
        global discord
        discord = discord + 1 
        resToUser = Urlify(social_media, discord)

    elif("slack" in incoming_msg.lower()):
        social_media = "slack"
        global slack
        slack = slack + 1 
        resToUser = Urlify(social_media, slack)

    elif("whatsapp" in incoming_msg.lower()):
        social_media = "whatsapp"
        global whataspp
        whataspp = whatsapp + 1 
        resToUser = Urlify(social_media, whataspp)
    else:
        resToUser = "cool"

    context.bot.send_message(chat_id=update.effective_chat.id, text=resToUser)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()