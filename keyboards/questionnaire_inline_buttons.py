from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    english_button = InlineKeyboardButton(
        "English",
        callback_data="english"
    )
    german_button = InlineKeyboardButton(
        "German",
        callback_data="german"
    )
    markup.add(english_button)
    markup.add(german_button)
    return markup


async def english_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    english_yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes_english"
    )
    english_no_button = InlineKeyboardButton(
        "No",
        callback_data="no_english"
    )
    markup.add(english_yes_button)
    markup.add(english_no_button)
    return markup
