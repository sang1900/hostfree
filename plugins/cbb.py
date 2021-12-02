from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import requests
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>• Tạo Bởi <a href='https://fb.com/sang1900'>Nguyễn Sáng</a>\n• Giới Thiệu :</b> Bot này được tạo ra nhắm mục đích lưu trữ dữ liệu trên Telegram. Nó có có thể lưu trữ không giới hạn bất cứ thứ gì mà bạn gửi cho nó.\n\n<b>• CÁC PHIÊN BẢN CỦA BOT\nUpdate ....</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Đóng", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass