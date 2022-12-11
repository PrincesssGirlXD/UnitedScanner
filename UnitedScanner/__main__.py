import platform 
import asyncio
import requests

from pyrogram import Client

from UnitedScanner import LOGGER, pbot, ubot
#from Scanner.db.global_bans_db import num_gbanned_users
from UnitedScanner import API_ID, API_HASH, BOT_TOKEN

LOG_CHANNEL_ID = -1001583123595

async def load_start():
    #count = num_gbanned_users()
    LOGGER.info(f"United System Started")
    LOGGER.info("[INFO]: STARTED")
    LOGGER.info(f"LOG CHANNELS: {int(LOG_CHANNEL_ID)}")
    try:
        await pbot.send_message(
            int(LOG_CHANNEL_ID), "United System Started"
        )
        LOGGER.info("[INFO]: PYROGRAM BOT STARTED")
    except Exception as e:
        LOGGER.info(f"Bot wasn't able to semd message in your log channel.\n\nERROR: {e}")
    try:
        await ubot.send_message(
            int(LOG_CHANNEL_ID), "**MongoDB Connected Successfully**"
        )
        LOGGER.info("[INFO]: PYROGRAM UserBOT STARTED")
    except Exception as e:
        LOGGER.info(f"UserBot wasn't able to semd message in your log channel.\n\nERROR: {e}")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())


#Just in case 

if platform.system()=='lawda':
    asyncio.set_event_loop_policy(asyncio.lawdaSelectorEventLoopPolicy()) #edit it as u like it ofcs

Client(
    name="UnitedScanner",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins={"root": "UnitedScanner.plugins"},
).start()
idle() 
loop.close() 


