#pip install -r requirements.txt
import telegram.ext #importing this package
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")#helps to read from env. variable
def start(update, context):
    update.message.reply_text("Hello! Welcome to Mighty Bot")
def helps(update, context):
    update.message.reply_text(
        """
        Hi there! I'm Telegram Bot created by Ankit. Please follow these commands:-
        /start - to start the conversation
        /content - Information about Ankit
        /contact - Information about contact of Ankit
        /help - to get this help menu

        I hope this helps:)
        """
    )
def content(update, context):
    update.message.reply_text(
        """
        Hi, I am Ankit Verma, a sophomore year student pursuing Computer 
        Science engineering from BIT Mesra.
        Hustling and upskilling myself everyday.
        Currently I am giving contests on Codeforces and learning WebD. 
        (Pre-ordered : ML and other tech's !)
        Let's connect as we move foward in this world.
        """
    )
def contact(update, context):
    update.message.reply_text(
        """
        Email - syncing284@gmail.com
        """
    )
def handle_message(update,context):
    update.message.reply_text(
        f"You said {update.message.text}"
    )
updater = telegram.ext.Updater(TOKEN, use_context = True) #updater is a variable
dispatch = updater.dispatcher
dispatch.add_handler(telegram.ext.CommandHandler('start',start))
dispatch.add_handler(telegram.ext.CommandHandler('help',helps))
dispatch.add_handler(telegram.ext.CommandHandler('content',content))
dispatch.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()