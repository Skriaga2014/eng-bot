import pandas as pd
import selenium


# with open('newfile.csv', 'r') as newfile:
#     base = newfile.re
pd.set_option('display.expand_frame_repr', False)
base = pd.read_csv('newfile.csv', sep=';')                                          # base of popular words
base2 = pd.read_csv('unigram_freq.csv')                                             # base of popular score
base2['id'] = range(1, len(base2) + 1)
base_final = base2.merge(base, left_on='word', right_on='eng', how='left').fillna('')
base_final = base_final.loc[base_final['eng'] != '']
base_transcription = pd.read_csv('pars_result.csv', sep=';')                        # base of parsed words
base_final = base_final.merge(base_transcription, left_on='eng', right_on='eng', how='left').fillna('')
base_final['rus'] = [base_final['rus_y'][i] if base_final['rus_y'][i] != '' else base_final['rus_x'][i] for i in range(len(base_final))]
#base_final = base_final.set_index('id')

WORDS = 'suggest, supply, heat, plumb'
WORDS = WORDS.split(', ')
print(WORDS)
WORDS = 'consider'
base_final['id'] = base_final['id'].astype(str)
word_to_line = base_final.loc[base_final['eng'] == WORDS, ['id', 'eng', 'transcription', 'rus']]
print(';'.join(word_to_line.values.flatten().tolist()))

