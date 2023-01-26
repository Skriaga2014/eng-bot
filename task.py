def get_task(base_, lang):
    sample = base_.sample()
    smpl = sample['sample'].iloc[0]
    if lang == 'en':
        task = sample['translate'].iloc[0]

        #task = f'{task}\n{smpl}'
        right_answer = sample['word'].iloc[0]
    else:
        task = sample['word'].iloc[0]
        right_answer = sample['translate'].iloc[0]
    if '/' in task:
        task = task.split('/')
    idx = sample['id'].iloc[0]
    return idx, task, right_answer, smpl


def get_check(answer, right_answer):
    if answer == right_answer or answer in right_answer:
        print('yes')
        #print(right_sample)
        return 1
    else:
        print('no')
        print(f'({right_answer})')
        return 0

