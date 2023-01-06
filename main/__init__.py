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
SESSION = "AQC8TAGPnGpg_wBdnvQIwNW-hNNEMkeI6Pho006pbrjN_nnTq1Ittvk2Kop9Td-8x4sShRderu79a0q5poRfD56x5cYbyMmptzhmuSdsEzElR3W9IUkY8o0jjgdRvY3vjGM9wmmuE3bT6nhfzDs8tpruV7yZ68EteGujPECeDoAK8oCzYZOy2mRYobU_skJ1D8nitgQeOs4zaaDqTJPWNvWnk243T4vG1eiHEHh9E7CNe0wssTshM5lNgPc2_AR8MrVTK0t_PjH1IN6501-nqf55RPntBjO7fVoJu75awfJ2tr7DrGs8ZHXmU14LDTLTOJjclMgea3VahP7GQaBt16ibAAAAAU0iIwkA"
FORCESUB = "VyctanClone_bot"
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
