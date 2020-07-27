
def get_y(distrib, y):
    for i in distrib:
        if distrib[i] == y:
            return i


def all_stab(xprfl, d):
    xprofile = xprfl.copy()
    r = 1
    stab = [d]
    while r:
        wasnt = [i for i in d]  # список x, которые не участвовали в обходе
        new_d = {}
        while wasnt:
            # print('wasnt: ', wasnt)  # delete it
            x = wasnt[0]
            xpref = xprofile[x]['pref']
            # print('x: ', x)  # delete it
            # print('xpref: ', xpref)  # delete it
            if len(xpref) > 1:  # если в предпочтениях x есть иные варианты, кроме текущего
                cycle = [[x, xpref[1]]]
                xn = get_y(stab[-1], xpref[1])  # следующий в цикле x
                while xn != x:  # пока следующий не равен первому (т.е. пока нет цикла)
                    # print('xprofile', xprofile)  # delete it
                    # print('xn', xn)  # delete it
                    xnpref = xprofile[xn]['pref']
                    # print('xn: ', xn)  # delete it
                    # print('xnpref: ', xnpref)  # delete it
                    if len(xnpref) > 1:  # если в предпочтения каждого следующег есть иные варианты, кроме их текущего
                        cycle.append([xn, xnpref[1]])  # тогда добовляем в цикл
                    else:
                        break  # иначе ломаем while и не переходим в else ниже
                    xn = get_y(stab[-1], xnpref[1])  # переходим к следующему x
                else:  # если while завершился не через break, то значит, цикл есть и в этот else попадаем
                    # print('cycle: ', cycle)  # delete it
                    for i in cycle:
                        new_d[i[0]] = i[1]  # фиксируем новое распределние при данном цикле
                # сюда попадаем в любм случае и удаляем из wasnt все пройденные x
                fc = [x[0] for x in cycle]
                # print('fc: ', fc)  # delete it
                for i in fc:
                    wasnt.remove(i)
                    # print('wasnt after del: ', wasnt)  # delete it
            else:  # если в предпочтениях x нет иных вариантов, кроме текущего, то цикла точно нет
                # убираем x из непроверенных
                wasnt = wasnt[1:]
            # print('------------')  # delete it
        # если new_d пустое, то нового распределения нет, значит, нашли все
        if not new_d:
            r = 0  # reason to seek for more stab
        else:  # если new_d не пустое, то нашли новое распределение и имеет смысл искать дальше
            stab.append(new_d)
        # в таком случае необходимо изменить предпочтения всех x ввиду нового распределения
        # print('new_d: ', new_d)  # delete it
        for i in new_d:
            xprofile[i]['pref'].pop(0)
        r -= 1
    print(stab)


xprofile = {'x1': {'pref': ['y3', 'y1', 'y5', 'y7', 'y4'], 'qoute': 1}, 'x2': {'pref': ['y1', 'y3', 'y4', 'y8', 'y7'], 'qoute': 1}, 'x3': {'pref': ['y7', 'y4', 'y3', 'y1', 'y2', 'y8'], 'qoute': 1}, 'x4': {'pref': ['y5', 'y8', 'y6', 'y1', 'y4', 'y7'], 'qoute': 1}, 'x5': {'pref': ['y4', 'y2', 'y8', 'y7', 'y3', 'y6', 'y5'], 'qoute': 1}, 'x6': {'pref': ['y6', 'y5', 'y7', 'y4', 'y3'], 'qoute': 1}, 'x7': {'pref': ['y8', 'y6', 'y2', 'y3', 'y4', 'y5'], 'qoute': 1}, 'x8': {'pref': ['y2', 'y7', 'y1', 'y3', 'y5'], 'qoute': 1}}
yprofile = {'y1': {'pref': ['x4', 'x3', 'x8', 'x1', 'x2'], 'qoute': 1}, 'y2': {'pref': ['x3', 'x7', 'x5', 'x8'], 'qoute': 1}, 'y3': {'pref': ['x7', 'x5', 'x8', 'x3', 'x6', 'x2', 'x1'], 'qoute': 1}, 'y4': {'pref': ['x6', 'x4', 'x2', 'x7', 'x3', 'x1', 'x5'], 'qoute': 1}, 'y5': {'pref': ['x8', 'x7', 'x1', 'x5', 'x6', 'x4'], 'qoute': 1}, 'y6': {'pref': ['x5', 'x4', 'x7', 'x6'], 'qoute': 1}, 'y7': {'pref': ['x1', 'x4', 'x5', 'x6', 'x2', 'x8', 'x3'], 'qoute': 1}, 'y8': {'pref': ['x2', 'x5', 'x4', 'x3', 'x7'], 'qoute': 1}}
d = {'x8': 'y2', 'x1': 'y3', 'x5': 'y4', 'x4': 'y5', 'x6': 'y6', 'x3': 'y7', 'x2': 'y1', 'x7': 'y8'}

all_stab(xprofile, d)
