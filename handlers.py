from bd import insert_data, all_data, del_data
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboard import main_keyboard, stop_fsm, thread_id, months, days


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('🤖 Бот позволяет отправлять сообщения по дате в разные темы.\n\n'
                         'ФУНКЦИОНАЛ:\n'
                         ' <b>"Добавить новую запись ✅"</b> - необходимо ввести нужные данные.\n'
                         ' <b>"Посмотреть все записи 📚"</b> - возможность посмотреть все существующие записи.\n'
                         ' <b>"Удалить запись ❌"</b> - необходимо ввести id_data для удаления определенной записи.\n'
                         ' <b>"Stop 🛑"</b> - прекращает выполнение функций:'
                         ' <b>"Добавить новую запись ✅"</b> и <b>"Удалить запись ❌"</b>',
                         reply_markup=main_keyboard,
                         parse_mode='html')


class NewData(StatesGroup):
    subject = State()
    month = State()
    day = State()
    text_message = State()


@router.message(F.text == 'Stop 🛑')
async def process_gender_press(message: Message, state: FSMContext):
    await message.answer('Заполние прекращено', reply_markup=main_keyboard)
    await state.clear()


@router.message(F.text == 'Добавить новую запись ✅')
async def search_book(message: Message, state: FSMContext):
    await state.set_state(NewData.subject)
    await message.answer(text="В какую тему отправить сообщение:", reply_markup=thread_id())


@router.message(NewData.subject)
async def search_name_book(message: Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(NewData.month)
    await message.answer('Выберите месяц отправки сообщения:',
                         reply_markup=months().as_markup(resize_keyboard=True))


@router.message(NewData.month)
async def search_name_book(message: Message, state: FSMContext):
    await state.update_data(month=message.text)
    await state.set_state(NewData.day)
    await message.answer('Выберите день отправки сообщения:',
                         reply_markup=days(month=message.text).as_markup(resize_keyboard=True))


@router.message(NewData.day)
async def search_author_book(message: Message, state: FSMContext):
    await state.update_data(day=message.text)
    await state.set_state(NewData.text_message)
    await message.answer('Введите текст записи:', reply_markup=main_keyboard)


@router.message(NewData.text_message)
async def search_author_book(message: Message, state: FSMContext):
    await state.update_data(text_message=message.text)
    data = await state.get_data()
    await state.clear()
    month = {'Январь': '01', 'Февраль': '02', 'Март': '03', 'Апрель': '04',
             'Май': '05', 'Июнь': '06', 'Июль': '07', 'Август': '08',
             'Сентябрь': '09', 'Октябрь': '10', 'Ноябрь': '11', 'Декабрь': '12'}
    dispatch_time = f'2023-{month[data["month"]]}-{data["day"]}'
    insert_data(data['subject'], dispatch_time, data['text_message'])
    await message.answer('Запись создана ✅', reply_markup=main_keyboard)


@router.message(F.text == 'Посмотреть все записи 📚')
async def search_book(message: Message):
    records = all_data()
    count = 0
    for record in records:
        id_book, subject, dispatch_time, text_message = record
        count += 1
        await message.answer(text=f'ЗАПИСЬ №{count}\n\n'
                                  f'🆔 id_data записи: {id_book}\n'
                                  f'💡 Тема записи: {subject}\n'
                                  f'🕓 Время записи : {dispatch_time}\n'
                                  f'📖 Текст записи: {text_message}')


class DelData(StatesGroup):
    id_data = State()


@router.message(F.text == 'Удалить запись ❌')
async def delete_datas(message: Message, state: FSMContext):
    await state.set_state(DelData.id_data)
    await message.answer('Введите id_data записи:', reply_markup=stop_fsm())


@router.message(DelData.id_data)
async def id_del_data(message: Message, state: FSMContext):
    await state.update_data(id_data=message.text)
    data = await state.get_data()
    await state.clear()
    del_data(data['id_data'])
    await message.answer('Запись удалена ❌', reply_markup=main_keyboard)
