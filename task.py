def get_task(base_, lang):
    sample = base_.sample()
    smpl = sample['sample'].iloc[0]
    transcription = sample['transcription'].iloc[0]
    if lang == 'ru':
        task = sample['translate'].iloc[0]
        right_answer = sample['word'].iloc[0]
    else:
        task = sample['word'].iloc[0]
        right_answer = sample['translate'].iloc[0]
    idx = sample['id'].iloc[0]
    return idx, task, right_answer, transcription, smpl


def get_check(answer, right_answer):
    if answer == right_answer:
        return 1
    elif ',' in right_answer and answer in right_answer.split(', '):
        return 1
    else:
        return 0
        # return 0, f'NO!\n{right_answer}'

