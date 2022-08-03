def rhythm_checker(text: str):
    strings = text.split()
    vowels = []
    for i in strings:
        for j in strings:
            if [x for x in i if x == 'а'] != [x for x in j if x == 'а']:
                return 'Пам парам'
    return 'Парам пам-пам'


rhyme = input('Введи стишок: ')
print(rhythm_checker(rhyme))