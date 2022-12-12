import os

from pyrogram import filters
from pyrogram import Client as bot
from pyrogram.types import Message
from UnitedScanner.config import INSPECTORS
from UnitedScanner.utils import sections



async def get_user_info(user, already=False):
    if not already:
        chat_id = chat.id
        userss = await bot.get_chat(chat_id)
        user = await bot.get_users(chat_id)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    is_bot = user.is_bot
    photo_id = user.photo.big_file_id if user.photo else None
    is_dev = user_id in INSPECTORS
    body = { 
        "✪ ID": user_id,
        "✪ DC": dc_id,
        "✪ Name": [first_name],
        "✪ Username": [("@" + username) if username else "Null"],
        "✪ Mention": [mention],
        "✪ Bot": is_bot,
        "✪ Inspector": is_dev,
        "✪ Bio": userss.bio,
    }
    caption = section("User info results", body)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await bot.get_chat(chat_id)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else "Null"
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "✪ ID": chat_id,
        "✪ DC": dc_id,
        "✪ Type": type_,
        "✪ Name": [title],
        "✪ Username": [("@" + username) if username else "Null"],
        "✪ Mention": [link],
        "✪ Members": members,
        "✪ Scam": is_scam,
        "✪ Restricted": is_restricted,
        "✪ Description": [description],
    }
    caption = section("Chat info", body)
    return [caption, photo_id]

@bot.on_message(filters.command("info"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Information Processing...")

    try:
        info_caption, photo_id = await get_user_info(chat_id)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await bot.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)
