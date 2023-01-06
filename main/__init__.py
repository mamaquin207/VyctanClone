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
SESSION = "AQAVkM9v70qLhNTv8L1qAzm4ryKmPVN1epXQUjXtOu_VMVrllxZNUHuBC3TF3Hp77EKTKdXXsNBIS5KQpg1H5c37TSadDfAen6GZZMqHCJRxTY-qD0AJpGOBqKkCE-b18BofwsvDHwGaKeONvA96hiXmsU-y51PmzH-xj7ZQNgZ4OM5EeLb8sJKhylPannjNrHOxPMCBLYhL9vpocmgph-fQYDmk_pGvlg_yor4BE5EH3uOTEykq_s6_c2hOEUPt1w9LXXGgP0wyX0-UjH2ogt8kHJybWRXJj2fwmYSt-r_eG6DZy1e3rw9EPCJ6zmOGHRb450uGgNzRjz_OVnZwuQfZAAAAAU0iIwkA"
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
