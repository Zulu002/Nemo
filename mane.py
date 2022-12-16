"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import BotCommand, ReplyKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text

TOKEN = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
chatbot = Bot(token=TOKEN)
dp = Dispatcher(chatbot)

'''Начало бота - команда start.'''
@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    inline_btn_hello = InlineKeyboardButton('Привет 👋', callback_data='button1')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_hello)
    await message.reply("Привет, пиши мне свои сообщения!Я с радостью на них отвечу.", reply_markup=inline_kb1)

@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    await message.reply("Перечень команд для твоей помощи...\n"
                        "/start - Начало бота. Приветствие. 1️⃣\n"
                        "/help - помощь по командам. 2️⃣\n"
                        "/communicaton - общение с модераторами. 3️⃣")
@dp.message_handler(commands=["communication"])
async def mes_communication(message: types.Message):
    button_moder = KeyboardButton("Помощь модератора ☎")
    button_admin = KeyboardButton("Помощь Админа ☎")
    all_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_moder, button_admin)
    await message.reply("Режим общения включен.", reply_markup=all_button)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await chatbot.send_message(callback_query.from_user.id, 'Привет 👋')

@dp.message_handler(lambda message: message.text == "Помощь модератора ☎")
async def mes_answer(message: types.Message):
    await message.reply("Запрос отправлен. Ожидайте....")

@dp.message_handler(lambda message: message.text == "Помощь Админа ☎")
async def mes_answer(message: types.Message):
    await message.reply("Запрос отправлен. Ожидайте....")
if __name__ == "__main__":
    executor.start_polling(dp)