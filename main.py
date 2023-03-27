def prog1(cap):
    capitals = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                 "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}

    for a in capitals:
        print("{}: {}".format(a, capitals[a]))

    print(capitals.get(cap))

    sortedDict = dict(sorted(capitals.items(), key=lambda x: x[0].lower()))

    for k, v in sortedDict.items():
        print('{}: {}'.format(k, v))


def prog2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    word = input().lower()
    counter = 0
    for a in word:
        o = alph[a]
        counter += o
    print(counter)



def prog3():
    count = input('Колво студентов: ')
    language_set = set()
    chinese_count = 0
    for i in range(int(count)):
        prompt = 'Введите языки студента {}: '.format(i + 1)
        languages = input(prompt).split(', ')
        language_set.update(languages)
        for lang in languages:
            if lang == 'Chinese':
                chinese_count += 1
    language_list = list(language_set)
    language_list.sort()
    print('Студенты знают: ', len(language_list), 'языков')
    print('Языки: ', language_list)
    print('Знают китайский: ', chinese_count)



prog3()