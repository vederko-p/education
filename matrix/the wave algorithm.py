
from numpy import array


def border(m0):
    m = m0.copy()
    m_size = [len(m), len(m[0]) + 2]
    for i in range(m_size[0]):
        m[i].append(-1)
        m[i].insert(0, -1)
    m_size[0] = m_size[0] + 2
    b = [-1 for i in range(m_size[1])]
    m.append(b)
    m.insert(0, b)
    return m


def wave_alg(m0, p01, p02):
    # ---| start |---
    m = border(m0)
    p1 = [p01[0] + 1, p01[1] + 1]
    p2 = [p02[0] + 1, p02[1] + 1]
    m[p1[0]][p1[1]] = 1

    if m[p1[0]-1][p1[1]] == 0 or m[p1[0]+1][p1[1]] == 0 or m[p1[0]][p1[1]-1] == 0 or m[p1[0]][p1[1]+1] == 0:
        clear_way = [p1]
    else:
        return False

    # ---| wave |---
    t = 0
    while clear_way:
        current_clear_way = []

        for pnt in clear_way:

            if pnt == p2:
                t = 1
                break

            if m[pnt[0]-1][pnt[1]] == 0:
                pfcw = [pnt[0]-1, pnt[1]]
                m[pfcw[0]][pfcw[1]] = m[pnt[0]][pnt[1]] + 1
                if m[pfcw[0] - 1][pfcw[1]] == 0 or m[pfcw[0] + 1][pfcw[1]] == 0 or m[pfcw[0]][
                    pfcw[1] - 1] == 0 or m[pfcw[0]][pfcw[1] + 1] == 0:
                    current_clear_way.append(pfcw)

            if m[pnt[0]+1][pnt[1]] == 0:
                pfcw = [pnt[0]+1, pnt[1]]
                m[pfcw[0]][pfcw[1]] = m[pnt[0]][pnt[1]] + 1
                if m[pfcw[0] - 1][pfcw[1]] == 0 or m[pfcw[0] + 1][pfcw[1]] == 0 or m[pfcw[0]][
                    pfcw[1] - 1] == 0 or m[pfcw[0]][pfcw[1] + 1] == 0:
                    current_clear_way.append(pfcw)

            if m[pnt[0]][pnt[1]-1] == 0:
                pfcw = [pnt[0], pnt[1]-1]
                m[pfcw[0]][pfcw[1]] = m[pnt[0]][pnt[1]] + 1
                if m[pfcw[0] - 1][pfcw[1]] == 0 or m[pfcw[0] + 1][pfcw[1]] == 0 or m[pfcw[0]][
                    pfcw[1] - 1] == 0 or m[pfcw[0]][pfcw[1] + 1] == 0:
                    current_clear_way.append(pfcw)

            if m[pnt[0]][pnt[1]+1] == 0:
                pfcw = [pnt[0], pnt[1]+1]
                m[pfcw[0]][pfcw[1]] = m[pnt[0]][pnt[1]] + 1
                if m[pfcw[0] - 1][pfcw[1]] == 0 or m[pfcw[0] + 1][pfcw[1]] == 0 or m[pfcw[0]][
                    pfcw[1] - 1] == 0 or m[pfcw[0]][pfcw[1] + 1] == 0:
                    current_clear_way.append(pfcw)

        if t:
            clear_way = []
        else:
            clear_way = current_clear_way

    # ---| path |---
    if not (m[p2[0]-1][p2[1]] < 1 and m[p2[0]+1][p2[1]] < 1 and m[p2[0]][p2[1]-1] < 1 and m[p2[0]][p2[1]+1]):
        path = [[p2[0]-1, p2[1]-1]]
        cp = p2
        while cp != p1:
            value = []
            pnts = []
            if m[cp[0]-1][cp[1]] > 0:
                value.append(m[cp[0]-1][cp[1]])
                pnts.append([cp[0]-1, cp[1]])
            if m[cp[0]+1][cp[1]] > 0:
                value.append(m[cp[0]+1][cp[1]])
                pnts.append([cp[0]+1, cp[1]])
            if m[cp[0]][cp[1]-1] > 0:
                value.append(m[cp[0]][cp[1]-1])
                pnts.append([cp[0], cp[1]-1])
            if m[cp[0]][cp[1]+1] > 0:
                value.append(m[cp[0]][cp[1]+1])
                pnts.append([cp[0], cp[1]+1])

            cp = pnts[value.index(min(value))]
            path.insert(0, [cp[0]-1, cp[1]-1])
    else:
        return False

    # ---| visualization |---
    m_size = [len(m), len(m[0])]
    for i in range(m_size[0]):
        for j in range(m_size[1]):
            if m[i][j] == -1:
                m[i][j] = 7
            elif not [i, j] in path and m[i][j] > 0:
                m[i][j] = 0

    for i in path:
        m[i[0]+1][i[1]+1] = 1
    m0 = []
    for k in m[1:-1]:
        m0.append(k[1:-1])
    print(array(m0))

    return '\npath: {0}'.format(path)


in_m1 = [
    [0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, -1, 0],
    [0, 0, -1, -1, 0, 0],
    [0, 0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

in_m2 = [
    [0, 0, 0, -1, 0, 0, 0],
    [0, -1, 0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0, -1, 0]
]

in_m3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, -1, -1],
    [0, -1, 0, -1, 0, 0],
    [0, -1, 0, -1, 0, 0]
]

print('\n---| example 1|---')
print('исходная точка: {0}\nконечная точка: {1}'.format([1, 2], [5, 4]))
print(wave_alg(in_m1, [0, 2], [5, 4]))

# print('\n---| example 2|---\n')
# print(wave_alg(in_m2, [0, 0], [2, 6]))

print('\n---| example 2|---')
print('исходная точка: {0}\nконечная точка: {1}'.format([0, 0], [3, 5]))
print(array(in_m3))
print(wave_alg(in_m3, [3, 0], [3, 5]))
