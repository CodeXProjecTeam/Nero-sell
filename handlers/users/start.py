import sqlite3

from aiogram import types, executor
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS,CHANNELS
from filters import IsPrivate
from loader import dp, db, bot
from keyboards.default.start_button import start_button
from keyboards.inline.sub_button import check_button


# <--------------DB START-------------->
@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        # await message.answer(f"Xush kelibsiz! {name}",start_button)
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

        await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n\n"
                            f"{channels_format}",
                            reply_markup=check_button,
                            disable_web_page_preview=True)
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} добавлен в базу.\nВ базе {count} участников."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} уже добавлен в базу.")
        # await message.answer(f"Xush kelibsiz! {name}", reply_markup=start_button)
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

        await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n\n"
                            f"{channels_format}",
                            reply_markup=check_button,
                            disable_web_page_preview=True)


#<----------Check Sub--------------->#

        
#<----------Условие--------------->#
@dp.message_handler(IsPrivate(),text='Shartlar 🎊')
async def bosh_sahifa(message: types.Message):
    await message.answer('пойти отсюда нахуй')

#<----------Ссылка---------------->#    
@dp.message_handler(IsPrivate(),text='Mening linkim 🔗')
async def my_link(message: types.Message):
    await message.answer('null (xyle)')

#<----------Очко---------------->#    
@dp.message_handler(IsPrivate(),text='Mening balim 🎈')
async def mine_points(message: types.Message):
    await message.answer('null(тоже xyle)')
    
#<----------TOP Members---------------->#
@dp.message_handler(IsPrivate(),text='TOP 10 ishtirokchilar 🎩')
async def top_members(message: types.Message):
    await message.answer('Men va men')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)