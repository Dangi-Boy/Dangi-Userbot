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
    ALIVE_TXT = f" ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐ฎ๐ณ\n"
    ALIVE_TXT += f"๐ธ**สแดแดส sแดแดแด ษชs ๐ท๐ถ๐ถ% sแดาแด แดษดแด แดกแดสแดษชษดษข าษชษดแด**\n\n"
    ALIVE_TXT += f"๐น **๐๐ท๐ธ๐ ๐๐๐ด๐๐ฑ๐พ๐ ๐ธ๐ 100% ๐ผ๐ฐ๐ณ๐ด ๐๐ธ๐๐ท ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ ๐ฐ๐ฝ๐ณ ๐๐ธ๐๐ท๐พ๐๐ ๐ฒ๐ป๐พ๐ฝ๐ด๐ณ ๐ฑ๐ ๐ฐ๐ฝ๐๐พ๐ฝ๐ด**\n\n"
    ALIVE_TXT += f"โโโโโโโโโโโโโโโโโโโโ\n"
    ALIVE_TXT += f"๐ธ๐ฝ๐๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ ๐๐ฒ๐ฟ๐๐ถ๐ผ๐ป: {pversion}\n"
    ALIVE_TXT += f"๐น ๐ฝ๐๐๐ต๐ผ๐ป ๐๐ฒ๐ฟ๐๐ถ๐ผ๐ป: {pthversion}\n"
    ALIVE_TXT += f"๐ธ๐๐ฝ๐๐ถ๐บ๐ฒ {uptime} ๐ฝ๐ถ๐ป๐ด {delta_ping * 1000:.3f}แดs\n\n"
    ALIVE_TXT += f"โโโโโโโโโโโโโโโโโโโโ\n"
    ALIVE_TXT += f"๐ธ[๐๐๐ฝ๐ฝ๐ผ๐ฟ๐](https://t.me/Dangi_UserBOTs)๐น|๐ธ[๐ฐ๐ต๐ฎ๐ป๐ป๐ฒ๐น](https://t.me/Dangi_spambot)\n"
    await m.delete() 
    await m.reply_photo(photo=ALIVE_PIC, caption=ALIVE_TXT) 


@Client.on_message(filters.user(SUDOERS) & filters.command(["ping", "pong"], [".", "!", "/", ",", "+", "?"]))
async def ping(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    ping_a = "โโโโโ โโโ โโโโโโ โโโโโ\nโโโโโ โโโ โโโโโโ โโโโโ\nโโโโโ โโโ โโโโโโ โโโโโ\n\n"  
    ping_b = f"๐๐๐๐:๐ {delta_ping * 1000:.3f}แดs\n"
    text = f"{ping_a} {ping_b}"
    await m.delete() 
    await m.reply_text(text) 
 

@Client.on_message(filters.user(SUDOERS) & filters.command(["help", "cmds"], [".", "!", "/"]))
async def eqw(client: Client, m: Message):
    blaze = await m.reply_text("Processing...")
    help_a = f"๐ฅ ๐๐๐๐๐ ๐ฆ๐ฃ๐๐? ๐จ๐ฆ๐๐ฅ๐๐ข๐ง๐ฅ\n\n"
    help_a += f"๐๐ด๐ป๐ฒ๐พ๐ผ๐ด ๐๐พ ๐ฆ๐ฃ๐๐? ๐ฒ๐ผ๐ณ ๐ท๐ด๐ป๐ฟ\n\n"
    help_a += f"๐ธ ๐๐ ๐๐๐๐ ๐\n\n"
    help_a += f".dm [username] [msz]\n"
    help_a += f".draid [count]  [username/reply_to_user]\n\n"
    help_a += f"๐น ๐๐๐๐ ๐๐๐๐ ๐\n\n"
    help_a += f".raid [count] [username/reply_to_user]\n"
    help_a += f".replyraid [username/reply_to_user]\n"
    help_a += f".dreplyraid [username/reply_to_user]\n\n"
    help_a += f"๐ธ ๐๐๐๐ ๐๐๐๐ ๐\n\n"
    help_a += f".addecho [username/reply_to_user]\n"
    help_a += f".rmecho [username/reply_to_user]\n\n"
    help_a += f"๐น ๐๐๐ ๐๐๐๐ ๐\n\n"
    help_a += f".alive to check if alive\n"
    help_a += f".ping to check ping\n"
    help_a += f".restart to restart bot\n\n"
    help_a += f"๐ธ ๐๐๐๐ ๐๐๐๐ ๐\n\n"
    help_a += f".spam [count] [spam_text]\n"
    help_a += f".delayspam [sleep time] [count] [message to spam]\n\n"
    help_a += f"๐น ๐๐๐๐๐๐๐ ๐๐: @The_DANGI\n"
    await m.delete() 
    await blaze.edit(help_a) 
