from aiogram import types, Dispatcher
from config import bot
from keyboards import third_questionnaire_inline_buttons

async def third_questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Books or Movies?",
        reply_markup=await third_questionnaire_inline_buttons.third_questionnaire_keyboard()
    )

async def books_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, books have a good effect on memory!",
    )

async def movies_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Cool, movies help you relax!",
    )

def register_third_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        third_questionnaire_start,
        lambda call: call.data == "start_third_questionnaire"
    )
    dp.register_callback_query_handler(
        books_answer,
        lambda call: call.data == "books"
    )
    dp.register_callback_query_handler(
        movies_answer,
        lambda call: call.data == "movies"
    )