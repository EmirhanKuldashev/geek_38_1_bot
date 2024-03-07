import sqlite3
from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards import start_inline_buttons
import const
from scraping.news_scraper import NewsScraper

async def start_button(message: types.Message):
    print(message)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=const.START_MENU_TEXT.format(
            user=message.from_user.first_name
        ),
        reply_markup=await start_inline_buttons.start_keyboard()
    )

async def latest_news_call(call: types.CallbackQuery):
    scraper = NewsScraper()
    db = bot_db.Database()
    data = scraper.scrape_data()
    print()
    for link in data[:5]:
        db.sql_insert_news(
            tg_id=call.from_user.id,
            link=link
        )
    for i in data[:5]:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=scraper.PLUS_URL + i
        )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_button,
        commands=['start']
    )
    dp.register_callback_query_handler(
        latest_news_call,
        lambda call: call.data == "latest_news"
    )

