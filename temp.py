import pandas as pd
import selenium


# with open('newfile.csv', 'r') as newfile:
#     base = newfile.re
pd.set_option('display.expand_frame_repr', False)
base = pd.read_csv('newfile.csv', sep=';')
base2 = pd.read_csv('unigram_freq.csv')
base2['id'] = range(1, len(base2) + 1)
base3 = base2.merge(base, left_on='word', right_on='eng', how='left').fillna('')
#base_new = base3.loc[base3['rus'] == '', ['word']]
base3 = base3.loc[base3['eng'] != '']
print(base3[500:550])

# with open('for_pars_words.txt', 'a') as file:
#     for i in base_new['word']:
#         file.write(f'{i}\n')
