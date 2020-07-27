
import sympy as sp


def grad_spusk(func, start, step, n, eps):  # start is sp object: sp.Matrix; func is sp object: f by var'ed x0, x1
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])  # нахождение градиента, sympy матрица из ч.п.
    for i in range(n):
        new = start - step * grad.subs([(x0, start[0]), (x1, start[1])])  # subs задает значения аргументам функции
        if (new - start).norm() <= eps:
            return start.evalf(2)[0:2]  # вывод с округлением
        else:
            start = new
    return start.evalf(2)[0:2]  # вывод с округлением


x = sp.var('x:2')  # объявление символьных переменных
f = x0**2 + x0*x1 + x1**2  # объявление переменной f, которая автоматически станет символьной (состоит из сим-ых пер-ых)
s = sp.Matrix([1, 1])

print('---| example 1 |---')
print(grad_spusk(f, s, 0.1, 20, 0.00001))
print('\n---| example 2 |---')
print(grad_spusk(f, s, 0.1, 20, 0.01))

print('\n---| example 3 |---')
t = grad_spusk(f, s, 0.1, 1000, 10**-100)
print('ответ без округления: {0}'.format(t))
u = sp.Matrix(t).evalf(chop=True)  # evalf(chop=True) очень маленькие значения обращает в 0
print('ответ с sympy округлением: {0}'.format(u[0:2]))
