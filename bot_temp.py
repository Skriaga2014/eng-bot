"""
Программа изучения слов иностранного языка.
Выводит случайное слово из числа (VARS_NUM) слов, которые были верно переведены минимальное число раз.
Направление перевода (на русский или с русского) выбирается случайным образом.
"""

import pandas as pd
import datetime as dt
import os
import random as rnd
import base
import task


# load dictionary



# send to log



# update my dict



# get word for translate



# check answer right or wrong




# show task
def run(base_, lang):
    #idx, task, right_answer = get_task(base, lang)
    idx, task_, right_answer, sample = task.get_task(base_, lang)

    print_task = ', '.join(task_) if type(task_) == list else task_
    if SHOW_VARIANTS:
        print(print_task)
        variants = base_['translate'] if lang == 'ru' else base_[['word', 'transcription']]
        variants.index = range(1, len(base_) + 1)
        print(variants)
        answer = input('Enter number or word: ')
        if answer.isdigit():
            if lang == 'ru':
                answer = variants.loc[int(answer)]
            else:
                answer = variants.loc[int(answer), 'word']
    else:
        answer = input(f'{print_task}: ')

    check = task.get_check(answer, right_answer)
    print(sample.replace(right_answer, right_answer.upper()))



    return {'check': check, 'idx': idx, 'task': task_,
            'right_answer': right_answer,
            'answer': answer, 'lang': lang}


SHOW_VARIANTS = False    # показывать ли варианты ответов
VARS_NUM = 5
lang = 'en'



base_, base_add = base.get_base(VARS_NUM)
log = run(base_, lang)
base.to_log(log, SHOW_VARIANTS)
base.base_update(base_, base_add, log)



