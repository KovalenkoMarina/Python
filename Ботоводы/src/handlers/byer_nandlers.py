from cgitb import text
from email import message
from select import select
from loader import db, bot
from loader import dp
from aiogram import types
from keyboads import commands_default_keyboard, see_commands_default_keyboard, info_commands_default_keyboard, get_item_inline_keyboard, navigation_items_callback
from aiogram.types import ReplyKeyboardRemove, InputFile, InputMediaPhoto





@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text= f'Привет, {message.from_user.first_name}! '
                         f'\nРад тебя видеть!',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=['Показать'])
@dp.message_handler(commands='help')
async def answer_help_command(message: types.Message):
    await message.answer(text= 'Список команд представлен на клавиатуре',
                          reply_markup=commands_default_keyboard)

@dp.message_handler(text=['Список товаров'])
@dp.message_handler(commands=['item'])
async def answer_menu_command(message: types.Message):
    first_item_info = db.select_item_info(id=1)
    first_item_info = first_item_info[0]
    _. name. count. photo_path = first_item_info
    item_text = f'Название товара: {name}'\
                f'\nКоличество товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                                caption = item_text,
                                reply_markup=get_item_inline_keyboard())
        
@dp.callback_query_handler(navigation_items_callback.filter(for_data = 'items'))   
async def see_new_item(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _. name. count. photo_path = first_item_info
    item_text = f'Название товара: {name}'\
                f'\nКоличество товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                        caption=item_text),
                                chat_id = call.message.chat_id,
                                message_id = call.message.message_id,
                                reply_markup=get_item_inline_keyboard(id=current_item_id))


@dp.message_handler(text=['Скрыть клавиатуру'])
async def answer_item_command(message: types.Message):
    await message.answer(text= 'Мы ее спрятали',
                        reply_markup = see_commands_default_keyboard)



@dp.message_handler(content_types=['contact'])
async def answer_item_command(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await message.answer(text= 'Регистрация прошла успешно',
                         reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text= 'Увы(',
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands='info')
async def answer_info_command(message: types.Message):
    await message.answer(text= 'Список команд представлен на клавиатуре',
                          reply_markup=info_commands_default_keyboard)


@dp.message_handler(content_types=['location'])
async def answer_info_command(message: types.Message):
    await message.answer(text= 'Я вижу где ты',
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text=['Контакты продавца'])
async def answer_item_command(message: types.Message):
    await message.answer(text= '123456789',
                        reply_markup = info_commands_default_keyboard)

@dp.message_handler(text=['Пункты самовывоза'])
async def answer_item_command(message: types.Message):
    await message.answer(text= f'Ромашкова, 7'
                        f'\nОдуванчиковая, 3'
                         f'\nВасильковая, 44'
                         f'\nПионовая, 17',
                        reply_markup = info_commands_default_keyboard)

@dp.message_handler(text=['Время работы'])
async def answer_item_command(message: types.Message):
    await message.answer(text= 'Понедельник - воскресенье с 8-00 до 20-00',
                        reply_markup = info_commands_default_keyboard)