from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.config import admins
from handlers.users.inline_menu import generate_ingredients_keyboard  # Update the import
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    user_id = message.from_user.id
    try:
        user = await commands.select_user(user_id)
        if user.status == 'active':
            ikb_menu = await generate_ingredients_keyboard()
            await message.answer(f'Ингридиенты:', reply_markup=ikb_menu)
        elif user.status == 'banned':
            await message.answer('Нет доступа')
    except Exception:
        await commands.add_user(user_id=user_id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                referral_id=0,
                                status='banned',
                                balance=0)
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer(f'Ингридиенты:', reply_markup=ikb_menu)
