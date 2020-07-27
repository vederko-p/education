
import random


# полные предопчтения
def gen(xn, yn):
    x = ['x' + str(i) for i in range(1, xn + 1)]
    y = ['y' + str(i) for i in range(1, yn + 1)]

    xprofile = dict()
    for i in range(len(x)):
        xprofile[x[i]] = dict(pref=random.sample(y, len(y)), qoute=1)

    yprofile = dict()
    for i in range(len(x)):
        yprofile[y[i]] = dict(pref=random.sample(x, len(x)), qoute=1)

    return xprofile, yprofile


def distribution(n):
    x = random.sample(['x' + str(i) for i in range(1, n + 1)], n)
    y = random.sample(['y' + str(i) for i in range(1, n + 1)], n)
    return {x[i]: y[i] for i in range(n)}


def get_y(distrib, y):
    for i in distrib:
        if distrib[i] == y:
            return i


def block_pairs(xprofile, yprofile, distrib):
    pairs = []
    for i in xprofile:
        for j in yprofile:
            # mxi
            s = [distrib[i], j]
            rangs = [xprofile[i]['pref'].index(h) for h in s]
            chx = xprofile[i]['pref'][min(rangs)]
            # myi
            s = [get_y(distrib, j), i]
            rangs = [yprofile[j]['pref'].index(h) for h in s]
            chy = yprofile[j]['pref'][min(rangs)]
            if chx != distrib[i] and chy != get_y(distrib, j):
                pairs.append([i, j])
    if pairs:
        return False, pairs
    else:
        return True, []


# xprofile, yprofile = gen(3, 3)
# d = distribution(3)

# print(xprofile)
# print(yprofile)
# print(d)

# т.к. предпчтения полные, то для проверки стабильности будет достаточно проверки на отсутствие блокирующих пар
# print(block_pairs(xprofile, yprofile, d))

# алгоритм локального поиска
def local_search(xprofile, yprofile, distrib):
    bp = block_pairs(xprofile, yprofile, distrib)[1]
    while bp:
        t = bp[0]
        distrib[get_y(distrib, t[1])] = distrib[t[0]]
        distrib[t[0]] = t[1]
        bp = block_pairs(xprofile, yprofile, distrib)[1]
    return xprofile, yprofile, distrib


# xprofile, yprofile = gen(8, 8)
# d = distribution(8)
#
# print('\nначальные xprofile, yprofile и распределение')
# print(xprofile)
# print(yprofile)
# print(d)
#
#
# u = local_search(xprofile, yprofile, d)
# print('\nрезультирующие xprofile, yprofile и распределение')
# print(u[0])
# print(u[1])
# print(u[2])
# print('\nпроверка на стабильность (отсутствие блокирующих пар)')
# print(block_pairs(u[0], u[1], u[2]))
#
# print('\n---| проверка на конкретном примере |---')
# txprofile = {'x1': {'pref': ['y2', 'y3', 'y1'], 'qoute': 1}, 'x2': {'pref': ['y3', 'y1', 'y2'], 'qoute': 1}, 'x3': {'pref': ['y3', 'y2', 'y1'], 'qoute': 1}}
# typrofile = {'y1': {'pref': ['x3', 'x1', 'x2'], 'qoute': 1}, 'y2': {'pref': ['x2', 'x3', 'x1'], 'qoute': 1}, 'y3': {'pref': ['x1', 'x2', 'x3'], 'qoute': 1}}
# td = {'x1': 'y1', 'x3': 'y3', 'x2': 'y2'}
# print(block_pairs(txprofile, typrofile, td))

# xprofile, yprofile = gen(3, 3)
# d = distribution(3)
# print('\nxprofile: ', xprofile)
# print('yprofile: ', yprofile)
# print('distribution: ', d)
