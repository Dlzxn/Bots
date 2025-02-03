import sqlite3
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio


# 🔹 Подключаемся к базе и создаем таблицу

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER UNIQUE,
#     username TEXT,
#     status TEXT
#
# )
# """)

# 🔹 Функция для добавления пользователя в БД
def add_user(user_id, username, status = "0"):
    conn = sqlite3.connect("bot_database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (user_id, username, status) VALUES (?, ?, ?)",
                       (user_id, username, status))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Если юзер уже есть, не добавляем
    finally:
        conn.close()


def update_user_status(user_id, new_status):
    try:
        conn = sqlite3.connect("bot_database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (new_status, user_id))
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)

    finally:
        conn.close()


def get_all_users():
    conn = sqlite3.connect("bot_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, status FROM users")
    users = cursor.fetchall()  # Получаем все записи
    user_list = []

    for user in users:
        message: str = f"""
        Айди: {user[0]} \n
        Username: {user[1]} \n
        Блок: {user[2]}
        """


        user_list.append(message)

    conn.close()
    return user_list