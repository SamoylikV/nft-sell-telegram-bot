import logging
import json
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

json_file = open("token.json", "r")
data = json.load(json_file)
json_file.close()

bot = Bot(token=data["Support"])
admin_id = data["Admin_id"]
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Чем я могу помочь? / How can i help?")


@dp.message_handler()
async def echo_message(message: types.Message):
    text = f'Пользователь: https://t.me/{message.from_user.username} \nТекст сообщения: {message.text}'
    await bot.send_message(message.from_user.id, 'Ваш вопрос был отправлен! / Your request has been sent!')
    await bot.send_message(admin_id, text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
