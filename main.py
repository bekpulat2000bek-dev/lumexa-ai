

import asyncio
import os
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "✨ Welcome to LUMEXA AI!\n\n"
        "I am your intelligent assistant.\n"
        "Send me a message to get started!"
    )


@dp.message(F.text)
async def chat(message: Message):
    await message.answer(
        "Hello! 👋 I am LUMEXA.\n\n"
        "My AI brain is being connected. Stay tuned! 🚀"
    )


async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    bot = Bot(token=TOKEN)

    try:
        print("LUMEXA is starting...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
            
