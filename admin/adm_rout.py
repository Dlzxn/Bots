from aiogram import Router, F
from aiogram.filters import Filter, Command
from aiogram import types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

from db.CRUD import add_user, get_all_users

from uroki.text import main_text, lecture_1, lecture_2, lecture_3, lecture_4, lecture_5, end_1, end_2

button1 = InlineKeyboardButton(text="📢 Бесплатные сигналы", url="https://t.me/@crypto_bulat")  # Укажи реальную ссылку
button2 = InlineKeyboardButton(text="📞 Мой YouTube", url="https://www.youtube.com/@cryptobulat")  # Укажи свой канал
button3 = InlineKeyboardButton(text="🔙 Я торгую здесь", url="https://t.me/crypto_bulat/524")  # Укажи ссылку
button41 = InlineKeyboardButton(text="Начать обучение", callback_data="lesson_1")
button5 = InlineKeyboardButton(text="🏠 В главное меню", callback_data="main_menu")
button6 = InlineKeyboardButton(text="Рассылка", callback_data="pars")

state = []


main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [button1, button2],  # Первая строка (две кнопки)
    [button3],  # Вторая строка (одна кнопка)
    [button41],  # Третья строка (одна кнопка)
    [button5]   # Четвертая строка (одна кнопка)
])

admin_rout = Router()


button41 = InlineKeyboardButton(text="Статистика", callback_data="stat")
button42 = InlineKeyboardButton(text="Пользователи", callback_data="users")

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [button41, button42],
    [button6] ,
])

USERS_TRUE:list = ["illgettomorow", "limonchaser"]

@admin_rout.message(Command("admin"))
async def start(message: types.Message):
    if message.from_user.username in USERS_TRUE:
        await message.answer(text = "Вы админ", reply_markup=main_keyboard)
    else:
        await message.answer(text = "Запрещено")



@admin_rout.callback_query(lambda c: c.data == "pars")
async def pars(callback: CallbackQuery):
        await callback.answer(text = "Введите сообщение")
        global state
        state.append("True")
        await asyncio.sleep(200)
        state = []

@admin_rout.callback_query(lambda c: c.data == "users")
async def stat(callback: CallbackQuery):
    sp = get_all_users()
    for i in range(len(sp)):
        await callback.message.answer(sp[i])


@admin_rout.callback_query(lambda c: c.data == "stat")
async def stat(callback: CallbackQuery):
    sp = get_all_users()
    block_None = 0
    block_1 = 0
    block_2 = 0
    block_3 = 0
    block_4 = 0
    block_5 = 0
    block_6 = 0
    for i in range(len(sp)):
        k = sp[i].split()[5]
        print(f"ЭТО K {k}")
        if k == "0":
            block_None += 1
        if k == "1":
            block_1 += 1

        if k == "2":
            block_2 += 1

        if k == "3":
            block_3 += 1
        if k == "4":
            block_4 += 1
        if k == "5":
            block_5 += 1
        if k == "end":
            block_6 += 1

    message = f""" Не прошли: {block_None}\nНа первом блоке: {block_1}\n На втором блоке: {block_2}\nНа третьем блоке: 
{block_3}\nНа четвертом блоке: {block_4}\nНа пятом блоке: {block_5}\nНа последнем блоке: {block_6}\n
    
            """
    await callback.message.answer(message)



@admin_rout.message()
async def main(message: Message, bot: Bot):

    await message.answer(reply_markup=main_inline_keyboard, text = main_text)
    print(message.from_user.id)
    try:
        add_user(message.from_user.id, message.from_user.username)
    except Exception as e:
        print("[ERROR]", e)
        add_user(message.from_user.id, None, None)

    finally:
        print("IN finnaly")
        if message.from_user.username in USERS_TRUE:
            print("ivi up")
            global state
            print("STATUS:", state)
            if len(state) == 1:
                print("lvl up")
                all_users = get_all_users()
                for user in all_users:
                    print(user.split())
                    await bot.send_message(user.split()[1], text = message.text)
                state = []
