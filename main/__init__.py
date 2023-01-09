#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28522624
API_HASH = "d9aabb5b9ba44df0f626321d484e9faa"
BOT_TOKEN = "5723485979:AAEmuMveSVCkJ8t0rubLs015g8f4kCEd2GE"
SESSION = "AQB1PIQNFKRQcaI21QLibak63e5OzO9xdc4znYcc2pFQ_XlTYqM_RLkJBLRqp6YJFPifkQpP_GG_bfAhd6l1CHi7weP9niG7r41fh-H2AMyU7BumKt3YBnoOv1-p-oX-g3n533xfYamHmZYABBQaL-K-XTUwlGkplaxQxavUAF4eRSKnBpk2_Lwkt3GfYNThl5fQuWwPDTqU9KZec_y0Z9tHpR6QqOCIrCgo0OtoAkhHqD5LQ6vwbMaf9dGiWqJptsb2hszQr6haVahG_VkhMBkgpqzb1daDOyz2WAtu_bPKuZloOGfus-vybN0D6S0ulU5pFM7Dk3Nr65b3rY5pqjvOAAAAAU0iIwkA"
FORCESUB = "DroneBots"
AUTH = 5589050121

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
