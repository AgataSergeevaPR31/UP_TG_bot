import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = '8033759336:AAHBmbgg3DIsSoDxrLILIrdK4N_t7gPaB9A'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply("Hi! Ya samiy luchshiy.")

@dp.message(Command(commands=['play']))
async def play_game(message: Message):
    await message.reply("Камень? Ножницы? Бумага? Раз, два, три...")

@dp.message()
async def echo(message: Message):
    me = message.text
    elem = ['Камень', 'Ножницы', 'Бумага']
    
    if me in elem:
        bot = random.choice(elem)
        await message.answer(f"Твой выбор {me.capitalize()}\nА мой выбор {bot.capitalize()}")
        
    else:
        await message.answer("Камень? Ножницы? Бумага: Раз, два, три...")

    if me == bot:
        await message.answer("Ничья!")
    elif (me == 'Камень' and bot == 'Ножницы') or (me == 'Ножницы' and bot == 'Бумага') or (me == 'Бумага' and bot == 'Камень'):
        await message.answer("Ну молодец!")
    else:
        await message.answer("Я круче тебя!")

async def qwert():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(qwert())
