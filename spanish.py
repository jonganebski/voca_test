# SPANISH VOCABULARY#

from random import *

print('Write in Spanish')
right_answer = 'el ciudad'

for i in range(3):
  question = input('the city: ').lower()
  if question == right_answer:
    print('correct')
    break
  elif 1 <= i < 3:
    prop = round(len(right_answer) * 0.3)
    random_nums = []
    for s in range(prop):
      random_nums.append(randint(0, len(right_answer) - 1))  # 문제점: 중복되는 수가 도출될 수 있음.
    hint = 'hint: '
    for n in range(len(right_answer)):
      if n in random_nums:
        hint += right_answer[n]
      else:
        if right_answer[n] == ' ':
          hint += ' '
        else:
          hint += '?'
    print(hint)
  else:
    print('wrong')
