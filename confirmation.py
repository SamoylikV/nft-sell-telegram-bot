# !venv/bin/python
import logging
import json

from aiogram.contrib.middlewares.logging import LoggingMiddleware

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


json_file = open("token.json", "r")
data = json.load(json_file)
json_file.close()

bot = Bot(token=data["Confirmation"])
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
json_file = open("eggs.json", "r")
data = json.load(json_file)
json_file.close()


def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(commands="start")
async def start(message: types.Message):
    global data
    egg_type = extract_unique_code(message.text)
    if egg_type == 'Fire':
        data['Amount']['Fire'] = data['Amount']['Fire'] - 1
    elif egg_type == 'Water':
        data['Amount']['Water'] = data['Amount']['Water'] - 1
    elif egg_type == 'Rock':
        data['Amount']['Rock'] = data['Amount']['Rock'] - 1

    await message.answer(f"Спасибо за покупку! / Thanks for your purchase!")
    json_file = open("eggs.json", "w")
    json.dump(data, json_file)
    json_file.close()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
