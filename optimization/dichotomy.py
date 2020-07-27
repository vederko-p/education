
import numpy as np
import matplotlib.pyplot as plt


def round_dot(a):
    return [round(a[0], 2), round(a[1], 2)]


def f(x):
    return x**4 - 20*x**3 + 7


def dichotomy(a, b, func, k, iter=None):
    if iter is None:
        iter = []

    x1 = (b + a - 0.1)/2
    x2 = (b + a + 0.1)/2

    if not k:
        iter.append(round_dot([(a + b) / 2, func((a + b) / 2)]))
        return iter
    elif func(x1) <= func(x2):
        iter.append(round_dot([x1, f(x1)]))
        return dichotomy(a, x2, func, k-1, iter)
    elif func(x1) > func(x2):
        iter.append(round_dot([x2, f(x2)]))
        return dichotomy(x1, b, func, k-1, iter)


def data_vis(a, b, f, k):
    data0x = []
    data0y = []
    t = a
    while t+5 < b:
        data0x.append(t)
        data0y.append(f(t))
        t += 0.2

    data = np.transpose(dichotomy(a, b, f, k))
    x = data[0]
    y = data[1]
    fig = plt.figure()
    ax0 = fig.add_subplot()
    ax0.scatter(data0x, data0y)
    ax0.scatter(x, y)
    plt.show()


def dot_vis(dots):
    for i in dots:
        print(i)


dot_vis(dichotomy(5, 25, f, 7))
data_vis(5, 25, f, 7)
