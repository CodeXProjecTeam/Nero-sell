from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text ='Shartlar 🎊'),KeyboardButton(text="Mening linkim 🔗"),KeyboardButton(text="Mening balim 🎈"), KeyboardButton(text='TOP 10 ishtirokchilar 🎩'), KeyboardButton(text='Profil')],
    ],
    resize_keyboard=True
)