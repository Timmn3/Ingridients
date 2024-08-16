from asyncpg import UniqueViolationError
from loguru import logger
from utils.db_api.db_gino import db
from utils.db_api.shemas.user import User


# добавление пользователя
async def add_user(user_id: int, first_name: str, last_name: str, username: str, referral_id: int, status: str,
                   balance: float):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username,
                    referral_id=referral_id, status=status, balance=balance)
        await user.create()
    except UniqueViolationError:
        logger.success('Пользователь не добавлен')


# выбрать всех пользователей
async def select_all_users():
    users = await User.query.gino.all()
    return users


# подсчет количества пользователей
async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


# выбрать пользователя
async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


# обновляет имя пользователя
async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()


# функция, которая возвращает количество рефералов
async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()  # получаем запрос в массив рефералов user_id
    return len(refs)


# функция для проверки аргументов переданных при регистрации
async def check_args(args, user_id: int):
    if args == '':  # если в аргумент передана пустая строка
        args = '0'
        return args

    elif not args.isnumeric():  # если не только цифры, а и буквы
        args = '0'
        return args

    elif args.isnumeric():  # если только цифры
        if int(args) == user_id:  # если аргумент является id пользователя
            args = '0'
            return args
        # получаем из БД пользователя у которого user_id такой же, как и переданный аргумент
        elif await select_user(user_id=int(args)) is None:  # если его нет
            args = '0'
            return args

        else:  # если аргумент прошел все проверки
            args = str(args)
            return args

    else:  # если что-то пошло не так
        args = '0'
        return args


async def change_balance(user_id: int, amount):  # функция изменения баланса
    user = await select_user(user_id)
    new_balance = user.balance + amount
    await user.update(balance=new_balance).apply()


async def check_balance(user_id: int, amount):  # функция для проверки баланса
    user = await select_user(user_id=user_id)  # получаем юзера
    try:
        amount = float(amount)  # переводим строку в число
        if user.balance + amount >= 0:
            await change_balance(user_id, amount)
            return True  # Если у пользователя есть деньги
        elif user.balance + amount < 0:
            return 'no money'  # если у пользователя нет денег
    except Exception:  # Если передаем буквы в строке
        return False
