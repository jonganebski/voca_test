import requests
from bs4 import BeautifulSoup
from random import *

URL = 'https://www.spanishdict.com/translate'
headers = {'User-Agent': 'Mozilla/5.0'}
TOTAL_questions = 5
previous_nums = []

def get_word():
    words_file = open('words_spanish.txt', 'r')
    WORD_LIST = words_file.read().split(',')
    WORD_LIST.pop()
    words_file.close()
    radnom_num = randint(0, len(WORD_LIST)-1)
    WORD = (WORD_LIST[radnom_num]).lower()
    return WORD

def req_bs4(WORD):
    request_site = requests.get(f'{URL}/{WORD}', headers=headers)
    soup_html = BeautifulSoup(request_site.content, 'html5lib')
    soup_class = soup_html.find_all('div', {'class': '_2VJwFW1Z _2Gv8ITgB'})
    return soup_class

def get_meanings(WORD):
    soup_class = req_bs4(WORD)
    meanings = []
    for i in soup_class:
        soup_meaning = i.find('a').string
        meanings.append(soup_meaning)
    return meanings

def pregunta():
    for n in range(TOTAL_questions):
        WORD = get_word()
        meanings_list = get_meanings(WORD)
        text = f"'{meanings_list[0]}'"
        if len(meanings_list) >= 2:
            for i in meanings_list[1:]:
                text += f" or '{i}'"
        answer = input(f'{n+1}.What is {text} in Spanish? ')
        if answer.lower() == WORD.lower():
            print('Correct')
        else:
            print(f"Wrong. it is '{WORD}'.")

pregunta()

