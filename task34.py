"""Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам   Парам пам-пам"""
"""
def count_rhyme(texts):
    text1 = texts.split(' ')
    count = 0
    #count_word = 0
    letters = 'аеёиоуыэюя'
    for words in text1:
        #count_word += 1
        for i in words:
            if i in letters:
                count +=1
    if count % len(text1) == 0:
        print('Парам пам-пам')
    else:
        print('Пам парам')
    
chant_vinny = input('Придумайте кричалку: ')
count_rhyme(chant_vinny)"""

def count_rhyme(texts):
    text1 = texts.split(' ')
    count = 0
    letters = 'аеёиоуыэюя'
    for words in text1:
        for i in words:
            if i in letters:
                count +=1
    return count % len(text1) == 0
    
chant_vinny = input('Придумайте кричалку: ')
if count_rhyme(chant_vinny):
    print('Парам пам-пам')
else:
    print('Пам парам')