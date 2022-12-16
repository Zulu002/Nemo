"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
chatbot = Bot(token=TOKEN)
dp = Dispatcher(chatbot)
'''Начало бота - команда start.'''
@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.reply("Привет, пиши мне свои сообщения!")


if __name__ == "__main__":
    executor.start_polling(dp)