from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

BOT_TOKEN = "8311848343:AAFnGIc9gG-aFtzSWEmVF2kbkV-TYF_b9xQ"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🎵 YouTube Music", callback_data="youtube_music"),
            InlineKeyboardButton(text="🔍 Google Search", callback_data="google_search"),
        ],
        [
            InlineKeyboardButton(text="📸 Instagram", callback_data="instagram"),
            InlineKeyboardButton(text="✈️ Telegram", callback_data="telegram", url="https://t.me/maxmudov_1117"),
            InlineKeyboardButton(text="📘 Facebook", callback_data="facebook"),
        ],
        [
            InlineKeyboardButton(text="🐦 Twitter", callback_data="twitter"),
            InlineKeyboardButton(text="🎬 TikTok", callback_data="tiktok"),
        ],
        [
            InlineKeyboardButton(text="🎧 Spotify", callback_data="spotify"),
            InlineKeyboardButton(text="🍿 Netflix", callback_data="netflix"),
            InlineKeyboardButton(text="💻 GitHub", callback_data="github"),
        ],
        [
         InlineKeyboardButton(text="❓ Yordam", callback_data="help"),
         InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="settings"),
         InlineKeyboardButton(text="📊 Statistika", callback_data="stats"),
         ]
    ])

def back_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
    ])

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Xush kelibsiz! Menyudan tanlang:", reply_markup=main_menu())

@dp.callback_query(F.data == "back")
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text("Asosiy menyu:", reply_markup=main_menu())
    await callback.answer()

@dp.callback_query(F.data == "stats")
async def stats_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📊 Statistika:\nFoydalanuvchilar: 1000\nXabarlar: 5000",
        reply_markup=back_menu()
    )
    await callback.answer()

@dp.callback_query(F.data == "settings")
async def settings_handler(callback: types.CallbackQuery):
    settings_menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Bildirishnomalar", callback_data="notifications")],
        [InlineKeyboardButton(text="🌐 Til", callback_data="language")],
        [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
    ])
    await callback.message.edit_text("⚙️ Sozlamalar:", reply_markup=settings_menu)
    await callback.answer()

async def main():
    print('Bot  ishga tushdi')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())