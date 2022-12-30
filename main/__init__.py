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
SESSION = "AQBTJYqVTkrRqDnurCSB0zn2DL--qgYyDq0czMgt8Yr5NvZsSfXrIn-5nz2pGzpqceJuSBD3YMTA4iaRV1mQYmGlV8ZdStC6uOQDigvyjTxorxsAH2FoGJMKcCRFtge2eSQb6ARUx2wuq89gIai5VZaOY0aYD6r8nH0ybAxV9GeCTaGftG0m0cjrVNd1qP-1vUhedOOyjGz3ec03uxUX0SXuuymI6zWYH4n17eGuszDLdMeBthbQ0Yr069qmu_7PVLlERXcjSsav4pT1XEfIAj5QAO66Np5GZRsNiiQ8cD6R2Oova4uB9lRg3O57qc032s69XOkDlzm0jgCuLmPj4teKAAAAAU4QSUQA"
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
