from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher
from handlers import handlers



bot = Bot(TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
