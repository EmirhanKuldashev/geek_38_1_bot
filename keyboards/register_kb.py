from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def gen_kb():
    markup = ReplyKeyboardMarkup()
    male = KeyboardButton("male")
    female = KeyboardButton("female")
    undef = KeyboardButton("secret")
    markup.add(male, female, undef)
    return markup