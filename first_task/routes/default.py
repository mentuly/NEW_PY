from .. import dp
from ..forms import temperature
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReactionTypeEmoji
from ..models import short_typing_action, user_temperature

@dp.message(Command('start'))
async def command_start(message: Message):
    chat_id = message.chat.id
    await short_typing_action(chat_id)
    await message.react([ReactionTypeEmoji(emoji = "👍")])
    await message.answer("Вітаю на моєиу телеграм боті, щоб розпочати нажміть на /temperature")

@dp.message(Command('temperature'))
async def ask_for_temperature(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await short_typing_action(chat_id)
    await message.react([ReactionTypeEmoji(emoji = "👍")])
    await message.answer("Введіть температуру в градусах Цельсія:")
    await state.set_state(temperature.temperature)

# обробка температури яку ввів користувач де текст з 78 строки на пряму каже що далі висупає state класу temperature і показує у 81 строці продовження
@dp.message(temperature.temperature)
async def process_temperature_input(message: Message, state: FSMContext):
    chat_id = message.chat.id
    try:
        temperature = float(message.text)  # перетворення тексту у число
        response = user_temperature(temperature)
        await short_typing_action(chat_id)
        await message.react([ReactionTypeEmoji(emoji = "❤")])
        await message.answer(response)
        await state.clear()
    except ValueError:
        await short_typing_action(chat_id)
        await message.answer("Будь ласка, введіть числове значення температури.")