from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
async def third_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    books_button = InlineKeyboardButton(
        "Books",
        callback_data="books"
    )
    movies_button = InlineKeyboardButton(
        "Movies",
        callback_data="movies"
    )
    markup.add(books_button)
    markup.add(movies_button)
    return markup

