from aiogram import types, Dispatcher
from config import bot
from database import bot_db
from keyboards import start_inline_buttons
import const
from profanity_check import predict, predict_prob

async def check_group(message: types.Message):
    db = bot_db.Database()
    ban_words_prob = predict_prob([message.text])
    if ban_words_prob > 0.8:
        if not db.sql_select_ban_user(message.from_user.id):
            db.sql_insert_ban(message.from_user.id)
            await message.answer(f"Don't swear @{message.from_user.username}, you can be banned from this group ")
            await bot.delete_message(message.chat.id, message.message_id)

        elif db.sql_select_ban_user(message.from_user.id)["count"] >=3:
            await bot.kick_chat_member(message.chat.id,message.from_user.id)
            await bot.send_message(message.from_user.id, text=const.BOT_KICKED_TEXT)
        else:
            db.sql_update_ban_user(message.from_user.id)
            await message.answer(f"Don't swear @{message.from_user.username}, it's not the first time you've cursed ")
            await bot.delete_message(message.chat.id, message.message_id)

async def check_ban(call : types.CallbackQuery):
    db = bot_db.Database()
    user = db.sql_select_ban_user(call.from_user.id)
    if not user:
        text = f"you don't have any warnings"
        await call.message.answer(text)
    else:
        text = f"your number of warnings: {user['count']},be careful "
    await call.message.answer(text)


def register_chat_actions_handler(dp: Dispatcher):
    dp.register_callback_query_handler(check_ban,
            lambda call: call.data == "check_ban")
    dp.register_message_handler(
        check_group
    )