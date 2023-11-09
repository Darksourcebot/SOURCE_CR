from pyrogram import Client, filters
from pyrogram.types import Message
import requests 
from AnonX import app


banned = []
@app.on_message(filters.command("كتم", "") & filters.group)
async def ktm(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get("https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}")
        memberB = requests.get("https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}")
        if member["status"] == "administrator":
            if memberB["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك كتم مشرف او مالك", reply_to_message_id=message.id)
            banned.append(message.reply_to_message.from_user.id)
            await message.reply("- تم كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        elif member["status"] == "creator":
            banned.append(message.reply_to_message.from_user.id)
            await message.reply("- تم كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.id)


@app.on_message(filters.group, group=928)
async def ktmf(_: Client, message: Message):
    if message.from_user.id in banned: await message.delete()
    

@app.on_message(filters.command("طرد", ""))
async def tard(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get("https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}")
        memberB = requests.get("https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}")
        if member["status"] == "administrator":
            if memberB["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك طرد مشرف او مالك", reply_to_message_id=message.id)
            await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply("- تم حظر العضو بنجاح!", reply_to_message_id=message.id)
            return
        elif member["status"] == "creator":
            await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.reply("- تم الحظر العضو بنجاح!", reply_to_message_id=message.id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.id)

    
