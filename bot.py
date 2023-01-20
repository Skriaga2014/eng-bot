#'5891767200:AAGSRE4qcouHrjJiwXjV4-nW2Ro_endLw0M'
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from aiogram import Bot, Dispatcher, executor, types
import const
from questions import q
import random

bot = Bot(token=const.token)
dp = Dispatcher(bot)

#global var
var = 0

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer_photo(open(f"images/intro.jpg", 'rb'))
    await message.answer("Hi, I'm a PDD_Bot! \nFor beginning send any message:")


# urlkb = InlineKeyboardMarkup(row_width=1, width='100%')
# urlButton = InlineKeyboardButton(text='Перейти в блог Skillbox', url='https://skillbox.ru/media/code/')
# urlButton2 = InlineKeyboardButton(text='12345678901234567890123456789012345678901234', url='https://skillbox.ru/code/')
# urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='task')
async def url_command(message: types.Message):
    await message.answer_photo(open(f"images/intro.jpg", 'rb'))
    await message.answer('Полезные ссылки:', reply_markup=taskkb)



@dp.message_handler()
async def echo(message: types.Message):
    global var
    if var != 0:
        if message.text == q[var][0]:
            await message.answer("It's right!")
        else:
            await message.answer(f'its a wrong answer (right {q[var][0]})')

    #for i in range(10):
    var = random.choice(list(q.keys()))
    #await message.answer(f"{var}/{list(q.keys())}")
    vars = q[var][1]
    random.shuffle(vars)

    kb = [
        [types.KeyboardButton(text=vars[0])],
        [types.KeyboardButton(text=vars[1])],
        [types.KeyboardButton(text=vars[2])],
        [types.KeyboardButton(text=vars[3])]
        ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, row_width=1)
    #await bot.send_photo(photo='images/1000.jpg')
    await message.answer_photo(open(f"images/{var}.jpg", 'rb'))
    await message.answer(f'Question {var} must be here', reply_markup=keyboard)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)








