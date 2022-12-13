from io import BytesIO
import json

from pyrogram.types import Message, ChatMember
from pyrogram import Client, filters, enums

from UnitedScanner import ASS_ID, BOT_ID, pbot, ubot
from UnitedScanner.config import LOG_CHANNEL_ID, INSPECTORS
from UnitedScanner.utils.filters import command
#from UnitedScanner.db import global_bans_db as db

def extract_gban(message):
    hmmm = message.split("-id")[1]
    hmm = hmmm.split("-r")  
    id = int(hmm[0].split()[0].strip())
    reason = hmm[1].split("-p")[0].strip()
    proof = hmm[1].split("-p")[1].strip()
    return id, reason, proof

@ubot.on_message(command("scan"))
async def scan(_, message: Message):
    if message.from_user.id not in INSPECTORS:
        await message.reply_text(
            "You Are Not Inspector.",
        )
        return
    try:
        user_id, reason, united = extract_gban(message.text)
    except ValueError:
        await message.reply_text("id must be integer.")
        return
    except:
        await message.reply_text("wrong format bitch")
        return
    if int(user_id) in INSPECTORS:
        await message.reply_text(
            "It's An Inspector\nYou Can't Scan This Person.",
        )
        return
    
    if user_id == BOT_ID or user_id == ASS_ID:
        await message.reply_text("You uhh...want me to punch myself?")
        return
    if user_id in [777000, 1087968824]:
        await message.reply_text("Fool! You can't attack Telegram's native tech!")
        return
    
   # if db.is_user_gbanned(user_id):
       # await message.reply_text(f"""
#User is already scanned.
#Reason: {db.get_gbanned_user(user_id)["reason"]}

#Scanned By: {db.get_gbanned_user(user_id)["scanner"]}
#""")
    #    return

    for chat_id in GBAN_CHATS:
        await ubot.send_message(
            chat_id,
            f"/gban {user_id} {reason} Proof: {proof}. Scanned by {message.from_user.id}"
        )
    db.gban_user(user_id, message.from_user.id, f"{reason} Proof: {proof}")
    await message.reply_text("Successfully Scanned")
    await pbot.send_message(
        LOG_CHANNEL_ID,
        f"""
# SCANNED
User ID: {user_id}
Reason: {reason}
Scanner: {united}

Scanned By: {message.from_user.id}
"""
    )

@ubot.on_message(command("revert"))
async def revert(_, message: Message):
    if message.from_user.id not in INSPECTORS:
        await message.reply_text(
            "Aukat me reh chotu",
        )
        return
    try:
        user_id, reason, united = extract_gban(message.text)
    except:
        try:
            hmmm = message.text.split("-i")[1]
            user_id = int(hmmm.strip())
        except ValueError:
            await message.reply_text("id must be integer.")
        except:
            await message.reply_text("Format: `/revert -i (id)`")
            return
    if not db.is_user_gbanned(user_id):
        await message.reply_text(f"User ID: {user_id} is not scanned.")
        return
    for chat_id in GBAN_CHATS:
        await ubot.send_message(
            chat_id,
            f"/ungban {user_id}"
        )
    db.ungban_user(user_id)
    await message.reply_text(
        f"""
# REVERTED
User ID: {user_id}

Reverted By: {message.from_user.id}
"""
    )
    await pbot.send_message(
        LOG_CHANNEL_ID,
        f"""
# REVERTED
User ID: {user_id}

Reverted By: {message.from_user.id}
"""
    )


@ubot.on_message(command("Uhelp"))
async def Uhelp(_, message: Message):
    await message.reply(
f"""
United Scanner Commands:

INSPECTOR COMMANDS

/scan [userid][reason][united] or reply to user - Scans The User

/revert [userid] - Unscan User

/gscan - coming soon

/ungscan - coming soon


USERS COMMAND
?github [username] - to check GitHub Account """
    )
