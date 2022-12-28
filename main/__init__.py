#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24525445
API_HASH = "ec30d2a64a99aa17518c6506860dcf43"
BOT_TOKEN = "5738131114:AAGtlFDkNodUHftMt_b9w_6_t7Cz1cg-tQ8"
SESSION = "AQB0uqvpFix_JQIcs6gvKXF8pq6A2ho7a8W0AyccPKam7DTxCFzWE99nYTvzlI8uyMtbaMgsaYs8aAIV7LLbz5qi7rrpfH3rb8cpjIfbZNWMAW6OSi2Pici4pMQPfjYcwmNh1NX92uqGFBl_wDT21i579WbCP7OpoTVY0jLcdkLUf-yAtevF0Ox51QQ00KVkM7UF0nRBfoRwwMba9JI1_Nb8JlM20JMtgmN8bXNmJeQ9P1mPJTHeuYkywBnySK_I3lz9GVn5OGRQa3YbHucWga3Ns4ZD0CZ5FORqwNK6GCiGTb_qyGzy8bGIrc3Y9c2jJBE8Tz13buNxKLJiNBcYuBV9AAAAAU4QSUQA"
FORCESUB = "my_forwarder_bot01"
AUTH = 5604657476

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
