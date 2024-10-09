import asyncio
from .. import bot
from ..forms import ChatAction

async def short_typing_action(chat_id, duration=3):
    await bot.send_chat_action(chat_id, ChatAction.TYPING)
    await asyncio.sleep(duration)