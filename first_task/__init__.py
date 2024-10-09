import logging
from os import getenv
from aiogram import Bot, Dispatcher

token = getenv("TOKEN")
bot = Bot(token)

dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

async def main() -> None:
    await dp.start_polling(bot)

from . import routes