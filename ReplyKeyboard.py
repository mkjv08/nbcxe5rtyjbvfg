from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="HAR HIL"),


        ]
    ],
    resize_keyboard=True
)
menuHH = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python asoslari (O'zbekcha)")
        ],
        [
            KeyboardButton(text="ALTERNSTORY")
        ],
        [
            KeyboardButton(text="FANTASY")
        ],
        [
          KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)
menuCityFen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CF1")
        ],
        [
            KeyboardButton(text="CF2")
        ],
        [
            KeyboardButton(text="CF3")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

