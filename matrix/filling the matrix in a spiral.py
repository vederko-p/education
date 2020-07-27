
from numpy import array


def spiral(n):
    m = [[0 for a in range(n)] for b in range(n)]
    k = n
    i, j = 0, 0
    y = 1
    while k != 0:
        # направо
        for t in range(k):
            m[i][j] = y
            j += 1
            y += 1
        j -= 1
        i += 1
        if k-1 == 0:
            break
        # вниз
        for t in range(k-1):
            m[i][j] = y
            i += 1
            y += 1
        i -= 1
        j -= 1
        # налево
        for t in range(k-1):
            m[i][j] = y
            j -= 1
            y += 1
        i -= 1
        j += 1
        # вверх
        for t in range(k-2):
            m[i][j] = y
            i -= 1
            y += 1
        i += 1
        j += 1
        k -= 2
    return m


print('---| example 1, n = 0 |---')
print(array(spiral(0)))

print('\n---| example 2, n = 1 |---')
print(array(spiral(1)))

print('\n---| example 3, n = 5 |---')
print(array(spiral(5)))

print('\n---| example 4, n = 6 |---')
print(array(spiral(6)))
