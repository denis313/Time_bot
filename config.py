from aiogram import Bot, Dispatcher


bot_token = "5500745825:AAGB6wu0MYTXv8YuPQc18WStQmdOmzp997U"

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

thread_exb = {'Молитвенные нужды': 128, 'Наставление на день': 13, 'Объявления': 3,
              'Дни рождения': 5, 'Кабинеты': None, 'Записи собраний': 126,
              'Волонтёры': 124, 'Жизнь церкви': 122, 'Расписание служений': 120}

# Для канала ЕХБ
# thread_exb = {'Молитвенные нужды': 7, 'Наставление на день': 64, 'Объявления': None,
#               'Дни рождения': 9, 'Кабинеты': 324, 'Записи собраний': 3,
#               'Волонтёры': 59, 'Жизнь церкви': 61, 'Расписание служений': 57}
