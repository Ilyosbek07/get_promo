import asyncio
import time

import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user(telegram_id=message.from_user.id,
                          full_name=message.from_user.full_name,
                          username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(telegram_id=message.from_user.id)
    button = types.KeyboardButton("Promo Code olish 🎦")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)

    await message.answer("Xush kelibsiz\n\n"
                         "But bot orqali siz Promo Code olishingiz mumkin\n"
                         "Pastdagi tugmani boring 👇",
                         reply_markup=keyboard)


@dp.message_handler(text="Promo Code olish 🎦")
async def promo_code(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    minute = f"{time.localtime().tm_min:02d}"
    clock = f"{time.localtime().tm_hour}"
    promo_code = await db.get_promo_code()
    if promo_code:
        if user['date'] is None:
            current_time = time.localtime()
            current_minute = current_time.tm_min
            date = time.strftime("%d", current_time)
            current_clock = f"{current_time.tm_hour}"
            current_minute = f"{current_minute:02d}"
            await message.answer(f"<b>Sizning Promo Code'ingiz: <code>"
                                 f"{promo_code[0]['promo']}</code></b>")
            await db.update_promo_expire(telegram_id=message.from_user.id,
                                         promo_code=promo_code[0]['promo'])
            await db.update_user_time(
                date=date,
                clock=current_clock,
                minute=current_minute,
                telegram_id=message.from_user.id)
        elif user['date'] < time.strftime("%d", time.localtime()):
            promo_code = await db.get_promo_code()
            current_time = time.localtime()
            current_minute = current_time.tm_min
            date = time.strftime("%d", current_time)
            current_clock = f"{current_time.tm_hour}"
            current_minute = f"{current_minute:02d}"
            await message.answer(f"<b>Sizning Promo Code'ingiz: <code>"
                                 f"{promo_code[0]['promo']}</code></b>")
            await db.update_promo_expire(telegram_id=message.from_user.id,
                                         promo_code=promo_code[0]['promo'])
            await db.update_user_time(
                date=date,
                clock=current_clock,
                minute=current_minute,
                telegram_id=message.from_user.id)
        elif user['date'] == time.strftime("%d", time.localtime()) and (int(clock)) > (int(user['clock'])) and (
                int(minute)) > (int(user['minute'])):
            promo_code = await db.get_promo_code()
            current_time = time.localtime()
            current_minute = current_time.tm_min
            date = time.strftime("%d", current_time)
            current_clock = f"{current_time.tm_hour}"
            current_minute = f"{current_minute:02d}"
            await message.answer(f"<b>Sizning Promo Code'ingiz: <code>"
                                 f"{promo_code[0]['promo']}</code></b>")
            await db.update_promo_expire(telegram_id=message.from_user.id,
                                         promo_code=promo_code[0]['promo'])
            await db.update_user_time(
                date=date,
                clock=current_clock,
                minute=current_minute,
                telegram_id=message.from_user.id)
        else:
            await message.answer('Yangi Promo Code olish uchun Umumiy 1 Soat kutishingiz kerak ')
    else:
        await message.answer('<b>Promo Code tugadi!</b>')


@dp.message_handler(text="add_promo")
async def get_promo_code(message: types.Message):
    await message.answer(f"Boshlandi")
    data = '''NcXJqS04 ayAfPbgw j7tc8OEF 0Amf7ql5 flJ3i7PX Vo9JQDlC 2X9zjpHt Z4LlIlz2 otTyYeJO c5YXCL35 Nac8he3R zG8ibnnB GQexKCmg aG7GgH6B fSpyot4S dYq3GPMI 4OqrslmX G8HDYxjn eY7SqLhf qkXQQQ75 BvFGtYo5 JnKYXkPC RdOfS2hV FKJThurY kfbLS9wn oHj3sGN0 zjTx0dvp UXFkedp4 0OcqVAv6 7EFPFpBN lrlMcXCh xg0kvldZ mhn5eqP5 guVRmUXP pk9jp1WN k541KFe3 8k4AGHfT j68gJI6X 6j276cD0 ZUyItm7N fRA0RB5K 3fukXAg3 6WJQ4yYp pte5vIs2 5sM3g7kA NPOh5QHW ExgGi1YN iyJxaKi6 MEPHxwQN NVT1vh1D AmvjdD2E vZtOpNXE 3166DltZ ZoRdmgO3 9MvIMM6v A8PvgRX0 ptHmNw0b tJ4XKiy5 w49Z3MLG gQnhUMwS nZHH8yc1 R4gXnKV6 V0hCXDAW TLE5D9IH Ya9SWS2J um6GFBqM wHjEqqna 7YMGiNFl EsFV1gur sSxHhIZQ IwoRTngg pFLEBws2 HBHRIrLJ ZzUMOUS2 8wVqVn9P 7JRwMbbr 9UXIfW3y uqgY6EVm 2ONrCJyR lH8gTgLJ 6Jp8fXXn VeCdTe5b aeDtT5qa NJVjaE2h ktWChmdj 9tb1lznZ gWg1yIdJ h6irosJd 4ExlGrkC bw49I5ro lDHhVHMN XujQmxSA cxz2d34e JEa2V3vj daWXy3Q5 J4q4HIR3 IgwNHFqq 8X5kreQM 7R3x1KIC ZTqtc6Zi vYSqNMLU iF2Ns6aH MRjmTmwd FxeHUjpA 2lLNp7Yf KYHz988U Afrn0y2X iBS2FvRh MCih8NV3 LYH3bIwn cuVweTlk dquugT3p 9DciOpOJ mG0lAHkn Ofev6l3t ED8Oskqk SLL3aHdC fuDMDnct Oz5pIzy7 0DpIQtAO r77TpZeR lCf4Fhqt 3e9rkIR6 IBIec23V QopdFaA4 lNTx083O QdDek7nT iORu8pRD teYPlzsM NnpqB7VM DuT3zx1C WZAZgvhC iGtagZ0W 4oXJl0n2 fZRqQR9I 1x7D51CC 94c1jdnv QeHopQ7h GhHWkvSL uDpK7DFq WbLwpRB8 3TUuHZ3E b9oxxMNK imNf6R7F ZHPHGsFk uLl6JL8U viTUnDm8 KoDBKG91 Awx2BjJP h1elagUR'''

    data_list = data.split()

    counter = 0
    for i in data_list:
        await asyncio.sleep(0.1)
        counter += 1
        await db.add_promo(promo=i)
