"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import BotCommand, ReplyKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
import jsone
import config
import apps

chatbot = Bot(token=config.TOKEN)
dp = Dispatcher(chatbot)

'''Начало бота - команда start.'''


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    inline_btn_hello = InlineKeyboardButton('Привет 👋', callback_data='button1')
    inline_btn_reg = InlineKeyboardButton("Регистрация", callback_data="button2")
    inline_btn_qst = InlineKeyboardButton("Оставить вопрос", callback_data="button3")
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_hello, inline_btn_reg, inline_btn_qst)
    await message.reply("Привет, пиши мне свои сообщения!Я с радостью на них отвечу.\n"
                        "Так же ты можешь зарегистрироваться.", reply_markup=inline_kb1)


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи...\n"
                        "/start - Начало бота. Приветствие. 1️⃣\n"
                        "/help - помощь по командам. 2️⃣\n"
                        "/communicaton - общение с модераторами. 3️⃣\n"
                        "/registry - регистрация 4️⃣")


@dp.message_handler(commands=["communication"])
async def mes_communication(message: types.Message):
    button_moder = KeyboardButton("Помощь модератора ☎")
    button_admin = KeyboardButton("Помощь Админа ☎")
    all_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_moder, button_admin)
    await message.reply("Режим общения включен.", reply_markup=all_button)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await chatbot.send_message(callback_query.from_user.id, 'Привет 👋')

@dp.callback_query_handler(lambda c: c.data == "button3")
async def qst_answer(callback_query: types.CallbackQuery):
    await chatbot.send_message(callback_query.from_user.id, "Можете оставить свой вопрос!")

    @dp.message_handler(content_types=["text"])
    async def mess_text(message: types.Message):
        await message.reply(message.text)
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


@dp.message_handler(lambda message: message.text == "Помощь модератора ☎")
async def mes_answer(message: types.Message):
    await message.reply("Запрос отправлен. Ожидайте....")

@dp.message_handler(lambda message: message.text == "Подтвердите ваш номер телефона ☎")
async def mes_answer(message: types.Message):
    await message.reply("SSS")
@dp.message_handler(lambda message: message.text == "Помощь Админа ☎")
async def mes_answer(message: types.Message):
    await message.reply("Запрос отправлен. Ожидайте...")

if __name__ == "__main__":
    executor.start_polling(dp)
