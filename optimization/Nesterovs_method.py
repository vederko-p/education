
import sympy as sp


def nesterovs_method(func, start, step, gamma, n, eps):
    v = sp.Matrix([0, 0])
    grad = sp.Matrix([sp.diff(func, x0), sp.diff(func, x1)])
    for i in range(n):
        new = start - gamma * v
        v = gamma * v + step * grad.subs([(x0, new[0]), (x1, new[1])])
        new = start - v
        if (new - start).norm() < eps:
            return start.evalf(2)[0:2]
        else:
            start = new
    return start.evalf(2)[0:2]


x = sp.var('x:2')
f = (1.5 - x0 + x0*x1)**2 + (2.25 - x0 + x0*(x1)**2)**2 + (2.625 - x0 + x0*(x1)**3)**2
strt = sp.Matrix([0.7, 1.4])
stp = 0.01

print('---| example 1 |---')
print(nesterovs_method(f, strt, stp, 0.9, 452, 10**(-7)))
