import logging

from aiogram import Dispatcher

from data.config import admins


async def on_startup_notufy(dp: Dispatcher):
    for admin in admins:
        try:
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)


async def send_admin(dp: Dispatcher, text):
    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
