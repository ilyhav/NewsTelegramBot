from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import random
from aiogram import types
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

sports = {'Футбол': 'https://t.me/rflive',
          'Баскетбол': 'https://t.me/all_about_nba',
          'Хоккей': 'https://t.me/khl_official_telegram',
          'Волейбол': 'https://t.me/volleyVFV',
          'Большой теннис': 'https://t.me/elitetennis',
          'Гандбол': 'https://t.me/rushandball'}

menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
menu = [types.KeyboardButton('Выбрать спорт'),
        types.KeyboardButton('Информация'),
        types.KeyboardButton('Рандом')]

for item in menu:
    menu_markup.add(item)

sport_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

menu = []
for s in sports.keys():
    menu.append(types.KeyboardButton(text=s))
back = types.KeyboardButton('Назад')
menu.append(back)
for item in menu:
    sport_markup.add(item)

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
BOT = Bot(token=TOKEN)
dp = Dispatcher(BOT, storage=storage)

athletes = {'Футбол': 'https://i.sprts.ru/preset/wysiwyg/2/b5/92a787f9211edb4b3b2f9ef93864a.jpeg',
          'Баскетбол': 'https://thelawofattraction.ru/wp-content/uploads/2/8/f/28f77b2bb4cbf03b3a61193b031a49cc.jpeg',
          'Хоккей': 'http://www.hockeyrussia.ru/uploads/posts/2019-04/1556632825_168865297.0.jpg',
          'Волейбол': 'https://zenit-kazan.com/photo_1494432619_1.jpg',
          'Большой теннис': 'http://almode.ru/uploads/posts/2021-03/1616442348_54-p-mariya-sharapova-59.jpg',
          'Гандбол': 'https://rushandball.ru/Files/Publications/p5qaevej.jpg'}

citation = {'Футбол': "Футбол – это не вопрос жизни и смерти. Он намного важнее!",
          'Баскетбол': "Границы, так же как и страхи, чаще всего оказываются просто иллюзиями",
          'Хоккей': "У меня к жизни отношение спортивное: если что-то не удается, "
                    "это еще не значит, что этого не надо добиваться.",
          'Волейбол': "Для игроков волейбол-это работа, Для «боссов» волейбол — это деньги, "
                      "Для зрителей волейбол- это шоу, Для всех нас волейбол- это жизнь!",
          'Большой теннис': "Я никогда не сдаюсь. Вы можете сбить меня с ног десять раз подряд, "
                            "и я поднимусь в одиннадцатый и запулю желтым мячиком прямо в вас.",
          'Гандбол': "Если чего-то хочется, не люблю себе отказывать, больше даже в каком-то ментальном смысле, "
                     "чтобы не стрессовать. Если чего-то хочется, то удовольствие, конечно, нужно получать."}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    output = f'Привет, {message.from_user.first_name}, рад видеть тебя!'
    await message.answer(text=output, reply_markup=menu_markup)


@dp.message_handler(content_types='text', text='О боте')
async def help_def(message):
    output = f'Привет! Я - бот для публикации ссылок на спортивные тг-каналы!'
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Выбрать спорт')
async def choose_sport(message):
    await message.answer(text='Выберите спорт', reply_markup=sport_markup)


@dp.message_handler(content_types='text', text='Информация')
async def get_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('О боте')
    back = types.KeyboardButton('Назад')
    markup.add(item1, back)
    await message.answer(text='Информация', reply_markup=markup)


@dp.message_handler(content_types='text', text='Назад')
async def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = [types.KeyboardButton('Выбрать спорт'),
            types.KeyboardButton('Информация'),
            types.KeyboardButton('Рандом')]
    for item in menu:
        markup.add(item)
    await message.answer(text='Назад', reply_markup=markup)


@dp.message_handler(content_types='text', text='Футбол')
async def football(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Баскетбол')
async def basketball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Хоккей')
async def hockey(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Волейбол')
async def volleyball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Большой теннис')
async def tennis(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Гандбол')
async def gandball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    phrase = citation[message.text]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='Рандом')
async def random_link(message):
    output = random.choice(list(sports.keys()))
    picture = athletes[output]
    phrase = citation[output]
    await BOT.send_photo(message.chat.id, photo=picture, caption=phrase)
    await message.answer(text=sports[output])


@dp.message_handler()
async def button_message(message):
    if message.text.lower() in ["привет", 'добрый день']:
        output = 'Приветствую!'
    elif message.text[-1] == '?':
        output = 'Введите /help, чтобы получить информацию или выберите спорт, чтоб получить новости'
    else:
        output = 'Интересная мысль, я обдумаю её.'
        await message.answer(text=output)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
