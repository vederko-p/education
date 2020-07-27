
def get_y(distrib, y):
    for i in distrib:
        if distrib[i] == y:
            return i


def gale_shep(frst, scnd):
    clearx, cleary = [i for i in frst], [j for j in scnd]
    d = {}
    while clearx:
        nwtc = []  # no way to choose by y
        for j in scnd:  # идем по каждому y
            candidates = []
            non = []
            for i in clearx:  # проверяем каждый x без пары
                if frst[i]['pref'][0] == j:
                    candidates.append(i)
            # сформировали список кандидатов для одного y
            candidates_rangs = [scnd[j]['pref'].index(cand) for cand in candidates]
            if candidates:  # для каждого y отберем наиболее предпочтительный x
                best = candidates[candidates_rangs.index(min(candidates_rangs))]
                # проверка, не имеет ли уже худший х, чем best, пару с y
                if j in d.values():  # если имелась такая пара, то удалим ее
                    prev = get_y(d, j)
                    d.pop(prev)
                    clearx.append(prev)  # и добавим предыдущий x в clearx
                d[best] = j
                # сформируем список тех, кого y точно не выберет
                bst_ind = scnd[j]['pref'].index(best)
                non = scnd[j]['pref'][bst_ind + 1:]
                # оставим только остальных, т.е. удалим все ненужные x из предпочтений каждого y
                scnd[j]['pref'] = scnd[j]['pref'][:bst_ind + 1]
            nwtc.append([j, non])
        # удалим все ненужные y из предпочтений каждого x
        for i in frst:  # все x
            for j in nwtc:  # отсутствие предпочтения у всех y
                if i in j[1]:
                    frst[i]['pref'].remove(j[0])
        # в clearx добавим те x, которые остались без пары
        clearx.clear()
        for i in frst:
            if not i in d:
                clearx.append(i)
        # в cleary добавим те y, которые стались без пары
        cleary.clear()
        for j in scnd:
            if not j in d.values():
                cleary.append(j)
    # возвращаем short-list'ы и распределение
    return frst, scnd, d


txprofile = {'x1': {'pref': ['y2', 'y3', 'y1', 'y5', 'y4'], 'qoute': 1}, 'x2': {'pref': ['y5', 'y2', 'y3', 'y1', 'y4'], 'qoute': 1}, 'x3': {'pref': ['y5', 'y3', 'y4', 'y1', 'y2'], 'qoute': 1}, 'x4': {'pref': ['y5', 'y1', 'y3', 'y4', 'y2'], 'qoute': 1}, 'x5': {'pref': ['y5', 'y1', 'y4', 'y3', 'y2'], 'qoute': 1}}
typrofile = {'y1': {'pref': ['x2', 'x5', 'x1', 'x4', 'x3'], 'qoute': 1}, 'y2': {'pref': ['x1', 'x5', 'x3', 'x4', 'x2'], 'qoute': 1}, 'y3': {'pref': ['x1', 'x4', 'x3', 'x5', 'x2'], 'qoute': 1}, 'y4': {'pref': ['x3', 'x5', 'x4', 'x1', 'x2'], 'qoute': 1}, 'y5': {'pref': ['x3', 'x5', 'x4', 'x1', 'x2'], 'qoute': 1}}

xprofile = {'x1': {'pref': ['y3', 'y1', 'y5', 'y7', 'y4', 'y2', 'y8', 'y6'], 'qoute': 1}, 'x2': {'pref': ['y6', 'y1', 'y3', 'y4', 'y8', 'y7', 'y5', 'y2'], 'qoute': 1}, 'x3': {'pref': ['y7', 'y4', 'y3', 'y6', 'y5', 'y1', 'y2', 'y8'], 'qoute': 1}, 'x4': {'pref': ['y5', 'y3', 'y8', 'y2', 'y6', 'y1', 'y4', 'y7'], 'qoute': 1}, 'x5': {'pref': ['y4', 'y1', 'y2', 'y8', 'y7', 'y3', 'y6', 'y5'], 'qoute': 1}, 'x6': {'pref': ['y6', 'y2', 'y5', 'y7', 'y8', 'y4', 'y3', 'y1'], 'qoute': 1}, 'x7': {'pref': ['y7', 'y8', 'y1', 'y6', 'y2', 'y3', 'y4', 'y5'], 'qoute': 1}, 'x8': {'pref': ['y2', 'y6', 'y7', 'y1', 'y8', 'y3', 'y4', 'y5'], 'qoute': 1}}
yprofile = {'y1': {'pref': ['x4', 'x3', 'x8', 'x1', 'x2', 'x5', 'x7', 'x6'], 'qoute': 1}, 'y2': {'pref': ['x3', 'x7', 'x5', 'x8', 'x6', 'x4', 'x1', 'x2'], 'qoute': 1}, 'y3': {'pref': ['x7', 'x5', 'x8', 'x3', 'x6', 'x2', 'x1', 'x4'], 'qoute': 1}, 'y4': {'pref': ['x6', 'x4', 'x2', 'x7', 'x3', 'x1', 'x5', 'x8'], 'qoute': 1}, 'y5': {'pref': ['x8', 'x7', 'x1', 'x5', 'x6', 'x4', 'x3', 'x2'], 'qoute': 1}, 'y6': {'pref': ['x5', 'x4', 'x7', 'x6', 'x2', 'x8', 'x3', 'x1'], 'qoute': 1}, 'y7': {'pref': ['x1', 'x4', 'x5', 'x6', 'x2', 'x8', 'x3', 'x7'], 'qoute': 1}, 'y8': {'pref': ['x2', 'x5', 'x4', 'x3', 'x7', 'x8', 'x1', 'x6'], 'qoute': 1}}

t = gale_shep(xprofile, yprofile)
print(t[0])
print(t[1])
print(t[2])

# print(xprofile)
# print(yprofile)
