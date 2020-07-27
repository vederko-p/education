
dictionary = []
with open("count_1w.txt") as words:
    for line in words:
        dictionary.append(line.split('\t')[0])


def max_sootv(word, dictionary, space=None):
    if space is None:
        space = []
    if word:
        mb = []
        for i in dictionary:
            if word.startswith(i):
                mb.append(i)
        if not mb:  # если не было найдено соответсвий в словаре
            space.append(word[0])
            return max_sootv(word[1:], dictionary, space)
        else:  # если соответсвия есть
            t = [len(i) for i in mb]
            key_word = mb[t.index(max(t))]
            space.append(key_word)
            return max_sootv(word[len(key_word):], dictionary, space)
    else:
        return space


def max_sootv_back(word, dictionary, space=None):
    if space is None:
        space = []
    if word:
        mb = []
        for i in dictionary:
            if word.endswith(i):
                mb.append(i)
        if not mb:  # если не было найдено соответсвий в словаре
            space.insert(0, word[-1])
            return max_sootv_back(word[:-1], dictionary, space)
        else:  # если соответсвия есть
            t = [len(i) for i in mb]
            key_word = mb[t.index(max(t))]
            space.insert(0, key_word)
            return max_sootv_back(word[:-len(key_word)], dictionary, space)
    else:
        return space


# word1 = 'tableapplechairtablecupboarding'
# print('исходное слово: ', word0)
# t = max_sootv(word0, dictionary)
# print(t)
# print(max_sootv_back(word0, dictionary))


def duo_max_sootv(word, dictionary):
    t1 = max_sootv(word, dictionary)
    t2 = max_sootv_back(word, dictionary)
    sgm1 = len([i for i in t1 if i in dictionary])
    sgm2 = len([i for i in t2 if i in dictionary])
    if sgm1 > sgm2:
        return t1
    else:
        return t2


word0 = 'themendinehere'
dictionary = ['theme', 'the', 'them', 'end', 'me', 'men', 'mend', 'in', 'dine', 'her', 'here']
print('прямой:')
print(max_sootv(word0, dictionary))
print('\nобратный:')
print(max_sootv_back(word0, dictionary))
print('\nдвунаправленный:')
print(duo_max_sootv(word0, dictionary))
