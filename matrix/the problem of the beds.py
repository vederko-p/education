
import numpy as np


def border(m0):
    m = m0.copy()
    m_size = [len(m), len(m[0]) + 2]
    for i in range(m_size[0]):
        m[i].append(0)
        m[i].insert(0, 0)
    m_size[0] = m_size[0] + 2
    b = [0 for i in range(m_size[1])]
    m.append(b)
    m.insert(0, b)
    return m


def beds_count(m0):
    m = border(m0)
    m_size = [len(m), len(m[0])]

    bc = 0

    for i in range(1, m_size[0]-1):
        for j in range(1, m_size[1]-1):
            if m[i][j] == 0:
                continue
            else:
                bc += 1
                m[i][j] = 0
                if m[i - 1][j] == 1 or m[i + 1][j] == 1 or m[i][j - 1] == 1 or m[i][j + 1] == 1:
                    clear_way = [[i, j]]
                else:
                    continue

                while clear_way:
                    current_clear_way = []
                    for pnt in clear_way:

                        if m[pnt[0]-1][pnt[1]] == 1:
                            pfcw = [pnt[0] - 1, pnt[1]]
                            m[pfcw[0], pfcw[1]] = 0
                            if m[pfcw[0] - 1][pfcw[1]] == 1 or m[pfcw[0] + 1][pfcw[1]] == 1 or m[pfcw[0]][
                                pfcw[1] - 1] == 1 or m[pfcw[0]][pfcw[1] + 1] == 1:
                                current_clear_way.append(pfcw)

                        if m[pnt[0]+1][pnt[1]] == 1:
                            pfcw = [pnt[0] + 1, pnt[1]]
                            m[pfcw[0]][pfcw[1]] = 0
                            if m[pfcw[0] - 1][pfcw[1]] == 1 or m[pfcw[0] + 1][pfcw[1]] == 1 or m[pfcw[0]][
                                pfcw[1] - 1] == 1 or m[pfcw[0]][pfcw[1] + 1] == 1:
                                current_clear_way.append(pfcw)

                        if m[pnt[0]][pnt[1]-1] == 1:
                            pfcw = [pnt[0], pnt[1]-1]
                            m[pfcw[0]][pfcw[1]] = 0
                            if m[pfcw[0] - 1][pfcw[1]] == 1 or m[pfcw[0] + 1][pfcw[1]] == 1 or m[pfcw[0]][
                                pfcw[1] - 1] == 1 or m[pfcw[0]][pfcw[1] + 1] == 1:
                                current_clear_way.append(pfcw)

                        if m[pnt[0]][pnt[1]+1] == 1:
                            pfcw = [pnt[0], pnt[1]+1]
                            m[pfcw[0]][pfcw[1]] = 0
                            if m[pfcw[0] - 1][pfcw[1]] == 1 or m[pfcw[0] + 1][pfcw[1]] == 1 or m[pfcw[0]][
                                pfcw[1] - 1] == 1 or m[pfcw[0]][pfcw[1] + 1] == 1:
                                current_clear_way.append(pfcw)

                        clear_way = current_clear_way

    return bc


t1 = [
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0]
]

t2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

t3 = [
    [0, 0, 0],
    [0, 0, 0]
]

t4 = [
    [1, 1],
    [1, 1],
    [1, 1],
]

print('---| example 1 |---')
print(np.array(t1))
print('число грядок: {0}'.format(beds_count(t1)))

print('\n---| example 2 |---')
print(np.array(t2))
print('число грядок: {0}'.format(beds_count(t2)))

print('\n---| example 3 |---')
print(np.array(t3))
print('число грядок: {0}'.format(beds_count(t3)))

print('\n---| example 4 |---')
print(np.array(t4))
print('число грядок: {0}'.format(beds_count(t4)))
