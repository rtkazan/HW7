def ritm(str):
    str = str.split()
    list_1 = []
    for i in str:
        sum_word = 0
        for j in i:
            if j in 'аеёиоуыэюя':
             sum_word += 1
        list_1.append(sum_word)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-да'
if ritm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')