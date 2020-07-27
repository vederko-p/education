
import numpy as np
import matplotlib.pyplot as plt


def round_dot(a):
    return [round(a[0], 2), round(a[1], 2)]


def f(x):
    return x**4 - 20*x**3 + 7


def bine(n):
    t = (1 + 5**0.5)/2
    return int((t**n - (-t)**(-n)) / (2*t - 1))


def fibonacci_method(a, b, func, k):
    x1 = a + (b - a) * (bine(k-2) / bine(k))
    x2 = a + (b - a) * (bine(k-1) / bine(k))
    y1 = func(x1)
    y2 = func(x2)

    iter =[]

    while k-1:
        k -= 1
        if y1 > y2:
            iter.append([x2, y2])
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            y1 = y2
            y2 = f(x2)
        else:
            iter.append([x1, y1])
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            y2 = y1
            y1 = func(x1)

    iter.append([(x1+x2)/2, func((x1+x2)/2)])
    iter = list(map(round_dot, iter))
    return iter


def data_vis(a, b, f, k):
    data0x = []
    data0y = []
    t = a
    while t+5 < b:
        data0x.append(t)
        data0y.append(f(t))
        t += 0.2

    data = np.transpose(fibonacci_method(a, b, f, k))
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


dot_vis(fibonacci_method(5, 25, f, 10))
data_vis(5, 25, f, 10)
