"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

import datetime

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

import apps
import jsone

storage = MemoryStorage()

TOKEN = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
chatbot = Bot(token=TOKEN)
dp = Dispatcher(chatbot, storage=storage)

'''Начало бота - команда start.'''


class UserState(StatesGroup):
    question = State()


'''Начало бота - команда start.'''


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    inline_btn_reg = InlineKeyboardButton("Регистрация", callback_data="button2")
    inline_btn_qst = InlineKeyboardButton("Оставить вопрос", callback_data="button3")
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_reg, inline_btn_qst)
    await message.reply("Привет, пиши мне свои сообщения!Я с радостью на них отвечу.\n"
                        "Так же ты можешь зарегистрироваться.", reply_markup=inline_kb1)


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи...\n"
                        "1️⃣ /start - Запуск бота \n"
                        "2️⃣ /help - помощь по командам. \n"
                        "3️⃣ /communicaton - общение с оператором. \n")


@dp.message_handler(commands=["communication"])
async def mes_communication(message: types.Message):
    button_moder = KeyboardButton("Помощь оператора")
    all_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_moder)
    await message.reply("Режим общения включен.", reply_markup=all_button)


@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await chatbot.send_message(callback_query.from_user.id, "Напиши ваш вопрос.")
    await UserState.question.set()


@dp.message_handler(state=UserState.question)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)
    if message.text.startswith('/'):
        return False
    a = datetime.datetime.now().isoformat()
    apps.Db().insert_message(message.from_user.id, message.text, a)
    await message.answer("Отлично! Ваш запрос был сохранен!")


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    inline_btn_tel = KeyboardButton('Подтвердите ваш номер телефона ☎', request_contact=True)
    bk_reg = ReplyKeyboardMarkup(resize_keyboard=True).add(inline_btn_tel)
    await chatbot.send_message(callback_query.from_user.id, f"Ваш Логин: {callback_query.from_user.id}")
    await chatbot.send_message(callback_query.from_user.id,
                               "Если хотите чтобы вам перезвонили, ответили на вопрос подтвердите свой номер телефона",
                               reply_markup=bk_reg)


@dp.message_handler(commands=["task"])
async def tasks(message: types.Message):
    all_qst = ReplyKeyboardMarkup(row_width=1)
    for i in range(0, len(jsone.get_question_json().keys())):
        button = types.KeyboardButton(f'{list(jsone.get_question_json().keys())[i]}')
        all_qst.add(button)
    await message.reply("Список популярных вопросов:", reply_markup=all_qst)


@dp.message_handler(content_types=['contact'])
async def mes_phone(message: types.Message):
    if message.contact is not None:
        apps.Db().insert_user(message.contact.user_id, message.contact.phone_number, "Telegram")


@dp.message_handler(lambda message: message.text in list(jsone.get_question_json().keys()))
async def answer_qst(message: types.Message):
    await message.reply(jsone.get_question_json().get(message.text))


@dp.message_handler(lambda message: message.text == "Помощь оператора")
async def mes_text(message: types.Message):
    await message.reply("Сейчас к вам подключится оператор.\nОжидайте.....")


@dp.message_handler(lambda message: message.text)
async def mes_fast(message: types.Message):
    key_1 = InlineKeyboardButton("Отменить", callback_data="but5")
    cancel = InlineKeyboardMarkup().add(key_1)
    apps.Db().insert_message(message.from_user.id, message.text, datetime.datetime.now())
    await message.reply("Скоро оператор вам поможет. Ожидайте..", reply_markup=cancel)


@dp.message_handler(lambda message: message.text == "Я не нашел ответ на свой вопрос...")
async def mes_answer(message: types.Message):
    await message.reply("Вам скоро поможет оператор :)")


@dp.callback_query_handler(lambda c: c.data == 'but5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    apps.Db().update_close_quest(callback_query.from_user.id)
    await chatbot.send_message(callback_query.from_user.id, "Вопрос отменен.")


if __name__ == "__main__":
    executor.start_polling(dp)
