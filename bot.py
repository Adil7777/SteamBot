from aiogram import Bot, Dispatcher, executor
import logging
import config
import asyncio
from db import DataBase
from parser_ import Parser

from keyboard import Keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
db = DataBase()
db.init_db()
parse = Parser('game.txt')

keyboard = Keyboard()


@dp.message_handler(commands=['start'])
async def start(message):
    if not db.subscriber_exist(message.chat.id):
        db.add_user(message.chat.id, True)
    await bot.send_message(message.chat.id, 'Welcome', reply_markup=keyboard.main())


@dp.message_handler(content_types=['text'])
async def msg(message):
    text = message.text
    # print(db.subscriber_exist(message.chat.id))
    if text == 'Subscribe' and not db.subscriber_exist(message.chat.id):
        db.add_user(message.chat.id, True)
        print('ds')
        await bot.send_message(message.chat.id, 'Subcsrribed', reply_markup=keyboard.main())
    elif text == 'Unsubscribe':
        db.delete_user(message.chat.id)
        await bot.send_message(message.chat.id, 'Unsubscribed', reply_markup=keyboard.main())
    elif text == 'Get last steam game':
        await bot.send_message(message.chat.id, open('game.txt', 'r').read(), reply_markup=keyboard.main())


async def schedule(wait_for):
    while 1:
        await asyncio.sleep(wait_for)
        # await bot.send_message(755715325, 'ok', disable_notification=True)

        user_ids = db.get_users()
        if parse.new_game():
            text = parse.get_game()

            print(user_ids)

            for user_id in user_ids:
                await bot.send_message(user_id, text, disable_notification=True)


if __name__ == '__main__':
    print('program starting')
    dp.loop.create_task(schedule(10))
    executor.start_polling(dp, skip_updates=True)
