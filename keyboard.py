from aiogram import types


class Keyboard:
    def __init__(self):
        pass

    def main(self):
        keyboard_main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        steam = types.KeyboardButton(text='Get last steam game')
        keyboard_main.add(steam)
        return keyboard_main
