import os
import sys
import asyncio
import re
from random import choice

from config import SUDOERS
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.data import RAID, DEV, PROGROUPS




@Client.on_message(filters.user(SUDOERS) & filters.command(["raid"], [",", ".", "!", "/", "+", "?"]))
async def raid(app: Client, m: Message):  
      usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid [Username of User] [count] \n\n.raid [count] [reply to a User]\n\nCount must be a integer."
      Deadly = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Deadly) == 2:
        counts = int(Deadly[0])
        username = Deadly[1]
        if not counts:
          await m.reply_text(f"RAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Deadly[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Deadly[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text(usage)
        return
      if int(m.chat.id) in PROGROUPS:
         await m.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in DEV:
         await m.reply_text("I can't raid on my developer")
         return
      if int(user.id) in SUDOERS:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      for _ in range(counts): 
         blaze = f"{mention} {choice(RAID)}"
         await app.send_message(m.chat.id, blaze)
         await asyncio.sleep(0.3)




