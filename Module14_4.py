from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import sys
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions14_4 import *

initiate_db()
products = get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


with open('Token.txt', 'r', encoding='UTF-8') as f:
    api = f.read()
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Рассчитать'),
            KeyboardButton('Информация')
        ],
        [
            KeyboardButton('Купить')
        ]
    ], resize_keyboard=True
)

ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton('Формулы расчёта', callback_data='formulas')],
    ]
)

buy_ikm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Продукт1', callback_data='product_buying'),
            InlineKeyboardButton('Продукт2', callback_data='product_buying'),
            InlineKeyboardButton('Продукт3', callback_data='product_buying'),
            InlineKeyboardButton('Продукт4', callback_data='product_buying')
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=start_menu)


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # logging.info(data)
    await state.finish()
    result = float(data['weight']) * 10 + float(data['growth']) * 6.25 - int(data['age']) * 5 + 5
    await message.answer(f'Ваша норма калорий {result}')


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('Мумиё.webp', 'rb') as img:
        await message.answer_photo(img, f'{get_all_products()[0]}')

    with open('Прополис.webp', 'rb') as img:
        await message.answer_photo(img, f'{get_all_products()[1]}')

    with open('Кумыс.webp', 'rb') as img:
        await message.answer_photo(img, f'{get_all_products()[2]}')

    with open('Алоэ-вера.webp', 'rb') as img:
        await message.answer_photo(img, f'{get_all_products()[3]}')

    await message.answer('Выберите продукт для покупки:', reply_markup=buy_ikm)
    connection.commit()
    connection.close()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikm)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    executor.start_polling(dp, skip_updates=True)
