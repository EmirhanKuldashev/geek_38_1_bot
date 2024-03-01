from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,second_questionnaire,third_questionnaire,
    admin_bot

)
from database import bot_db

async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
second_questionnaire.register_second_questionnaire_handlers(dp=dp)
third_questionnaire.register_third_questionnaire_handlers(dp=dp)
admin_bot.register_chat_actions_handler(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup
    )
