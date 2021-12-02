from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Chuyển tiếp tin nhắn hoặc link đầu tiên từ kênh Database (có trích dẫn)", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Lỗi\n\nTin nhắn /link này không tồn tại hoặc được chuyển tiếp từ kênh Database", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Chuyển tiếp tin nhắn hoặc link cuối cùng từ kênh Database (có trích dẫn)", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Lỗi\n\nTin nhắn /link này không tồn tại hoặc được chuyển tiếp từ kênh Database", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = requests.get(f"https://link1s.com/api?api=9e9c26d7a2a2759289d9f95c84931a0471da7243&url=https://toolpremium.blogspot.com/p/lay-url-luu-tru-telegram.html?link=https://t.me/{client.username}?start={base64_string}").json()['shortenedUrl']
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>✅ LƯU TRỮ THÀNH CÔNG \n\n🔗 Your URL : {link}</b>\n(Vì đây là bản FREE nên cần mở link rút gọn để lấy link lưu trữ, liên hệ <a href='https://fb.com/sang1900>Admin</a> để xoá link rút gọn.)", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    #link = f"https://t.me/{client.username}?start={base64_string}"
    link = requests.get(f"https://link1s.com/api?api=9e9c26d7a2a2759289d9f95c84931a0471da7243&url=https://toolpremium.blogspot.com/p/lay-url-luu-tru-telegram.html?link=https://t.me/{client.username}?start={base64_string}").json()['shortenedUrl']
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>✅ LƯU TRỮ THÀNH CÔNG \n\n🔗 Your URL : {link}</b>\n(Vì đây là bản FREE nên cần mở link rút gọn để lấy link lưu trữ, liên hệ <a href='https://fb.com/sang1900>Admin</a> để xoá link rút gọn.)", quote=True, reply_markup=reply_markup)