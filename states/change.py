from aiogram.dispatcher.filters.state import StatesGroup, State


class Change(StatesGroup):
    amount = State()
