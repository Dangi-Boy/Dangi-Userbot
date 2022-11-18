import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import filters
from sys import version_info
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import __version__ as pversion
from resources.data import PROGROUPS, DEV
From .import *
from DEADLY import ALIVE_PIC, SUDOERS

pthversion = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"



ALIVE_TXT = f"𝐃𝐄𝐀𝐃𝐋𝐘𝐒𝐏𝐀𝐌-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 🇮🇳\n"
ALIVE_TXT += f"🔸**ʏᴏᴜʀ ᴅᴇᴀᴅʟʏsᴘᴀᴍ ɪs 𝟷𝟶𝟶% sᴀғᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ**\n"
ALIVE_TXT += f"🔹 **𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 100% 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙰𝙽𝙳 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙲𝙻𝙾𝙽𝙴𝙳 𝙱𝚈 𝙰𝙽𝚈𝙾𝙽𝙴**\n\n"
ALIVE_TXT += f"════════════════════\n"
ALIVE_TXT += f"🔸𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pversion}\n"
ALIVE_TXT += f"🔹 𝗽𝘆𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pthversion}\n"
ALIVE_TXT += f"🔸𝘂𝗽𝘁𝗶𝗺𝗲 {uptime} 𝗽𝗶𝗻𝗴 {delta_ping * 1000:.3f}ᴍs\n\n"
ALIVE_TXT += f"════════════════════\n"
ALIVE_TXT += f"🔸[𝘀𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/Deadly_spam_bot) [𝗰𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/Deadly_spambot)\n"

@Client.on_message(filters.user(SUDOERS) & filters.command(["alive", "on", "start"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))   
 
 if int(message.chat.id) in PROGROUPS:
    await m.reply_text("Sorry U Cannot Use Alive Here") 
    return

    await m.delete() 
    await m.reply_photo(photo=ALIVE_PIC, caption=ALIVE_TXT) 
