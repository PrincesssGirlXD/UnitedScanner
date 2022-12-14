import asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import time
from datetime import datetime

from UnitedScanner.utils.filters import command
from UnitedScanner.config import SUPPORT_CHAT , START_PIC
from UnitedScanner import BOT_USERNAME, starttime

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


CAPTION = f"""Hᴇʟʟᴏ message.from_user.mention()
I Wɪʟʟ Hᴇʟᴘ Yᴏᴜ Tᴏ Pʀᴏᴛᴇᴄᴛ Yᴏᴜ Fʀᴏᴍ Pᴏᴛᴇɴᴛɪᴀʟ Tʜʀᴇᴀᴛ.
"""

@Client.on_message(command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.delete()
    accha = await message.reply("United Scanner Starting ✨")
    await accha.delete()
    await asyncio.sleep(0.1)
    await message.reply_video("https://telegra.ph/file/e3c8a57b3ebcd0b1c8529.mp4" , CAPTION ,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton(
                        "Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
           ]
        ),
    )

@Client.on_message(command("start") & ~filters.private)
async def start_grp(client: Client, message: Message):
    await message.delete()
    accha = await message.reply("United Scanner Starting ✨")
    await accha.delete()
    await asyncio.sleep(0.1)
    await message.reply_video("https://telegra.ph/file/e3c8a57b3ebcd0b1c8529.mp4" , CAPTION ,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url=f"https://t.me/{SUPPORT_CHAT}"),
                    InlineKeyboardButton(
                        "Add Me To Your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
           ]
        ),
    )
