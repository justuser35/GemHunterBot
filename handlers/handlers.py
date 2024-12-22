from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def command_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мой профиль"), KeyboardButton(text="Список лидеров"), KeyboardButton(text="Достижения")],
            [KeyboardButton(text="Перейти в шахту")], # в шахте будут ежедневки и др.
        ],
        resize_keyboard=True
    )
    await message.answer("тут будет профиль игрока", reply_markup=keyboard)


@router.message(Command("help"))
async def command_help(message: Message):
    text = '''<a href="https://t.me/GemHunterBot_help">Официальное FAQ</a>
 ➖➖➖➖➖➖
Другие вопросы и предложения по улучшению пишите в нашу группу @GemHunterBot_chat'''
    await message.answer(text, parse_mode="HTML")


@router.message(Command("id"))
async def get_id(message: Message):
    user_id = message.from_user.id
    await message.answer(f"Ваш ID: {user_id}")


@router.message()
async def handle_reply_button(message: Message):
    if message.text == "Достижения":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⏪Назад"), KeyboardButton(text="Моих достижений: 10")],
                [KeyboardButton(text="Список достижений и награды")]
            ],
            resize_keyboard=True
        )
        await message.answer("", reply_markup=keyboard)

    elif message.text == "Список лидеров":
        await message.answer("Список лидеров")

    elif message.text == "Перейти в шахту":
        await message.answer("Переход в шахту")

    elif message.text == "⏪Назад":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мой профиль"), KeyboardButton(text="Список лидеров"),
                 KeyboardButton(text="Достижения")],
                [KeyboardButton(text="Перейти в шахту")],
            ],
            resize_keyboard=True
        )
        await message.answer("тут будет профиль игрока", reply_markup=keyboard)

    else:
        await message.answer(f"тут будет профиль игрока")
