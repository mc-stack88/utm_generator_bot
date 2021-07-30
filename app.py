#packages
from telegram.ext import Updater, MessageHandler, Filters
import logging
import os
from dotenv import load_dotenv
from urllib.parse import parse_qsl ,urlparse, urlencode, urlunparse
import requests
import uuid
load_dotenv()
TELE_TOKEN = os.getenv('telegramToken')
BITLY_TOKEN = os.getenv('bitlyToken')
updater = Updater(token=TELE_TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def BitlyShortener(url):
    header = {
        "Authorization": BITLY_TOKEN,
        "Content-Type": "application/json"
    }
    params = {
        "long_url": url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
    data = response.json()
    shortenedLink = data['link']
    if shortenedLink:
        return shortenedLink
    else:
        return("Shortening error")
    # if 'link' in data.keys(): short_link = data['link']
    # else: short_link = None

def Urlify(social_media, uniqueID):
    baseURL = "https://www.getwithub.com"
    params = {"utm_campaign":"withub-beta-access", "utm_medium": social_media, "utm_source": "website" , "utm_term": uniqueID}
    url_parse = urlparse(baseURL)
    query = url_parse.query
    url_dict = dict(parse_qsl(query))
    url_dict.update(params)
    url_new_query = urlencode(url_dict)
    url_parse = url_parse._replace(query=url_new_query)
    new_url = urlunparse(url_parse)
    short_url = BitlyShortener(new_url)
    return(short_url)

def echo(update, context):
    #user
    chat_id = update.effective_chat.id
    incoming_msg = update.message.text
    social_media = "did not work"
    linkID = uuid.uuid4()

    if(incoming_msg.lower().startswith("twitter")):
        social_media = "twitter"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+replystring 

    elif(incoming_msg.lower().startswith("reddit")):
        social_media = "reddit"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+replystring

    elif(incoming_msg.lower().startswith("linkedin")):
        social_media = "linkedin"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+replystring

    elif(incoming_msg.lower().startswith("discord")):
        social_media = "discord"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+ replystring

    elif(incoming_msg.lower().startswith("slack")):
        social_media = "slack"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+replystring

    elif(incoming_msg.lower().startswith("whatsapp")):
        social_media = "whatsapp"
        replystring = "\nlink for : " + social_media + "\nunique ID = " + str(linkID) + "\n" 
        resToUser = Urlify(social_media, linkID)+ replystring
    
    else:
        resToUser = "cool"

    context.bot.send_message(chat_id=update.effective_chat.id, text=resToUser)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()