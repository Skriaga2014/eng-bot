#'5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM'
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from aiogram import Bot, Dispatcher, executor, types
import const
from questions import q
import random
import base
import task

bot = Bot(token='5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM')
dp = Dispatcher(bot)

#global var
var = 0

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    #await message.answer_photo(open(f"images/intro.jpg", 'rb'))
    await message.answer("Hi, I'm a ReedOriginal_Bot! \nFor beginning send any message:")


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




def run(base_, lang):
    idx, task_, right_answer, sample = task.get_task(base_, lang)
    print_task = ', '.join(task_) if type(task_) == list else task_
    # if SHOW_VARIANTS:
    #     print(print_task)
    #     variants = base_['translate'] if lang == 'ru' else base_[['word', 'transcription']]
    #     variants.index = range(1, len(base_) + 1)
    #     print(variants)
    #     answer = input('Enter number or word: ')
    #     if answer.isdigit():
    #         if lang == 'ru':
    #             answer = variants.loc[int(answer)]
    #         else:
    #             answer = variants.loc[int(answer), 'word']
    # else:
    #     answer = input(f'{print_task}: ')
    log = {'idx': idx, 'task': task_, 'right_answer': right_answer, 'lang': lang}
    return print_task, right_answer, sample, log


SHOW_VARIANTS = False    # показывать ли варианты ответов
VARS_NUM = 5
lang = 'en'

base_, base_add = base.get_base(VARS_NUM)
print_task, right_answer, sample, log = run(base_, lang)
print(print_task)
#answer = input(print_task)
answer = input('Your answer:')
check = task.get_check(answer, right_answer)
log['answer'] = answer
log['check'] = check
base.to_log(log, SHOW_VARIANTS)
base.base_update(base_, base_add, log)
