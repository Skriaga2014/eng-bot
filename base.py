import pandas as pd
import os
import datetime as dt


def get_base(VARS_NUM):
    # проверка, есть ли nan в shows и/или result
    try:
        base = pd.read_csv(BASE_FILE, sep=';', dtype={'shows': int, 'result': int})
    except ValueError:  # если nan найдено
        base = pd.read_csv(BASE_FILE, sep=';').fillna(0)
        base = base.astype({'shows': 'int32', 'result': int})
    except KeyError:    # если проблема с базой в результате сбоя предыдущей выгрузки
        base = pd.read_csv(BASE_FILE_RESERVE, sep=';').fillna(0)
        base = base.astype({'shows': 'int32', 'result': int})

    if len(base) < VARS_NUM:    # если количество слов в базе меньше
        vars_num = len(base)
    else:
        vars_num = VARS_NUM

    base = base.sort_values('result')
    base_new = base.head(vars_num).sample(frac=1)
    base_add = base.tail(len(base) - vars_num)

    return base_new, base_add


def to_log(log, SHOW_VARIANTS):    # date,variants, type,id,task,target,answer,result
    line = f'\n{dt.datetime.now()};{SHOW_VARIANTS};'
    if type(log['task']) == list:
        log['task'] = '/'.join(log['task'])
    log_items = ['lang', 'idx', 'task', 'right_answer', 'answer', 'check']
    line += ';'.join([str(log[i]) for i in log_items])

    with open(LOG_FILE, 'a') as f:
        f.write(line)


def base_update(base, base_add, log):
    base.loc[base['id'] == log['idx'], ['shows']] += 1
    if log['check']:
        base.loc[base['id'] == log['idx'], ['result']] += 1
    base_final = pd.concat([base, base_add])
    base_final = base_final.sort_values(by=['result'])
    base_final.to_csv(BASE_FILE, index=0, sep=';')
    base_final.to_csv(BASE_FILE_RESERVE, index=0, sep=';')


BASE_FILE = os.path.join(os.getcwd(), 'my_dict.csv')
BASE_FILE_RESERVE = os.path.join(os.getcwd(), 'my_dict_r.csv')
LOG_FILE = os.path.join(os.getcwd(), 'log.csv')
pd.set_option('display.expand_frame_repr', False)



