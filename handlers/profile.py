import re
import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.bot_db import Database
import const
import random
from keyboards.profile_inline_buttons import (
    like_dislike_keyboard
    )

async def random_filter_profile_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_all_profiles(
        tg_id=call.from_user.id
    )
    print(profiles)
    random_profile = random.choice(profiles)
    with open(random_profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=const.PROFILE_TEXT.format(
                nickname=random_profile['nickname'],
                bio=random_profile['bio'],
                age=random_profile['age'],
                job=random_profile['job'],
                hobby=random_profile['hobby'],
                gender=random_profile['gender'],
            ),
            reply_markup=await like_dislike_keyboard(
                tg_id=random_profile["telegram_id"]
            )
        )

async def detect_like_call(call: types.CallbackQuery):
    await call.message.delete()
    owner = re.sub("like_", "", call.data)
    print(owner)
    db = Database()
    try:
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='U have liked this profile!'
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)
    db.sql_insert_like(
        owner=owner,
        liker=call.from_user.id
    )
    await random_filter_profile_call(call=call)

def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        random_filter_profile_call,
        lambda call: call.data == "random_profiles"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: 'like_' in call.data
    )



