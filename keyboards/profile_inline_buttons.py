from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

async def like_dislike_keyboard(tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like",
        callback_data=f"like_{tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike",
        callback_data="random_profiles"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup
