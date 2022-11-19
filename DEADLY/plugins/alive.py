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
from DEADLY import ALIVE_PIC, SUDOERS



START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)




pthversion = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"




@Client.on_message(filters.user(SUDOERS) & filters.command(["alive", "on", "start"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))  
    ALIVE_TXT = f"𝐃𝐄𝐀𝐃𝐋𝐘𝐒𝐏𝐀𝐌-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 🇮🇳\n"
    ALIVE_TXT += f"🔸**ʏᴏᴜʀ ᴅᴇᴀᴅʟʏsᴘᴀᴍ ɪs 𝟷𝟶𝟶% sᴀғᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ**\n\n"
    ALIVE_TXT += f"🔹 **𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 100% 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙰𝙽𝙳 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙲𝙻𝙾𝙽𝙴𝙳 𝙱𝚈 𝙰𝙽𝚈𝙾𝙽𝙴**\n\n"
    ALIVE_TXT += f"════════════════════\n"
    ALIVE_TXT += f"🔸𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pversion}\n"
    ALIVE_TXT += f"🔹 𝗽𝘆𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pthversion}\n"
    ALIVE_TXT += f"🔸𝘂𝗽𝘁𝗶𝗺𝗲 {uptime} 𝗽𝗶𝗻𝗴 {delta_ping * 1000:.3f}ᴍs\n\n"
    ALIVE_TXT += f"════════════════════\n"
    ALIVE_TXT += f"🔸[𝘀𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/Deadly_spam_bot)🔹|🔸[𝗰𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/Deadly_spambot)\n"
    await m.delete() 
    await m.reply_photo(photo=ALIVE_PIC, caption=ALIVE_TXT) 


@Client.on_message(filters.user(SUDOERS) & filters.command(["ping", "pong"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    ping_a = f"𝙋𝙊𝙉𝙂:🏓\n\n"
    ping_a += f"ʏᴏᴜʀ sᴘᴀᴍ ᴜʙ ɪs ғᴜɴᴄᴛɪᴏɴɪɴɢ ᴘʀᴏᴘᴇʀʟʏ🌹\n\n"  
    ping_a = f"𝙋𝙊𝙉𝙂:🏓{delta_ping * 1000:.3f}\n"
    await m.delete() 
    await m.reply_text(ping_a) 
 
