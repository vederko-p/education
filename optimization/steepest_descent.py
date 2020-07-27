
import sympy as sp


def dichotomy(a, b, func, k):  # func is sp object: f by var'ed et
    x1 = (b + a - 0.1)/2
    x2 = (b + a + 0.1)/2

    if not k:
        return (a + b) / 2
    elif func.subs(et, x1) <= func.subs(et, x2):
        return dichotomy(a, x2, func, k-1)
    elif func.subs(et, x1) > func.subs(et, x2):
        return dichotomy(x1, b, func, k-1)


def steepest_descent(func, start, step, n, eps):  # start is sp object: sp.Matrix; func is sp object: f by var'ed x0, x1
    sp.var('et')  # переменная для поиска оптимальнго шага
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])  # нахождение градиента, sympy матрица из ч.п.
    for i in range(n):
        new = start - step * grad.subs([(x0, start[0]), (x1, start[1])])  # subs задает значения аргументам функции
        if (new - start).norm() <= eps:
            return start.evalf(2)[0:2]  # вывод с округлением
        else:
            start = new
            # find out best step
            per = start - et * grad.subs([(x0, start[0]), (x1, start[1])])  # переменная (2-х мерный вектор)
            fet = func.subs([(x0, per[0]), (x1, per[1])])  # значение ф-и от переменной
            step = dichotomy(0, 1, fet, 10)  # результат одномерной оптимизации
    return start.evalf(2)[0:2]  # вывод с округлением


x = sp.var('x:2')  # объявление символьных переменных
f = x0**2 + x0*x1 + x1**2  # объявление переменной f, которая автоматически станет символьной (состоит из сим-ых пер-ых)
s = sp.Matrix([1, 1])

print('\n---| example 1 |---')
t1 = sp.Matrix([steepest_descent(f, s, 0.1, 3, 10**(-4))])
print(t1[0:2])

print('\n---| example 2 |---')
t2 = sp.Matrix([steepest_descent(f, s, 0.1, 100, 10**(-100))])
print('ответ без округления: {0}'.format(t2[0:2]))
print('ответ с sympy округлением: {0}'.format(t2.evalf(chop=True)[0:2]))
