
import sympy as sp
from time import strftime


def dichotomy(a, b, func, k):
    x1 = (b + a - 0.1)/2
    x2 = (b + a + 0.1)/2

    if not k:
        return (a + b) / 2
    elif func.subs(et, x1) <= func.subs(et, x2):
        return dichotomy(a, x2, func, k-1)
    elif func.subs(et, x1) > func.subs(et, x2):
        return dichotomy(x1, b, func, k-1)


def grad_spusk(func, start, step, n, eps):
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])
    for i in range(n):
        new = start - step * grad.subs([(x0, start[0]), (x1, start[1])])
        if (new - start).norm() < eps:
            return [start[0:2], i]
        else:
            start = new
    return [start[0:2], n]


def steepest_descent(func, start, step, n, eps):
    sp.var('et')
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])
    for i in range(n):
        new = start - step * grad.subs([(x0, start[0]), (x1, start[1])])
        if (new - start).norm() <= eps:
            return [start[0:2], i]
        else:
            start = new
            # find out best step
            per = start - et * grad.subs([(x0, start[0]), (x1, start[1])])
            fet = func.subs([(x0, per[0]), (x1, per[1])])
            step = dichotomy(0, 1, fet, 10)
    return [start[0:2], n]


def pulse_method(func, start, step, gamma, n, eps):
    v = sp.Matrix([0, 0])
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])
    for i in range(n):
        v = gamma * v + step * grad.subs([(x0, start[0]), (x1, start[1])])
        new = start - v
        if (new - start).norm() < eps:
            return [start[0:2], i]
        else:
            start = new
    return [start[0:2], n]


def nesterovs_method(func, start, step, gamma, n, eps):
    v = sp.Matrix([0, 0])
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])
    for i in range(n):
        new = start - gamma * v
        v = gamma * v + step * grad.subs([(x0, new[0]), (x1, new[1])])
        new = start - v
        if (new - start).norm() < eps:
            return [start[0:2], i]
        else:
            start = new
    return [start[0:2], n]


x = sp.var('x:2')
f = (1.5 - x0 + x0*x1)**2 + (2.25 - x0 + x0*(x1)**2)**2 + (2.625 - x0 + x0*(x1)**3)**2
strt = sp.Matrix([0.7, 1.4])
stp = 0.01
n = 10**3
eps = 10**(-7)
gamma = 0.9

print('---| градиентный спуск |---')
t0 = 60 * int(strftime('%M')) + int(strftime('%S'))
print(grad_spusk(f, strt, stp, n, eps))
t1 = 60 * int(strftime('%M')) + int(strftime('%S'))
print('абсолютное время выполнения, сек: {0}'.format(t1 - t0))

print('\n---| наискорейший спуск |---')
t0 = 60 * int(strftime('%M')) + int(strftime('%S'))
print(steepest_descent(f, strt, stp, n, eps))
t1 = 60 * int(strftime('%M')) + int(strftime('%S'))
print('абсолютное время выполнения, сек: {0}'.format(t1 - t0))

print('\n---| метод импульсов |---')
t0 = 60 * int(strftime('%M')) + int(strftime('%S'))
print(pulse_method(f, strt, stp, gamma, n, eps))
t1 = 60 * int(strftime('%M')) + int(strftime('%S'))
print('абсолютное время выполнения, сек: {0}'.format(t1 - t0))

print('\n---| метод Нестерова |---')
t0 = 60 * int(strftime('%M')) + int(strftime('%S'))
print(nesterovs_method(f, strt, stp, gamma, n, eps))
t1 = 60 * int(strftime('%M')) + int(strftime('%S'))
print('абсолютное время выполнения, сек: {0}'.format(t1 - t0))
