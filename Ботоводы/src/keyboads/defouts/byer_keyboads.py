from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text='/start'),
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton (text='/help')
            
        ],
        [
            KeyboardButton (text='Поделиться контактом',
            request_contact=True),
            KeyboardButton (text='Поделиться геолокацией',
            request_location =True)
            
        ],
        [
            KeyboardButton (text='Скрыть клавиатуру')
            
        ]
    ], 
    resize_keyboard=True
)

see_commands_default_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text='Показать')
           
        ]
        ], 
    resize_keyboard=True)

info_commands_default_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton (text='Контакты продавца'),
            KeyboardButton (text='Пункты самовывоза'), 
            KeyboardButton (text='Время работы')
           
           
        ]
        ], 
    resize_keyboard=True)