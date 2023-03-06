"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import time

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, MessageHandler 

from Shikimori import dispatcher 
from Shikimori.vars import OWNER_USERNAME

def awake(update: Update, context: CallbackContext): 
    hmm = update.effective_message.reply_text("⚡")
    time.sleep(2)
    hmm.edit_text("ᴀʟɪᴠɪɴɢ..")
    time.sleep(0.1)
    hmm.edit_text("ᴀʟɪᴠɪɴɢ ʙᴀʙʏ ....")
    time.sleep(0.1)
    hmm1 = update.effective_message.reply_sticker(
    "CAACAgUAAx0CZIiVngABBHAzYwdi9OIVTQ7DYELAqMl46fgnK4wAAjsIAAKagolX-O0V64tvzK8pBA",
    )
    hmm.delete()
    time.sleep(2.5)
    update.effective_message.reply_photo(
    "https://telegra.ph/file/49b9382045dec452d4f4e.jpg",
    f""" ♦️「 ʟɪᴇᴜᴛᴇɴᴀɴᴛ ᴏᴡɴᴇʀ 」♦️

➖➖➖➖➖➖➖➖➖➖➖➖➖ ࿐•┈────┈•

• ᴏᴡɴᴇʀ : {OWNER_USERNAME}

• ᴄʟɪᴇɴᴛ : ᴘʏʀᴏɢʀᴀᴍ

➖➖➖➖➖➖➖➖➖➖➖➖➖ ࿐•┈────┈•

「 ᴛʜɪꜱ ɪꜱ ᴀ ɢᴏᴅ ʟɪᴋᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ」

•➵࿐•┈────┈•

┊╰─•➢ ꜱᴛᴀᴛꜱ : ᴀ +

┊╰─•➢ ʜᴀʀᴇᴍ : 16

┊╰─•➢ ᴘᴏᴡᴇʀ ʟᴇᴠᴇʟ : ɪɴꜰɪɴɪᴛʏ 

╰───•➢""",
	parse_mode=ParseMode.MARKDOWN
  )
    hmm1.delete()

dispatcher.add_handler(MessageHandler("awake kurumi", awake, run_async=True))
