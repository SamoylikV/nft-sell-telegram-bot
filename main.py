# !venv/bin/python
import logging
import codecs

from aiogram.dispatcher.webhook import EditMessageReplyMarkup
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

bot = Bot(token="")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)


class States(StatesGroup):
    lang = State()
    menu = State()
    egg_ru = State()
    egg_eng = State()
    dragon_ru = State()
    dragon_eng = State()
    app_ru = State()
    app_eng = State()
    support_ru = State()
    support_eng = State()


@dp.message_handler(commands=['support_ru'])
async def support_ru(message: types.Message):
    await bot.send_message(message.from_user.id, "test message")


@dp.message_handler(commands=['support_eng'])
async def support_eng(message: types.Message):
    await bot.send_message(message.from_user.id, "test message")


# --------------------------Start------------------------------------------

@dp.message_handler(commands="start")
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text="🇷🇺", callback_data="ru"),
                 types.InlineKeyboardButton(text="🇬🇧", callback_data="eng"))
    await message.answer("Выберете язык / Select language", reply_markup=keyboard)


# --------------------------Language-select--------------------------------
@dp.callback_query_handler(text="ru")
async def change_lang_ru(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🥚 Купить яйцо", callback_data="buy_egg_ru"),
                 # types.InlineKeyboardButton(text="🐲 Купить дракона", callback_data="buy_dragon_ru"),
                 types.InlineKeyboardButton(text="📱 Приложение", callback_data="app_ru"),
                 types.InlineKeyboardButton(text="🤝 Служба поддержки", callback_data="support_ru"))
    async with state.proxy() as data:
        data['lang'] = 'ru'
    await call.answer(text="Язык поменялся", show_alert=True)
    # await call.message.answer("Меню", reply_markup=keyboard)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Добро пожаловать в бота DRAGON EGGS")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="eng")
async def change_lang_eng(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🥚 Buy egg", callback_data="buy_egg_eng"),
                 # types.InlineKeyboardButton(text="🐲 Buy dragon", callback_data="buy_dragon_eng"),
                 types.InlineKeyboardButton(text="📱 App", callback_data="app_eng"),
                 types.InlineKeyboardButton(text="🤝 Support", callback_data="support_eng"))
    async with state.proxy() as data:
        data['lang'] = 'eng'
    await call.answer(text="Language changed", show_alert=True)
    # await call.message.answer("Меню", reply_markup=keyboard)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Wellcome to DRAGON EGGS bot")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


# --------------------------Language-select--------------------------------


# ---------------------------Main-Menu-------------------------------------


@dp.callback_query_handler(text="menu_ru")
async def menu_ru(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🥚 Купить яйцо", callback_data="buy_egg_ru"),
                 # types.InlineKeyboardButton(text="🐲 Купить дракона", callback_data="buy_dragon_ru"),
                 types.InlineKeyboardButton(text="📱 Приложение", callback_data="app_ru"),
                 types.InlineKeyboardButton(text="📱 Тест покупки", callback_data="test_buy_ru"),
                 types.InlineKeyboardButton(text="🤝 Служба поддержки", callback_data="support_ru"))
    async with state.proxy() as data:
        data['lang'] = 'ru'
    # await call.message.answer("Меню", reply_markup=keyboard)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="🗺️ Главное меню 🗺️")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="menu_eng")
async def menu_eng(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🥚 Buy egg", callback_data="buy_egg_eng"),
                 # types.InlineKeyboardButton(text="🐲 Buy dragon", callback_data="buy_dragon_eng"),
                 types.InlineKeyboardButton(text="📱 App", callback_data="app_eng"),
                 types.InlineKeyboardButton(text="🤝 Support", callback_data="support_eng"))
    async with state.proxy() as data:
        data['lang'] = 'eng'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="🗺️ Main menu 🗺️")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


# ---------------------------Main-Menu-------------------------------------


# --------------------------Egg-select-------------------------------------
@dp.callback_query_handler(text="buy_egg_eng")
async def egg_planet_eng(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🔥 Fire", callback_data="fire_egg_eng"),
                 types.InlineKeyboardButton(text="💧 Water", callback_data="water_egg_eng"),
                 types.InlineKeyboardButton(text="🪨 Rock", callback_data="rock_egg_eng"),
                 types.InlineKeyboardButton(text="↩️ Back", callback_data="menu_eng"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='🥚 What egg do you want?')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="buy_egg_ru")
