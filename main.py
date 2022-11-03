from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import executor
from config import dp, bot
from ReplyKeyboard import menuStart, menuHH, menuCityFen
import logging


@dp.message_handler(Command('start'))
async def start(msg: Message):
    img = open("images/logo.jpg", "rb")
    text = f"Assalomu alaykum {msg.from_user.full_name}, \nNwelion botiga xush kelibsiz"
    await bot.send_photo(msg.chat.id, img, caption=text, reply_markup=menuStart)


@dp.message_handler(commands='help')
async def help(msg: Message):
    img = open("images/help1.jpg", "rb")
    text = f"Yordam uchun https://t.me/mkjv08 bilan gaplashing"
    await bot.send_photo(msg.chat.id, img, caption=text)


@dp.message_handler(text="HAR HIL")
async def programming(msg: Message):
    await msg.answer(f"Kitobni tanlang!", reply_markup=menuHH)


@dp.message_handler(text="Python asoslari (O'zbekcha)")
async def python_asos(msg: Message):
    await msg.answer_document(open("books/Python asoslari (O'zbekcha).pdf", "rb"), reply_markup=menuHH)


@dp.message_handler(text="ALTERNSTORY")
async def python_asos(msg: Message):
    await msg.answer_document(open("books/ALTERNSTORY.pdf", "rb"), reply_markup=menuHH)


@dp.message_handler(text="FANTASY")
async def python_asos(msg: Message):
    await msg.answer_document(open("books/FANTASY.pdf", "rb"), reply_markup=menuHH)


@dp.message_handler(text="Orqaga")
async def cancel(msg: Message):
    img = open("images/logo.jpg", "rb")
    text = f"Assalomu alaykum {msg.from_user.full_name}, \nNwelion botiga xush kelibsiz"
    await bot.send_photo(msg.chat.id, img, caption=text, reply_markup=menuStart)


@dp.message_handler(commands="cf")
async def start(msg: Message):
    await msg.answer(f"Kitobni tanlang!", reply_markup=menuCityFen)


@dp.message_handler(text="CF1")
async def python_asos(msg: Message):
    await msg.answer_document(open("books2/CF1.pdf", "rb"), reply_markup=menuCityFen)


@dp.message_handler(text="CF2")
async def python_asos(msg: Message):
    await msg.answer_document(open("books2/CF2.pdf", "rb"), reply_markup=menuCityFen)


@dp.message_handler(text="CF3")
async def python_asos(msg: Message):
    await msg.answer_document(open("books2/CF3.pdf", "rb"), reply_markup=menuCityFen)


@dp.message_handler(text="Orqaga")
async def cancel(msg: Message):
    img = open("images/logo.jpg", "rb")
    text = f"Assalomu alaykum {msg.from_user.full_name}, \nNwelion botiga xush kelibsiz"
    await bot.send_photo(msg.chat.id, img, caption=text, reply_markup=menuCityFen)

if __name__ == '__main__':
    executor.start_polling(dp)
