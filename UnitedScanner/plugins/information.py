import asyncio
from UnitedScanner import * 
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import filters , enums
from UnitedScanner.utils.filters import command
from UnitedScanner.config import *


INFO_TEXT = """
𝗨𝗦𝗘𝗥𝗦𝗧𝗔𝗧𝗨𝗦:

**ID:** `{}`
**Name:** {}
**Username:** @{}
**Mention:** {}

**UserStatus:**\n`{}`\n
**RankUser**: {}

**Dc:** {}
**Bio:** {}

`note were sends you necessary information about user not at all`!
"""

async def userstatus(user_id):
    user = await bot.get_chat(user.id)
    x = user.status
    if x == enums.UserStatus.RECENTLY:
       return "User was seen recently."
    elif x == enums.UserStatus.LAST_WEEK:
        return "User was seen last week."
    elif x == enums.UserStatus.LONG_AGO:
        return "User was seen long ago."
    elif x == enums.UserStatus.OFFLINE:
        return "User is offline."
    elif x == enums.UserStatus.ONLINE:
       return "User is online."
   
    



@bot.on_message(filters.command(["info","userinfo"],["?"]))
async def userinfo(_, message):
        
     chat_id = message.chat.id
     user_id = message.from_user.id
     if not message.reply_to_message and len(message.command) == 2:
         
        try:
            user_id = message.text.split(None, 1)[1]
            user_info = await bot.get_chat(user.id)
            user = await bot.get_chat(user.id)
            rank = user.id in (await INSPECTORS())
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await bot.download_media(user.photo.big_file_id)
            await bot.send_photo(chat_id,photo=photo, caption=INFO_TEXT.format(
id,name, username, mention, status, rank,dc_id, bio),reply_to_message_id=message.id)
            await asyncio.sleep(5)
        except pyrogram.errors.exceptions.flood_420.FloodWait as wait_err:
            await asyncio.sleep(wait_err.x)
        except TimeoutError:
            continue
        except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
            continue
    
     elif not message.reply_to_message:
        try:
            user_info = await bot.get_chat(user.id)
             user = await bot.get_chat(user.id)
             status = await userstatus(user.id)
             id = user_info.id
             dc_id = user.dc_id
             rank = user.id in (await INSPECTORS())
             name = user_info.first_name
             username = user_info.username
             mention = user.mention
             bio = user_info.bio
             photo = await bot.download_media(user.photo.big_file_id)
             await bot.send_photo(chat_id,photo=photo, caption=INFO_TEXT.format(
id,name, username, mention,status,rank, dc_id, bio),reply_to_message_id=message.id)
             await asyncio.sleep(5)
         except pyrogram.errors.exceptions.flood_420.FloodWait as wait_err:
             await asyncio.sleep(wait_err.x)
         except TimeoutError:
             continue
         except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
             continue
     elif message.reply_to_message:
         user_id = message.reply_to_message.from_user.id          
         user_info = await bot.get_chat(user.id)
         user = await bot.get_chat(user.id)
         status = await userstatus(user.id)
         id = user_info.id
         dc_id = user.dc_id
         rank = user.id in (await INSPECTORS())
         name = user_info.first_name
         username = user_info.username
         mention = user.mention
         bio = user_info.bio
         photo = await bot.download_media(message.reply_to_message.from_user.photo.big_file_id)
         await bot.send_photo(chat_id,photo=photo,caption=INFO_TEXT.format(
id,name, username, mention,status,rank, dc_id, bio),reply_to_message_id=message.id)
          
