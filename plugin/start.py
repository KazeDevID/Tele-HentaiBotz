from pyrogram import *
from pyrogram.types import *

def start(client, message):
    message.reply_text("""**/search <hentai name> to search**\n Powered By @KenalSayaaa""", parse_mode="markdown")
