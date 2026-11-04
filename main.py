
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "✨ Welcome to LUMEXA AI!\n\n"
        "Your intelligent assistant is ready.\n"
        "Send me a message to get started."
    )


@dp.message(F.text)
async def chat(message: Message):
    await message.answer(
        "Hello! I'm LUMEXA AI. 🤖\n\n"
        "AI connection is coming soon!"
    )


async def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
  
