from utils.db_api.ingredients_commands import new_ingredients
from loguru import logger

logger.add("logs/file.log", format="{time} {level} {message}", level="DEBUG", rotation="50 MB", compression="zip")


async def on_startup(dp):
    from loader import db
    from utils.db_api.db_gino import on_startup
    await on_startup(db)

    # logger.success('Удаление базы данных')
    # await db.gino.drop_all()

    await db.gino.create_all()

    # импортирует функцию, которая устанавливает команды бота
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    # выдает в консоль бот запущен
    logger.success('Бот запущен')

    await new_ingredients(1, 1, 1, 1, 1, 1, 1, 1)


if __name__ == '__main__':
    try:
        from aiogram import executor  # импортируем executor для запуска поллинга
        from handlers import dp  # из хендлеров импортируем dp

        executor.start_polling(dp, on_startup=on_startup)
    except Exception as e:
        logger.exception(e)
