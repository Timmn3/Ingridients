from aiogram.types import CallbackQuery
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher import FSMContext
from utils.db_api.ingredients_commands import get_coffee_value, get_milk_value, get_raf_value, get_cacao_value, \
    get_glass_value, get_syrup_value, update_syrup_value, update_glass_value, update_cacao_value, update_raf_value, \
    update_milk_value, update_coffee_value, change_coffee_value, change_syrup_value, change_glass_value, \
    change_cacao_value, change_raf_value, change_milk_value, update_cover_value, change_cover_value, get_cover_value
from utils.notify_admins import send_admin
from aiogram.dispatcher.filters.state import StatesGroup, State


async def generate_ingredients_keyboard():
    ikb_menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="+", callback_data='+coffee'),
            InlineKeyboardButton(text="Кофе", callback_data='coffee'),
            InlineKeyboardButton(text=str(await get_coffee_value()), callback_data='coffee'),
            InlineKeyboardButton(text="-", callback_data='-coffee'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+milk'),
            InlineKeyboardButton(text="Молоко", callback_data='milk'),
            InlineKeyboardButton(text=str(await get_milk_value()), callback_data='milk'),
            InlineKeyboardButton(text="-", callback_data='-milk'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+raf'),
            InlineKeyboardButton(text="РАФ", callback_data='raf'),
            InlineKeyboardButton(text=str(await get_raf_value()), callback_data='raf'),
            InlineKeyboardButton(text="-", callback_data='-raf'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+cacao'),
            InlineKeyboardButton(text="Какао", callback_data='cacao'),
            InlineKeyboardButton(text=str(await get_cacao_value()), callback_data='cacao'),
            InlineKeyboardButton(text="-", callback_data='-cacao'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+glass'),
            InlineKeyboardButton(text="Стакан", callback_data='glass'),
            InlineKeyboardButton(text=str(await get_glass_value()), callback_data='glass'),
            InlineKeyboardButton(text="-", callback_data='-glass'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+cover'),
            InlineKeyboardButton(text="Крышки", callback_data='cover'),
            InlineKeyboardButton(text=str(await get_cover_value()), callback_data='cover'),
            InlineKeyboardButton(text="-", callback_data='-cover'),
        ],
        [
            InlineKeyboardButton(text="+", callback_data='+syrup'),
            InlineKeyboardButton(text="Сироп", callback_data='syrup'),
            InlineKeyboardButton(text=str(await get_syrup_value()), callback_data='syrup'),
            InlineKeyboardButton(text="-", callback_data='-syrup'),
        ],
    ])

    return ikb_menu


# Предполагается, что функция generate_ingredients_keyboard доступна в вашем модуле

@dp.callback_query_handler(text="-coffee")
async def decrease_coffee(call: CallbackQuery):
    try:
        await update_coffee_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения coffee: {e}')


@dp.callback_query_handler(text="+coffee")
async def increase_coffee(call: CallbackQuery):
    try:
        await update_coffee_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения coffee: {e}')


@dp.callback_query_handler(text="-milk")
async def decrease_milk(call: CallbackQuery):
    try:
        await update_milk_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения milk: {e}')


@dp.callback_query_handler(text="+milk")
async def increase_milk(call: CallbackQuery):
    try:
        await update_milk_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения milk: {e}')


@dp.callback_query_handler(text="-raf")
async def decrease_raf(call: CallbackQuery):
    try:
        await update_raf_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения raf: {e}')


@dp.callback_query_handler(text="+raf")
async def increase_raf(call: CallbackQuery):
    try:
        await update_raf_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения raf: {e}')


@dp.callback_query_handler(text="-cacao")
async def decrease_cacao(call: CallbackQuery):
    try:
        await update_cacao_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения cacao: {e}')


@dp.callback_query_handler(text="+cacao")
async def increase_cacao(call: CallbackQuery):
    try:
        await update_cacao_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения cacao: {e}')


@dp.callback_query_handler(text="-glass")
async def decrease_glass(call: CallbackQuery):
    try:
        await update_glass_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения glass: {e}')


@dp.callback_query_handler(text="+glass")
async def increase_glass(call: CallbackQuery):
    try:
        await update_glass_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения glass: {e}')


@dp.callback_query_handler(text="-cover")
async def decrease_cover(call: CallbackQuery):
    try:
        await update_cover_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения cover: {e}')


@dp.callback_query_handler(text="+cover")
async def increase_cover(call: CallbackQuery):
    try:
        await update_cover_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения cover: {e}')


@dp.callback_query_handler(text="-syrup")
async def decrease_syrup(call: CallbackQuery):
    try:
        await update_syrup_value(-1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при уменьшении значения syrup: {e}')


@dp.callback_query_handler(text="+syrup")
async def increase_syrup(call: CallbackQuery):
    try:
        await update_syrup_value(1)
        ikb_menu = await generate_ingredients_keyboard()
        await call.message.edit_reply_markup(reply_markup=ikb_menu)
    except Exception as e:
        await send_admin(dp, f'Ошибка при увеличении значения syrup: {e}')


# Добавляем состояние для отслеживания ввода количества кофе
class Change(StatesGroup):
    amount_coffee = State()
    amount_milk = State()
    amount_raf = State()
    amount_cacao = State()
    amount_glass = State()
    amount_syrup = State()
    amount_cover = State()


@dp.callback_query_handler(text="coffee")
async def coffee_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества кофе:")
    await Change.amount_coffee.set()


@dp.message_handler(state=Change.amount_coffee)
async def set_coffee_amount(message: Message, state: FSMContext):
    try:
        await change_coffee_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения coffee: {e}')


@dp.callback_query_handler(text="milk")
async def milk_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества молока:")
    await Change.amount_milk.set()


@dp.message_handler(state=Change.amount_milk)
async def set_milk_amount(message: Message, state: FSMContext):
    try:
        await change_milk_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения milk: {e}')


@dp.callback_query_handler(text="raf")
async def raf_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества рафа:")
    await Change.amount_raf.set()


@dp.message_handler(state=Change.amount_raf)
async def set_raf_amount(message: Message, state: FSMContext):
    try:
        await change_raf_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения raf: {e}')


@dp.callback_query_handler(text="cacao")
async def cacao_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества какао:")
    await Change.amount_cacao.set()


@dp.message_handler(state=Change.amount_cacao)
async def set_cacao_amount(message: Message, state: FSMContext):
    try:
        await change_cacao_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения cacao: {e}')


@dp.callback_query_handler(text="glass")
async def glass_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества стаканов:")
    await Change.amount_glass.set()


@dp.message_handler(state=Change.amount_glass)
async def set_glass_amount(message: Message, state: FSMContext):
    try:
        await change_glass_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения glass: {e}')


@dp.callback_query_handler(text="cover")
async def cover_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение для количества cover:")
    await Change.amount_cover.set()


@dp.message_handler(state=Change.amount_cover)
async def set_cover_amount(message: Message, state: FSMContext):
    try:
        await change_cover_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения cover: {e}')


@dp.callback_query_handler(text="syrup")
async def syrup_callback(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите новое значение количества сиропа:")
    await Change.amount_syrup.set()


@dp.message_handler(state=Change.amount_syrup)
async def set_syrup_amount(message: Message, state: FSMContext):
    try:
        await change_syrup_value(int(message.text))
        await message.delete()
        ikb_menu = await generate_ingredients_keyboard()
        await message.answer('Ингредиенты:', reply_markup=ikb_menu)
        await state.finish()
    except ValueError:
        await message.answer("Неверный формат ввода. Пожалуйста, введите целое число.")
    except Exception as e:
        await send_admin(dp, f'Ошибка при обновлении значения syrup: {e}')
