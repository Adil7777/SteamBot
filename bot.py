"""import tools"""
from aiogram import Bot, Dispatcher, executor
import logging

from keyboard import Keyboard

"""Initialization"""

logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

keyboard = Keyboard()


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Welcome', reply_markup=keyboard.main())


@dp.message_handler(content_types=['text'])
async def msg(message):
    await bot.send_message(message.chat.id, 'Getting', reply_markup=keyboard_main)


if __name__ == "__main__":
    print('program starting')
    executor.start_polling(dp, skip_updates=True)
