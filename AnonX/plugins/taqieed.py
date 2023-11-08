from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.enums import ChatMemberStatus
from datetime import datetime, timedelta
from AnonX import app

@app.on_message(filters.command("تقييد", "") & filters.group & filters.reply)
async def restric(_: Client, message: Message):
    user_id = message.from_user.id 
    chat_id = message.chat.id 
    replied = message.reply_to_message.from_user.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("- يجب ان تكون مشرف على الاقل لإستخدام هذا الامر")
    await app.restrict_chat_member(chat_id, replied, until_date=datetime.now() + timedelta(seconds=30), permissions=ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False))
    await message.reply_to_message.reply("- تم تقييدك.")
    