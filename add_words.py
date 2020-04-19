def checking(new):
    file = open('words_spanish.txt', 'r')
    list = file.read().split(',')
    file.close()
    for i in list:
        if i == new:
            return False
            break
    retuen True

def adding_new_word(new):
    file = open('words_spanish.txt', 'a')
    check = checking(new)
    if check:
        file.write(f'{new},')
        print(f"'{new}' is added to the list.")
    else:
        print(f"'{new}' already exists in the list.")
    file.close()

adding_new_word('trece')
