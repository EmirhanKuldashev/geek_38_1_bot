from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons

async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="English or German language?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )

async def english_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh cool, i learn English too\n"
             "Do you want to learn other languages ?",
        reply_markup=await questionnaire_inline_buttons.english_questionnaire_keyboard()
    )
async def german_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="A good choice! now it is a very popular language"
    )

async def yes_english_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Learning foreign languages is great!"
    )

async def no_english_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I advise you to learn more foreign languages"
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        english_answer,
        lambda call: call.data == "english"
    )
    dp.register_callback_query_handler(
        german_answer,
        lambda call: call.data == "german"
    )
    dp.register_callback_query_handler(
        yes_english_answer,
        lambda call: call.data == "yes_english"
    )
    dp.register_callback_query_handler(
        no_english_answer,
        lambda call: call.data == "no_english"
    )