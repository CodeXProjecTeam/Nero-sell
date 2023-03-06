import sqlite3

from aiogram import types, executor
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.start_button import start_button


# <--------------DB START-------------->
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Добро пожаловать! {name}",start_button)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу.\nВ базе {count} участников."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} уже добавлен в базу.")
        await message.answer(f"Добро пожаловать! {name}", reply_markup=start_button)


#<----------Обработка ссылки---------------->#
@dp.message_handler(text='Profil')
async def profil(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, f'ID: {message.from_id}\nhttps://t.me/nero_konkurs_bot?start={message.from_user.id}\nReferal: 0')
    
#<----------Profil---------------->#
# @dp.message_handler(text='Profil')
# async def bosh_sahifa(message: types.Message):
#     await message.answer(message.from_user.id, f'ID: {message.from_id}\nhttps://t.me/nero_konkurs_bot?start={message.from_user.id}\nReferal: 0')
    
#<----------Условие--------------->#
@dp.message_handler(text='Shartlar 🎊')
async def bosh_sahifa(message: types.Message):
    await message.answer('пойти отсюда нахуй')

#<----------Ссылка---------------->#    
@dp.message_handler(text='Mening linkim 🔗')
async def my_link(message: types.Message):
    await message.answer('null (xyle)')

#<----------Очко---------------->#    
@dp.message_handler(text='Mening balim 🎈')
async def mine_points(message: types.Message):
    await message.answer('null(тоже xyle)')
    
#<----------TOP Members---------------->#
@dp.message_handler(text='TOP 10 ishtirokchilar 🎩')
async def top_members(message: types.Message):
    await message.answer('Men va men')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)