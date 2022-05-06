# !venv/bin/python
import logging
import json
import random

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

json_file = open("token.json", "r")
data = json.load(json_file)
json_file.close()
bot = Bot(token=data["Main"])
admin = data["admin"]
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)


# --------------------------Start------------------------------------------

@dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text="👋", callback_data="ru"))
    await message.answer("👋", reply_markup=keyboard)


# --------------------------Language-select--------------------------------
@dp.callback_query_handler(text="ru")
async def quant(call: types.CallbackQuery, state: FSMContext):
    if str(call.message.chat.id) == admin:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(types.InlineKeyboardButton(text="⚛️ Добавить квант", callback_data="add_quant"),
                     types.InlineKeyboardButton(text="⚛️ Удалить квант", callback_data="del_quant"),
                     types.InlineKeyboardButton(text="🎫 Добавить ивент", callback_data="add_event"),
                     types.InlineKeyboardButton(text="🎫 Удалить ивент", callback_data="del_event"))

        await call.answer(text="Привет! 👋", show_alert=True)
        # await call.message.answer("Меню", reply_markup=keyboard)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Добро пожаловать в адмен бота")
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(one_time_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text="👋", callback_data="ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Ты не одмен")
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="add_event")
async def event(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обратно", callback_data="ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Напишите название ивента, направление, преподавателя, время начала, время конца")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="add_quant")
async def event(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обратно", callback_data="ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Напишите название кванта и описание")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="del_event")
async def event(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обратно", callback_data="ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Напишите название ивента, направление, преподавателя, время начала, время конца")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="del_quant")
async def event(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Обратно", callback_data="ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Напишите название кванта и описание")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.message_handler()
async def add_stuff(message: types.Message):
    if message.text != '/start':
        keyboard = types.InlineKeyboardMarkup(one_time_keyboard=True)
        keyboard.add(types.InlineKeyboardButton(text="👋", callback_data="ru"))
        await bot.send_message(message.from_user.id, 'Готово', reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
