from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )

    second_questionnaire_button = InlineKeyboardButton(
        "Second questionnaire",
        callback_data="start_second_questionnaire"
    )
    third_questionnaire_button = InlineKeyboardButton(
        "Third questionnaire",
        callback_data="start_third_questionnaire"
    )
    check_bun_button = InlineKeyboardButton(
        "Check ban",
        callback_data="check_ban"
    )
    register_button = InlineKeyboardButton(
        "Register",
        callback_data="register"
    )
    profiles_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="random_profiles"
    )
    news_button = InlineKeyboardButton(
        "Latest News",
        callback_data="latest_news"
    )

    markup.add(questionnaire_button)
    markup.add(second_questionnaire_button)
    markup.add(third_questionnaire_button)
    markup.add(check_bun_button)
    markup.add(register_button)
    markup.add(profiles_button)
    markup.add(news_button)
    return markup
