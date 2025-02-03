import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

from uroki.text import main_text, lecture_1, lecture_2, lecture_3, lecture_4, lecture_5, end_1, end_2
from admin.adm_rout import admin_rout
from db.CRUD import update_user_status


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp =  Dispatcher()
dp.include_router(admin_rout)


button1 = InlineKeyboardButton(text="📢 Free signals", url="https://t.me/@crypto_bulat")  # Укажи реальную ссылку
button2 = InlineKeyboardButton(text="📞 My YouTube", url="https://www.youtube.com/@cryptobulat")  # Укажи свой канал
button3 = InlineKeyboardButton(text="🔙 I trade here", url="https://t.me/crypto_bulat/524")  # Укажи ссылку
button41 = InlineKeyboardButton(text="Start learning", callback_data="lesson_1")
button42 = InlineKeyboardButton(text="The next lesson", callback_data="lesson_2")
button43 = InlineKeyboardButton(text="The next lesson", callback_data="lesson_3")
button44 = InlineKeyboardButton(text="The next lesson", callback_data="lesson_4")
button45 = InlineKeyboardButton(text="The next lesson", callback_data="lesson_5")
button46 = InlineKeyboardButton(text="The next lesson", callback_data="lesson_6")
button5 = InlineKeyboardButton(text="🏠 To the main menu", callback_data="main_menu")


main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button41],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])
main_inline_keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button42],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])
main_inline_keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button43],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])
main_inline_keyboard4 = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button44],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])
main_inline_keyboard5 = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button45],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])
main_inline_keyboard6 = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button46],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])



@dp.callback_query(lambda c: c.data == "main_menu")
async def main(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard, text = main_text)

@dp.callback_query(lambda c: c.data == "lesson_1")
async def lesson_1(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard2, text = lecture_1)
    print(callback.from_user.id)
    update_user_status(callback.message.from_user.id, "1")


@dp.callback_query(lambda c: c.data == "lesson_2")
async def lesson_2(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard3, text = lecture_2)
    update_user_status(callback.from_user.id, "2")

@dp.callback_query(lambda c: c.data == "lesson_3")
async def lesson_3(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard4, text = lecture_3)
    update_user_status(callback.from_user.id, "3")

@dp.callback_query(lambda c: c.data == "lesson_4")
async def lesson_4(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard5, text = lecture_4)
    update_user_status(callback.from_user.id, "4")

@dp.callback_query(lambda c: c.data == "lesson_5")
async def lesson_5message(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard6, text = lecture_5)
    update_user_status(callback.from_user.id, "5")

@dp.callback_query(lambda c: c.data == "lesson_6")
async def lesson_6message(callback: types.CallbackQuery):
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard, text = end_1)
    await bot.send_message(callback.message.chat.id, reply_markup=main_inline_keyboard, text=end_2)
    update_user_status(callback.from_user.id, "end")


async def create():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(create())