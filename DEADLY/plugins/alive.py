from pyrogram import filters, Client
from pyrogram.types import *


SUPPORT = ""


ALIVE_TXT = "𝐃𝐄𝐀𝐃𝐋𝐘𝐒𝐏𝐀𝐌-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 🇮🇳\n"
ALIVE_TXT += "**ʏᴏᴜʀ ᴅᴇᴀᴅʟʏsᴘᴀᴍ ɪs 𝟷𝟶𝟶% sᴀғᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ғɪɴᴇ**\n"
ALIVE_TXT += "**𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 100% 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙰𝙽𝙳 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙲𝙻𝙾𝙽𝙴𝙳 𝙱𝚈 𝙰𝙽𝚈𝙾𝙽𝙴**\n"
ALIVE_TXT += "𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pversion}\n"
ALIVE_TXT += "**𝗽𝘆𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻: {pthversion}\n"
ALIVE_TXT += "𝘂𝗽𝘁𝗶𝗺𝗲 {uptime} 𝗽𝗶𝗻𝗴 {delta_ping * 1000:.3f}ᴍs\n"
ALIVE_TXT += "𝗼𝘄𝗻𝗲𝗿: @{username}\n"
ALIVE_TXT += "[𝘀𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/Deadly_spam_bot) [𝗰𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/Deadly_spambot)\n"

@Client.on_message(filters.user(SUDOER) & filters.command(["alive", "on", "start"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))   
    await m.delete() 
  await
