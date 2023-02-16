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

new_words2 = pd.read_csv('new_words2.csv')
id_col = [i + 1 for i in range(len(new_words2))]
new_words2['new_id'] = id_col
new_words2['eng'] = new_words2['eng'].str.lower()

base_final = base_final.merge(new_words2, left_on='eng', right_on='eng', how='left')
print(base_final)

TXT = 'hang out'

words = TXT.split(', ') if ',' in TXT else TXT.split(' ')
print(words)
base_final['id'] = base_final['id'].astype(str)
base_final['new_id'] = base_final['new_id'].astype(str)

word_to_line = base_final.loc[base_final['eng'].isin(words), ['id', 'new_id', 'eng', 'transcription', 'rus']]
word_to_line['len_eng'] = word_to_line['eng'].str.len()
word_to_line = word_to_line.sort_values(by='len_eng', ascending=False)
word_to_line = word_to_line.drop(columns=['len_eng'])
print(word_to_line, '\n')

for word in word_to_line['eng']:
    TXT = TXT.replace(word, word_to_line.loc[word_to_line['eng'] == word, ['transcription']].iloc[0, 0][1:-1])
# print('----------------', word_to_line.loc[word_to_line['eng'] == 'heap', ['transcription']].iloc[0, 0])
TXT = '[' + TXT + ']'
print('----------', TXT)
for i in word_to_line.values:
    new_line = ';'.join(i)
    print(f'{new_line};0;0;')

print(pd.read_csv('my_dict.csv', sep=';')['id'].max())



