# !venv/bin/python
import logging
import json

from cryptopay import CryptoPay
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

json_file = open("token.json", "r")
data = json.load(json_file)
json_file.close()

bot = Bot(token=data["Main"])
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
user_id = data["User_id"]
parameters = {
    "token": data["Cryptobot"],
    # "api_url": "https://pay.crypt.bot/"
    "api_url": "https://testnet-pay.crypt.bot/"
}
json_file = open("eggs.json", "r")
data = json.load(json_file)
json_file.close()


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
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🥚 Купить яйцо", callback_data="buy_egg_ru"),
                 # types.InlineKeyboardButton(text="🐲 Купить дракона", callback_data="buy_dragon_ru"),
                 types.InlineKeyboardButton(text="Приложение", callback_data="app_ru"),
                 types.InlineKeyboardButton(text="🤝 Служба поддержки", url='http://t.me/nft_seller_support_bot'))
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
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🥚 Buy egg", callback_data="buy_egg_eng"),
                 # types.InlineKeyboardButton(text="🐲 Buy dragon", callback_data="buy_dragon_eng"),
                 types.InlineKeyboardButton(text="App", callback_data="app_eng"),
                 types.InlineKeyboardButton(text="🤝 Support", url='http://t.me/nft_seller_support_bot'))
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
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🥚 Купить яйцо", callback_data="buy_egg_ru"),
                 # types.InlineKeyboardButton(text="🐲 Купить дракона", callback_data="buy_dragon_ru"),
                 types.InlineKeyboardButton(text="Приложение", callback_data="app_ru"),
                 types.InlineKeyboardButton(text="🤝 Служба поддержки", url='http://t.me/nft_seller_support_bot'))
    async with state.proxy() as data:
        data['lang'] = 'ru'
    # await call.message.answer("Меню", reply_markup=keyboard)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="🗺️ Главное меню 🗺️")
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="menu_eng")
async def menu_eng(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="🥚 Buy egg", callback_data="buy_egg_eng"),
                 # types.InlineKeyboardButton(text="🐲 Buy dragon", callback_data="buy_dragon_eng"),
                 types.InlineKeyboardButton(text="App", callback_data="app_eng"),
                 types.InlineKeyboardButton(text="🤝 Support", url='http://t.me/nft_seller_support_bot'))
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
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=f"🔥 Fire {data['Amount']['Fire']}/30", callback_data="fire_egg_eng"),
                 types.InlineKeyboardButton(text=f"💧 Water {data['Amount']['Water']}/40",
                                            callback_data="water_egg_eng"),
                 types.InlineKeyboardButton(text=f"🪨 Rock {data['Amount']['Rock']}/50", callback_data="rock_egg_eng"),
                 types.InlineKeyboardButton(text="↩️ Back", callback_data="menu_eng"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='🥚 What egg do you want?')
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=keyboard)


@dp.callback_query_handler(text="buy_egg_ru")
async def egg_planet_ru(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text=f"🔥 Огня {data['Amount']['Fire']}/30", callback_data="fire_egg_ru"),
                 types.InlineKeyboardButton(text=f"💧 Воды {data['Amount']['Water']}/40", callback_data="water_egg_ru"),
                 types.InlineKeyboardButton(text=f"🪨 Скал {data['Amount']['Rock']}/50", callback_data="rock_egg_ru"),
                 types.InlineKeyboardButton(text="↩️ Назад", callback_data="menu_ru"))
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"🥚 Какое яйцо ты хочешь?")
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
    # unique_string = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for _ in range(10))
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Fire'] != 0:
        fire_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            fire_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Fire', 'USDT',
                                            'Подтверди покупку!')['result']['invoice_id']
        pay_url = fire_egg_invoice.get_invoice(invoice_id)[0]['pay_url']
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
            types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🔥 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Эти яйца закончились :(')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="water_egg_ru")
async def water_egg_ru(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Water'] != 0:
        water_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            water_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Water', 'USDT',
                                             'Подтверди покупку!')['result']['invoice_id']
        pay_url = water_egg_invoice.get_invoice(invoice_id)[0]['pay_url']
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
            types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'💧 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Эти яйца закончились :(')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="rock_egg_ru")
async def rock_egg_ru(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Rock'] != 0:
        rock_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            rock_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Rock', 'USDT',
                                            'Подтверди покупку!')['result']['invoice_id']
        pay_url = rock_egg_invoice.get_invoice(invoice_id)[0]['pay_url']

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
            types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🪨 {call.from_user.first_name}, как оплачивать будешь?\n(При оплате через TONLINK указывай какое яйцо тебе нужно)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_ru"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Эти яйца закончились :(')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="fire_egg_eng")
async def fire_egg_eng(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Fire'] != 0:
        fire_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            fire_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Fire', 'USDT',
                                            'Confirm your payment!')['result']['invoice_id']
        pay_url = fire_egg_invoice.get_invoice(invoice_id)[0]['pay_url']
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
                     types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
                     types.InlineKeyboardButton(text="↩️ Назад", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🔥 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'These eggs are out of stock :(')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="water_egg_eng")
async def water_egg_eng(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Water'] != 0:
        water_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            water_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Water', 'USDT',
                                             'Confirm your payment!')['result']['invoice_id']
        pay_url = water_egg_invoice.get_invoice(invoice_id)[0]['pay_url']
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
                     types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
                     types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'💧 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'These eggs are out of stock :(')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)


@dp.callback_query_handler(text="rock_egg_eng")
async def rock_egg_eng(call: types.CallbackQuery):
    json_file = open("eggs.json", "r")
    data = json.load(json_file)
    json_file.close()
    if data['Amount']['Water'] != 0:
        rock_egg_invoice = CryptoPay(user_id, parameters)
        invoice_id = \
            rock_egg_invoice.create_invoice(1, 'openBot', 'https://t.me/confirm_payment_nft_bot?start=Rock', 'USDT',
                                            'Confirm your payment!')['result']['invoice_id']
        pay_url = rock_egg_invoice.get_invoice(invoice_id)[0]['pay_url']
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(types.InlineKeyboardButton(text='CRYPTOBOT', url=pay_url),
                     types.InlineKeyboardButton(text='TONLINK', url='https://tonlink.app/dragoneggs'),
                     types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'🪨 {call.from_user.first_name}, how will you pay?\n(When paying via TONLINK specify which egg you need)')
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(text="↩️ Back", callback_data="buy_egg_eng"))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'These eggs are out of stock :(')
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
