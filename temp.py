import pandas as pd
import selenium


# with open('newfile.csv', 'r') as newfile:
#     base = newfile.re
pd.set_option('display.expand_frame_repr', False)
base = pd.read_csv('newfile.csv', sep=';', na_filter=False)
base = base.loc[(base['error'] == '') & (base['status'] == 'word'), ['num', 'eng', 'rus', 'status']]
#print(base[base['error'] == '', ['num', 'eng', 'rus', 'status']])
print(base)
#print(base)


