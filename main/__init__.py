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
BOT_TOKEN = "5606250570:AAH2CbJOYoofUz1kVkyxL6imu6geKGt4nQQ"
SESSION = "AQCVhjcI9cul3BuNt22l9itMxEf9NlDEJK1lCMRUWuvRFUKSdu_C-VtwzmsHWlfo4QK38VNzneoz1KHFUEjOra0WFldMCimRKgsKM6uMOs6O14i05zHbR0v5AUjC5RcUVyXy6gO0eako1qIgfyhRitTHAUhKVs4URhe2wEM9BQq0CjTTFUSBCGAbXYQQssfkiT62NoOzkUzu6m1HSJgEgelQDor_efOkI1ZbPV_TCTxWLKDBdayNCHLOCXPKZOf9DZXqbE-FDOSnVuUPY3ihKaopB8Aick7-oIDwql4toCGVX6gTNE2DF93ogUuzRYiMWzVeQj6Zb1bp-SF5H1C1mUCFAAAAAU4QSUQA"
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
