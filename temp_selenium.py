import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
#from bs4 import BeautyfulSoup

with open('for_pars_words.txt', 'r') as file:
    vocabulary = file.read().split('\n')
    file.close()



print(vocabulary, len(vocabulary))
driver = webdriver.Chrome()

time.sleep(10)
with open('pars_result2.csv', 'r') as file:
    pars_list = file.read().split('\n')
    file.close()

parsed_list = [i.split(';')[0] for i in pars_list]
print(parsed_list)

for word in vocabulary:
    if word not in parsed_list:
        driver.get(f'https://wooordhunt.ru/word/{word}')
        sleep(1)
        try:
            transcription = driver.find_element(By.CLASS_NAME, 'transcription').text
        except:
            transcription = ''
        transcription = f'[{transcription[1:-1]}]'
        try:
            rus = driver.find_element(By.CLASS_NAME, 't_inline_en').text
        except:
            rus = ''
        with open('pars_result2.csv', 'a') as file:
            file.write(f'{word};{transcription};{rus};{};\n')
            file.close()





