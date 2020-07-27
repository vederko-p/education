
from numpy import array


def bubble_sort(lst0):
    lst = lst0.copy()
    n = len(lst)
    k = 0
    while k != n-1:
        for i in range(n-k-1):
            t = lst[i]
            if t > lst[i+1]:
                lst[i] = lst[i+1]
                lst[i+1] = t
        k += 1
    return lst


def l_sq(m):
    s = len(m)
    for i in m:
        if bubble_sort(i) != list(range(1, s+1)):
            return False
    for i in [[m[k][j] for k in range(s)] for j in range(s)]:
        if bubble_sort(i) != list(range(1, s+1)):
            return False
    return True


print('---| example 1|---')
m1 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
print(array(m1))
print(l_sq(m1))

print('\n---| example 2|---')
m2 = [[1, 2, 3], [2, 1, 2], [2, 3, 1]]
print(array(m2))
print(l_sq(m2))

print('\n---| example 3|---')
m2 = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
print(array(m2))
print(l_sq(m2))
