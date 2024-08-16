from asyncpg import UniqueViolationError
from utils.db_api.shemas.ingredients import Ingredients  # Используйте Ingredients вместо Registration
from utils.notify_admins import send_admin
from loader import dp
from loguru import logger


# добавление ингредиентов
async def new_ingredients(number: int, coffee: int, milk: int, raf: int, cacao: int, glass: int, cover: int,
                          syrup: int):
    try:
        ingredients = Ingredients(number=number, coffee=coffee, milk=milk, raf=raf, cacao=cacao, glass=glass,
                                  cover=cover, syrup=syrup)
        await ingredients.create()
    except UniqueViolationError:
        logger.success('Ингредиенты не созданы')


async def update_coffee_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_coffee_value = ingredients.coffee + delta
            await ingredients.update(coffee=new_coffee_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения coffee на {delta}')


async def update_milk_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_milk_value = ingredients.milk + delta
            await ingredients.update(milk=new_milk_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения milk на {delta}')


async def update_raf_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_raf_value = ingredients.raf + delta
            await ingredients.update(raf=new_raf_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения raf на {delta}')


async def update_cacao_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_cacao_value = ingredients.cacao + delta
            await ingredients.update(cacao=new_cacao_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения cacao на {delta}')


async def update_glass_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_glass_value = ingredients.glass + delta
            await ingredients.update(glass=new_glass_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения glass на {delta}')


async def update_syrup_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_syrup_value = ingredients.syrup + delta
            await ingredients.update(syrup=new_syrup_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения syrup на {delta}')


async def get_coffee_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.coffee
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения coffee: {e}')
        return None


async def get_milk_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.milk
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения milk: {e}')
        return None


async def get_raf_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.raf
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения raf: {e}')
        return None


async def get_cacao_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.cacao
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения cacao: {e}')
        return None


async def get_glass_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.glass
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения glass: {e}')
        return None


async def get_syrup_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.syrup
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения syrup: {e}')
        return None


async def change_coffee_value(new_coffee_value: int):
    try:
        await Ingredients.update.values(coffee=new_coffee_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения coffee: {e}')


async def change_milk_value(new_milk_value: int):
    try:
        await Ingredients.update.values(milk=new_milk_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения milk: {e}')


async def change_raf_value(new_raf_value: int):
    try:
        await Ingredients.update.values(raf=new_raf_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения raf: {e}')


async def change_cacao_value(new_cacao_value: int):
    try:
        await Ingredients.update.values(cacao=new_cacao_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения cacao: {e}')


async def change_glass_value(new_glass_value: int):
    try:
        await Ingredients.update.values(glass=new_glass_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения glass: {e}')


async def change_syrup_value(new_syrup_value: int):
    try:
        await Ingredients.update.values(syrup=new_syrup_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения syrup: {e}')


async def update_cover_value(delta: int):
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            new_cover_value = ingredients.cover + delta
            await ingredients.update(cover=new_cover_value).apply()
    except UniqueViolationError:
        await send_admin(dp, f'Ошибка при изменении значения cover на {delta}')


async def get_cover_value():
    try:
        ingredients = await Ingredients.query.where(Ingredients.number == 1).gino.first()

        if ingredients:
            return ingredients.cover
    except Exception as e:
        await send_admin(dp, f'Ошибка при получении значения cover: {e}')
        return None


async def change_cover_value(new_cover_value: int):
    try:
        await Ingredients.update.values(cover=new_cover_value).where(Ingredients.number == 1).gino.status()
    except Exception as e:
        await send_admin(dp, f'Ошибка при изменении значения cover: {e}')