async def egg_planet_ru(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🔥 Огня", callback_data="fire_egg_ru"),
                 types.InlineKeyboardButton(text="💧 Воды", callback_data="water_egg_ru"),
                 types.InlineKeyboardButton(text="🪨 Скал", callback_data="rock_egg_ru"),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="menu_ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='🥚 Какое яйцо ты хочешь?')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


# --------------------------Egg-select-------------------------------------

# --------------------------Dragon-select-----------------------------------
# @dp.callback_query_handler(text="buy_dragon_eng")
# async def dragon_planet_eng(call: types.CallbackQuery):
#     # keyboard = types.InlineKeyboardMarkup()
#     # keyboard.add(types.InlineKeyboardButton(text="Planet one", callback_data="dragon_planet1_eng"),
#     #              types.InlineKeyboardButton(text="Planet two", callback_data="dragon_planet2_eng"),
#     #              types.InlineKeyboardButton(text="Pla FLLnet three", callback_data="dragon_planet3_eng"),
#     #              types.InlineKeyboardButton(text="Planet four", callback_data="dragon_planet4_eng"),
#     #              types.InlineKeyboardButton(text="Planet five", callback_data="dragon_planet5_eng"),
#     #              types.InlineKeyboardButton(text="Planet six", callback_data="dragon_planet6_eng"),
#     #              types.InlineKeyboardButton(text="Back", callback_data="menu_eng"))
#     # await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#     #                             text="🐲 Dragon shop")
#     # await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#     #                                     reply_markup=keyboard)
#     await call.answer(text="Work in progress", show_alert=True)
#
#
# @dp.callback_query_handler(text="buy_dragon_ru")
# async def dragon_planet_ru(call: types.CallbackQuery):
#     # keyboard = types.InlineKeyboardMarkup()
#     # keyboard.add(types.InlineKeyboardButton(text="Первая планета", callback_data="dragon_planet1_ru"),
#     #              types.InlineKeyboardButton(text="Вторая планета", callback_data="dragon_planet2_ru"),
#     #              types.InlineKeyboardButton(text="Третья планета", callback_data="dragon_planet3_ru"),
#     #              types.InlineKeyboardButton(text="Четвёртая планета", callback_data="dragon_planet4_ru"),
#     #              types.InlineKeyboardButton(text="Пятая планета", callback_data="dragon_planet5_ru"),
#     #              types.InlineKeyboardButton(text="Шестая планета", callback_data="dragon_planet6_ru"),
#     #              types.InlineKeyboardButton(text="Назад", callback_data="menu_ru"))
#     # await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#     #                             text="🐲 Покупка дракона")
#     # await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#     #                                     reply_markup=keyboard)
#     await call.answer(text="В разработке", show_alert=True)


# --------------------------Dragon-select-----------------------------------

# --------------------------Egg-buying--------------------------------------

@dp.callback_query_handler(text="fire_egg_ru")
async def fire_egg_ru(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IV4SwXR1C4p6'),
                 types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'🔥 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="water_egg_ru")
async def water_egg_ru(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IVCp4qYHBzNg'),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'💧 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)

    @dp.callback_query_handler(text="rock_egg_ru")
    async def rock_egg_ru(call: types.CallbackQuery):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IVEcKtST54vm'),
                     types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🪨 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="fire_egg_eng")
async def fire_egg_eng(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IV4SwXR1C4p6'),
                 types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_eng"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'🔥 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="water_egg_eng")
async def water_egg_eng(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IVCp4qYHBzNg'),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_eng"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'💧 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)

    @dp.callback_query_handler(text="rock_egg_eng")
    async def rock_egg_eng(call: types.CallbackQuery):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url='http://t.me/CryptoBot?start=IVEcKtST54vm'),
                     types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🪨 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


# --------------------------Egg-buying--------------------------------------

# --------------------------Application-------------------------------------

@dp.callback_query_handler(text="app_ru")
async def dragon_planet_ru(call: types.CallbackQuery):
    await call.answer(text="В разработке", show_alert=True)


@dp.callback_query_handler(text="app_eng")
async def dragon_planet_ru(call: types.CallbackQuery):
    await call.answer(text="Work in progress", show_alert=True)


# --------------------------Application-------------------------------------


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
