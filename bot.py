#'5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM'
import time

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from aiogram import Bot, Dispatcher, executor, types

import random
import base
import task


def run(base_, lang):
    idx, task_, right_answer, transcription, sample = task.get_task(base_, lang)
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
    return print_task, right_answer, transcription, sample, log


version = 0.02

bot = Bot(token='5817828615:AAFf_L7BwZPLprTn-vPXQiQ1QtXFaxfL2IM')
dp = Dispatcher(bot)

count = 0
answer = 0
SHOW_VARIANTS = False    # показывать ли варианты ответов
VARS_NUM = 5
FREQUENCY_OF_OLD = 3
# lang = 'en'


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi, I'm a ReedOriginal_Bot! \nFor beginning send any message:")


@dp.message_handler(commands=['add'])
async def url_command(message: types.Message):
    data = message.get_args()
    with open('new_words.csv', 'a') as file:
        file.write(f'{data}\n')
    file.close()

@dp.message_handler(commands=['version', 'ver'])
async def url_command(message: types.Message):
    await message.answer(version)


@dp.message_handler()
async def echo(message: types.Message):
    global answer, print_task, right_answer, transcription, sample, log, base_, base_add, lang, count

    if answer != 0:


        answer = message.text.lower()
        check = task.get_check(answer, right_answer)
        if lang == 'ru':
            if check:
                await message.answer('YES!')
            else:
                await message.answer(f'NO!\n{right_answer}\n{transcription}')
            await message.answer(sample.replace(right_answer, right_answer.upper()))
        else:
            verdict = 'YES!'
            if not check:
                verdict = f'NO!\n{right_answer}'
            if ',' in right_answer:
                # await message.answer(f'{check_txt}\n{right_answer}')
                if check:
                    await message.answer(verdict + '\n' + right_answer)
                if not check:
                    await message.answer(verdict)
            else:
                await message.answer(verdict)
            await message.answer(sample.replace(print_task, print_task.upper()))    # worked
            # await message.answer(check_txt)
            # await message.answer(sample.replace(print_task, print_task.upper()))
        log['answer'] = answer
        log['check'] = check
        base.to_log(log, SHOW_VARIANTS)
        base.base_update(base_, base_add, log)
        time.sleep(1)
        lang = random.choice(['ru', 'en'])
        count += 1

        if count % FREQUENCY_OF_OLD == 0:
            VARS_NUM_NEW = float('inf')
        else:
            VARS_NUM_NEW = VARS_NUM

        base_, base_add = base.get_base(VARS_NUM_NEW)
        print_task, right_answer, transcription, sample, log = run(base_, lang)
        if lang == 'en':
            await message.answer(f'{print_task}\n{transcription}')
        else:
            await message.answer(print_task)


    else:
        lang = random.choice(['ru', 'en'])
        base_, base_add = base.get_base(VARS_NUM)
        print_task, right_answer, transcription, sample, log = run(base_, lang)

        if lang == 'en':
            await message.answer(f'{print_task}\n{transcription}')
        else:
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
