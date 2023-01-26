#'5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM'
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from aiogram import Bot, Dispatcher, executor, types
#import const
#from questions import q
import random
import base
import task


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


bot = Bot(token='5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM')
dp = Dispatcher(bot)

answer = 0
SHOW_VARIANTS = False    # показывать ли варианты ответов
VARS_NUM = 5
lang = 'en'


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
    global answer, print_task, right_answer, sample, log, base_, base_add
    if answer != 0:
        answer = message.text
        check, check_txt = task.get_check(answer, right_answer)
        await message.answer(check_txt)
        log['answer'] = answer
        log['check'] = check
        base.to_log(log, SHOW_VARIANTS)
        base.base_update(base_, base_add, log)

        base_, base_add = base.get_base(VARS_NUM)
        print_task, right_answer, sample, log = run(base_, lang)
        await message.answer(print_task)

        # answer = input(print_task)


    else:
        base_, base_add = base.get_base(VARS_NUM)
        print_task, right_answer, sample, log = run(base_, lang)
        await message.answer(print_task)
        answer = message.text




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)










# base_, base_add = base.get_base(VARS_NUM)
# print_task, right_answer, sample, log = run(base_, lang)
# print(print_task)
# #answer = input(print_task)
#
# answer = input('Your answer:')
# check = task.get_check(answer, right_answer)
# log['answer'] = answer
# log['check'] = check
# base.to_log(log, SHOW_VARIANTS)
# base.base_update(base_, base_add, log)
