
dictionary = []
with open("count_1w.txt") as words:  # segmentation of text - some words data
    for line in words:
        l = line.split('\t')
        dictionary.append([l[0], int(l[1].replace('\n', ''))])

# print(dictionary[:100])


def max_sootv(word, dictionary, space=None, prob=1):
    if space is None:
        space = []
    if word:
        mb = []
        for i in dictionary:
            if word.startswith(i[0]):
                mb.append(i)
        if not mb:  # если не было найдено соответсвий в словаре
            space.append(word[0])
            dictionary.append([word[0], 0])
            dictionary = [[i[0], i[1]+1] for i in dictionary]
            s = sum([i[1] for i in dictionary])
            return max_sootv(word[1:], dictionary, space, prob*(1/s))
        else:  # если соответсвия есть
            p = [i[1] for i in mb]
            key_word = mb[p.index(max(p))]
            space.append(key_word[0])
            s = sum([i[1] for i in dictionary])
            return max_sootv(word[len(key_word[0]):], dictionary,
                             space, prob*(key_word[1]/s))
    else:
        return space, prob


def max_sootv_back(word, dictionary, space=None, prob=1):
    if space is None:
        space = []
    if word:
        mb = []
        for i in dictionary:
            if word.endswith(i[0]):
                mb.append(i)
        if not mb:  # если не было найдено соответсвий в словаре
            space.insert(0, word[-1])
            dictionary = [[i[0], i[1] + 1] for i in dictionary]
            dictionary.append([word[0], 0])
            s = sum([i[1] for i in dictionary])
            return max_sootv_back(word[:-1], dictionary, space, prob*(1/s))
        else:  # если соответсвия есть
            p = [i[1] for i in mb]
            key_word = mb[p.index(max(p))]
            space.insert(0, key_word[0])
            s = sum([i[1] for i in dictionary])
            return max_sootv_back(word[:-len(key_word[0])], dictionary,
                                  space, prob*(key_word[1]/s))
    else:
        return space, prob


def duo_max_sootv(word, dictionary):
    t1 = max_sootv(word, dictionary)
    t2 = max_sootv_back(word, dictionary)
    if t1[1] > t1[1]:
        return t1[0]
    else:
        return t2[0]


# формирование своего словаря
l = ['theme', 'the', 'them', 'end', 'me', 'men', 'mend', 'in', 'dine', 'her', 'here']
my_dictionary = []
for i in l:
    for j in dictionary:
        if i == j[0]:
            my_dictionary.append([i, j[1]])

word0 = 'themendinehere'
print('исходное слово: ', word0)
print('\nпрямой метод')
print(max_sootv(word0, my_dictionary))

print('\nобратный метод')
print(max_sootv_back(word0, my_dictionary))

print('\nдвунаправленный метод')
print(duo_max_sootv(word0, my_dictionary))
