from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from Bot import bot
import asyncio

router = Router()

def create_keyboard(state="Study") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    if state == "Study":
        builder.button(text="Исследование", callback_data="Study")

    return builder.as_markup()


@router.message(Command("start"))
async def command_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎒Снаряжение"), KeyboardButton(text="🛒Магазин"), KeyboardButton(text="🏆Достижения")],
            [KeyboardButton(text="📊Список лидеров"), KeyboardButton(text="🧾Квесты")],
            [KeyboardButton(text="🏠Мой профиль"), KeyboardButton(text="🌐Друзья")],
            [KeyboardButton(text="⛏️Перейти в шахту")]
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
    if message.text == "🏆Достижения":
        achiv = 1
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Список всех достижений и награды"), KeyboardButton(text="Мои достижения")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Моих достижений: "+ str(achiv), reply_markup=keyboard)

    elif message.text == "📊Список лидеров":
        await message.answer("📊Список лидеров \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n"
                             "6. \n"
                             "7. \n"
                             "8. \n"
                             "9. \n"
                             "10. \n")


    elif message.text == "⛏️Перейти в шахту":
        miners = 0

        keyboard = ReplyKeyboardMarkup(

            keyboard=[

                [KeyboardButton(text="Выбрать шахту"), KeyboardButton(text="Совместная шахта")],
                [KeyboardButton(text="Система поиска шахт")],
                [KeyboardButton(text="⏪Назад")]

            ],

            resize_keyboard=True

        )
        await message.answer("Выберите режим \n", reply_markup=keyboard)

        await message.answer("⛏️Шахта \n"
                             "👨🏿Работников в шахте: "+ str(miners))


    elif message.text == "⏪Назад":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🎒Снаряжение"), KeyboardButton(text="🛒Магазин"),
                 KeyboardButton(text="🏆Достижения")],
                [KeyboardButton(text="📊Список лидеров"), KeyboardButton(text="🧾Квесты")],
                [KeyboardButton(text="🏠Мой профиль"), KeyboardButton(text="🌐Друзья")],
                [KeyboardButton(text="⛏️Перейти в шахту")]
            ],
            resize_keyboard=True
        )
        await message.answer("тут будет профиль игрока", reply_markup=keyboard)

    elif message.text == "🛒Магазин":
        bal = 10

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📈Прокачка"), KeyboardButton(text="💳Донат")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Текущий баланс: "+ str(bal), reply_markup=keyboard)

    elif message.text == "🎒Снаряжение":
        await message.answer("🎒Снаряжение")

    elif message.text == "🏠Мой профиль":
        await message.answer("🏠Мой профиль")

    elif message.text == "🌐Друзья":
        await message.answer("🌐Друзья")

        
    elif message.text == "🧾Квесты":

        sent_message = await message.answer("Получение сведений о квестах...")
        await asyncio.sleep(2)
        CompletedDailyQuest = 4
        CompletedWeeklyQuest = 0

        DailyIndicator = ""
        WeeklyIndicator = ""

        if CompletedDailyQuest == 4:
            DailyIndicator = "🟩 Ежедневные"
        else:
            DailyIndicator = "🟥 Ежедневные"

        if CompletedWeeklyQuest == 4:
            WeeklyIndicator += "🟩 Еженедельные"
        else:
            WeeklyIndicator = "🟥 Еженедельные"

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=DailyIndicator), KeyboardButton(text=WeeklyIndicator)],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await bot.delete_message(chat_id=sent_message.chat.id,
                                    message_id=sent_message.message_id)
        await message.answer(text = DailyIndicator + " | " + WeeklyIndicator, reply_markup = keyboard)

    elif message.text == "🟩 Ежедневные" or message.text == "🟥 Ежедневные":
        await message.answer("Ежедневные \n"
                             "1. Пенис \n"
                             "2. Викторович \n"
                             "3. Пенисов \n"
                             "4. Да \n")

    elif message.text == "🟩 Еженедельные" or message.text == "🟥 Еженедельные":
        await message.answer("Еженедельные \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n")

    elif message.text == "💳Донат":
        DonateBalance = 10

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⛏️Донат-орудие"), KeyboardButton(text="📦Донат-иное")],
                [KeyboardButton(text="💸Пополнить счёт")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Ваш донат-баланс: "+ str(DonateBalance)+ "$", reply_markup=keyboard)

    elif message.text == "📈Прокачка":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⛏️Орудие"), KeyboardButton(text="✖️Множители"), KeyboardButton(text="📦Иное")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Выберите тип прокачки", reply_markup=keyboard)

    elif message.text == "⛏️Орудие":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⛏️Кирка"), KeyboardButton(text="⛏️️Бур")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Какой тип предмета?", reply_markup=keyboard)

    elif message.text == "✖️Множители":
        await message.answer("✖️Множители \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "📦Иное":
        await message.answer("📦Иное \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "⛏️Кирка":
        await message.answer("⛏️Кирка \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "⛏️️Бур":
        await message.answer("⛏️️Бур \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")


    elif message.text == "⛏️Донат-орудие":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="⛏️Супер-кирка"), KeyboardButton(text="⛏️️Супер-бур")],
                [KeyboardButton(text="⏪Назад")]
            ],
            resize_keyboard=True
        )
        await message.answer("Какой тип донат-предмета?", reply_markup=keyboard)

    elif message.text == "📦Донат-иное":
        await message.answer("📦Донат-Иное \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "⛏️Супер-кирка":
        await message.answer("⛏️Супер-Кирка \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "⛏️️Супер-бур":
        await message.answer("⛏️Супер-️Бур \n"
                             "1. \n"
                             "2. \n"
                             "3. \n"
                             "4. \n"
                             "5. \n")

    elif message.text == "💸Пополнить счёт":
        await message.answer("Текущий курс: 2 Donate = 1₽ \n"
                             "Напишите сумму (₽): ")

    elif message.text == "Мои достижения":
        await message.answer("Ваши достижения: \n"
                             "1. Первый бизнес \n"
                             "\n"
                             "-- 0/1 --")

    elif message.text == "Список всех достижений и награды":
        await message.answer("1. Первый бизнес \n"
                             "2. Успешный успех \n"
                             "\n"
                             "-- В этапе разработки -- \n")

    elif message.text == "Выбрать шахту":
        await message.answer("Выбор шахты. \n"
                             "1. Каменное русло \n")

    elif message.text == "Совместная шахта":
        await message.answer("Выбор друга \n"
                             "1. ... \n"
                             "\n"
                             "0/1\n")

    elif message.text == "Система поиска шахт":
        await message.answer("Поиск шахты.\n")
        keyboard = create_keyboard(state="Study")
        await message.answer("Шахта №1 \n", reply_markup=keyboard)
        keyboard = create_keyboard(state="Study")
        await message.answer("Шахта №2 \n", reply_markup=keyboard)
        keyboard = create_keyboard(state="Study")
        await message.answer("Шахта №3 \n", reply_markup=keyboard)

        @router.callback_query()
        async def handle_callback(callback_query: CallbackQuery):
            if callback_query.data == "Study":
                await callback_query.message.answer("Исследовано!")
                await callback_query.answer()

    else:
        await message.answer(f"тут будет профиль игрока")

