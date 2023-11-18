from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


'''   
        Создание обьект основной клавиатуры Пользователя и кнопок для основной клавиатуры Пользователя
'''
btn_new = KeyboardButton(text='Добавить новую запись ✅')
btn_all = KeyboardButton(text='Посмотреть все записи 📚')
btn_del = KeyboardButton(text='Удалить запись ❌')

main_keyboard = ReplyKeyboardMarkup(keyboard=[[btn_new], [btn_all, btn_del]],
                                    resize_keyboard=True)


stop_button = KeyboardButton(text='Stop 🛑')


def stop_fsm() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[stop_button]],
                               resize_keyboard=True)


def thread_id():
    kb_builder = ReplyKeyboardBuilder()

    # Создаем список с кнопками
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=i) for i in ['Молитвенные нужды', 'Наставления на день', 'Объявления', 'Дни рождения',
                                         'Кабинеты', 'Записи собрания', 'Волонтеры', 'Жизнь церкви',
                                         'Расписание служений']
    ]
    kb_builder.row(*buttons, width=3)

    return kb_builder.row(stop_button)


def months():
    kb_builder = ReplyKeyboardBuilder()

    # Создаем список с кнопками
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=i) for i in ['Январь', 'Февраль', 'Март', 'Апрель',
                                         'Май', 'Июнь', 'Июль', 'Август',
                                         'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    ]

    kb_builder.row(*buttons, width=4)

    return kb_builder.row(stop_button)


def days(month: str):
    kb_builder = ReplyKeyboardBuilder()

    day_in_month = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30,
                    'Май': 31, 'Июнь': 30, 'Июль': 31, 'Август': 31,
                    'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}

    # Создаем список с кнопками
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'{i}') for i in range(1, day_in_month[month]+1)
    ]

    kb_builder.row(*buttons, width=4)
    return kb_builder.row(stop_button)
