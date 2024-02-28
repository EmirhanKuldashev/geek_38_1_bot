from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
async def second_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    soda_button = InlineKeyboardButton(
        "Soda",
        callback_data="soda"
    )
    still_water_button = InlineKeyboardButton(
        "Still water",
        callback_data="still_water"
    )
    markup.add(soda_button)
    markup.add(still_water_button)
    return markup
