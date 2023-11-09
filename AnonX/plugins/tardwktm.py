from pyrogram import Client, filters
from pyrogram.types import Message
import requests 
from AnonX import app

muted = []
@app.on_message(filters.command("كتم", "") & filters.group)
async def ktm(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        memberB = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if memberB["result"]["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك كتم مشرف او مالك", reply_to_message_id=message.id)
            muted.append(message.reply_to_message.from_user.id)
            await message.reply("- تم كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        elif member["result"]["status"] == "creator":
            muted.append(message.reply_to_message.from_user.id)
            await message.reply("- تم كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.id)


@app.on_message(filters.command("الغاء كتم", "") & filters.group)
async def unktm(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if message.reply_to_message.from_user.id not in muted: return await message.reply("- هذا المستخدم غير مكتوم!")
            muted.pop(message.reply_to_message.from_user.id)
            await message.reply("- تم الغاء كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        elif member["result"]["status"] == "creator":
            if message.from_user.id not in muted: return message.reply("- هذا المستخدم غير مكتوم!")
            muted.pop(message.reply_to_message.from_user.id)
            await message.reply("- تم الغاء كتم العضو بنجاح!", reply_to_message_id=message.id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.id)



@app.on_message(filters.text & filters.group, group=928)
async def ktmf(_: Client, message: Message):
    if message.from_user.id in muted: await message.delete()
    

@app.on_message(filters.command("طرد", "") & filters.group)
async def tard(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        memberB = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if memberB["result"]["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك طرد مشرف او مالك", reply_to_message_id=message.id)
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply("- ليس لدي الصلاحيه لطرد هذا العضو")
            await message.reply("- تم طرد العضو بنجاح!", reply_to_message_id=message.id)
            return
        elif member["result"]["status"] == "creator":
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply("- ليس لدي الصلاحيه لطرد هذا العضو")
            await message.reply("- تم طرد العضو بنجاح!", reply_to_message_id=message.id)
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.id)
    
