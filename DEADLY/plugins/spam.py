from pyrogram.types import Message
import asyncio
import asyncio
from pyrogram import filters, Client
from DEADLY import SUDOERS
from resources.data import PROGROUPS, DEV

# SPAM
@Client.on_message(filters.user(SUDOERS) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def sspam(client: Client, message: Message):
    sex  = await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommands!\n\nspam <count> <message to spam>\n.spam <count> <reply to a message>\n\nCount must be a integer.")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await sex.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


#STICKERSPAM HANDLER
@Client.on_message(filters.user(SUDOERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)
