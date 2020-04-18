import requests
from bs4 import BeautifulSoup
from random import *
import html5lib

WORD_LIST = ['pequeno', 'nevera', 'mujer', 'sombrero', 'mensaje', 'baloncesto', 'preocupado', 'escuchar']
URL = 'https://www.spanishdict.com/translate'
headers = {'User-Agent': 'Mozilla/5.0'}

def get_word():
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
    WORD = get_word()
    meanings_list = get_meanings(WORD)
    text = f"'{meanings_list[0]}'"
    if len(meanings_list) >= 2:
        del meanings_list[0]
        for i in meanings_list:
            text += f" or '{i}'"
    answer = input(f'What is {text} in Spanish? ')
    if answer.lower() == WORD.lower():
        print('Correct')
    else:
        print(f"Wrong. it is '{WORD}'.")

pregunta()

