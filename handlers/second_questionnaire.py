from aiogram import types, Dispatcher
from config import bot
from keyboards import second_questionnaire_inline_buttons

async def second_questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Soda or Still water?",
        reply_markup=await second_questionnaire_inline_buttons.second_questionnaire_keyboard()
    )
async def soda_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Soda is harmful, it's better to drink still water!",
    )

async def still_water_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh cool, I like still water too!",
    )


def register_second_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        second_questionnaire_start,
        lambda call: call.data == "start_second_questionnaire"
    )
    dp.register_callback_query_handler(
        soda_answer,
        lambda call: call.data == "soda"
    )
    dp.register_callback_query_handler(
        still_water_answer,
        lambda call: call.data == "still_water"
    )