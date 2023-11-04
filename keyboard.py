from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

'''   
        Создание обьект основной клавиатуры Пользователя и кнопок для основной клавиатуры Пользователя
'''
btn_new = KeyboardButton(text='Добавить новую запись ✅')
btn_all = KeyboardButton(text='Посмотреть все записи 📚')
btn_del = KeyboardButton(text='Удалить запись ❌')

main_keyboard = ReplyKeyboardMarkup(keyboard=[[btn_new], [btn_all, btn_del]],
                                    resize_keyboard=True)


def stop_fsm() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Stop 🛑')]],
                               resize_keyboard=True)


def thread_id():
    btn_1 = KeyboardButton(text='Молитвенные нужды')
    btn_2 = KeyboardButton(text='Наставление на день')
    btn_3 = KeyboardButton(text='Объявления')
    btn_4 = KeyboardButton(text='Дни рождения')
    btn_5 = KeyboardButton(text='Кабинеты')
    btn_6 = KeyboardButton(text='Записи собраний')
    btn_7 = KeyboardButton(text='Волонтёры')
    btn_8 = KeyboardButton(text='Жизнь церкви')
    btn_9 = KeyboardButton(text='Расписание служений')

    return ReplyKeyboardMarkup(keyboard=[[btn_1, btn_2, btn_3],
                                         [btn_4, btn_5, btn_6],
                                         [btn_7, btn_8, btn_9]],
                               resize_keyboard=True)


def months():
    kb_builder = ReplyKeyboardBuilder()

    # Создаем список с кнопками
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=i) for i in ['Январь', 'Февраль', 'Март', 'Апрель',
                                         'Май', 'Июнь', 'Июль', 'Август',
                                         'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    ]
    buttons_2 = KeyboardButton(text='Stop 🛑')
    kb_builder.row(*buttons, width=4)
    return kb_builder.add(buttons_2)


def days(month: str):
    kb_builder = ReplyKeyboardBuilder()

    day_in_month = {'Январь': 31, 'Февраль': 28, 'Март': 31, 'Апрель': 30,
                    'Май': 31, 'Июнь': 30, 'Июль': 31, 'Август': 31,
                    'Сентябрь': 30, 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}
    # Создаем список с кнопками
    buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'{i}') for i in range(1, day_in_month[month]+1)
    ]

    buttons_2 = KeyboardButton(text='Stop 🛑')
    kb_builder.row(*buttons, width=4)
    return kb_builder.add(buttons_2)
