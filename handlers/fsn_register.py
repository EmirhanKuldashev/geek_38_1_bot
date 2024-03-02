import sqlite3
from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons, register_kb
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    job = State()
    hobby = State()
    gen = State()
    photo = State()


async def start_register(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Write your nickname")
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["nickname"] = message.text
    await message.answer("Write a short biography")
    await RegistrationStates.next()


async def load_biography(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["biography"] = message.text
    await message.answer("Write your age using only numbers")
    await RegistrationStates.next()


async def load_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        age_value = int(age)
        if age_value < 12:
            await message.answer("age restrictions")
        else:
            async with state.proxy() as data:
                data["age"] = message.text
            await message.answer("What is your job?")
            await RegistrationStates.next()
    else:
        await message.answer("Write only numbers")


async def load_job(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["job"] = message.text
    await message.answer("What is your hobby?")
    await RegistrationStates.next()


async def load_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["hobby"] = message.text
    await message.answer("What gender are you?", reply_markup=await register_kb.gen_kb())
    await RegistrationStates.next()


async def load_gen(message: types.Message, state: FSMContext):
    gen = message.text
    if gen not in ["male", "female", "secret"]:
        await message.answer("Select from the list")
    else:
        async with state.proxy() as data:
            data["gen"] = message.text
        await message.answer("Send a photo")
        await RegistrationStates.next()


async def load_photo(message: types.Message, state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(destination_dir=MEDIA_DESTINATION)
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data["nickname"],
            biography=data["biography"],
            age=data["age"],
            hobby=data["hobby"],
            job=data["job"],
            gen=data["gen"],
            photo=path.name
        )

    with open(path.name, "rb") as photo_file:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo_file,
            caption=const.PROFILE_TEXT.format(
                nickname=data['nickname'],
                bio=data['biography'],
                age=data['age'],
                job=data['job'],
                hobby=data['hobby'],
                gender=data['gen']
            )
        )

    await bot.send_message(
        chat_id=message.from_user.id,
        text="You have successfully registered\nCongrats!"
    )

    await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_register,
        lambda call: call.data == "register"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_job,
        state=RegistrationStates.job,
        content_types=['text']
    )
    dp.register_message_handler(
        load_hobby,
        state=RegistrationStates.hobby,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gen,
        state=RegistrationStates.gen,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=[types.ContentType.PHOTO]
    )
