from sympy import *
import sympy

# x = sympy.symbols("x")
x = symbols("x")
expr = cos(x) + 1
print(expr)  # 公式
print(expr.subs(x, 0))  # 求值

# 求解方程

a, b, c = symbols("a b c")
x, y, z = symbols("x y z")
print(a*x**3+b*y**2+c*z)
print(solve(a*x**3+b*y**2+c*z))

print(a*x**2 + b*x + c)
print(solve(a*x**2 + b*x + c, x))

exps = x**3 + 4**y - z
print(exps.subs([(x, 2), (y, 4), (z, 0)]))

