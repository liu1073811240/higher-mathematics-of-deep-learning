from sympy import *

x = symbols("x")
print(diff(x**4, x, 1))
print(diff(x**4, x, 2))
print(diff(x**4, x, 3))
print(diff(x**4, x, 4))
print(diff(x**4, x, 5))

x, y, z = symbols("x y z")
exp_num = exp(x*y*z)
print(diff(exp_num, x))
print(diff(exp_num, y))
print(diff(exp_num, z))
print(diff(exp_num, x, 2))

# 积分：定积分，不定积分
print(diff(x**6), x)  # 6*x**5
print(integrate(6*x**5))
print(diff(sin(x), x))
print(integrate(cos(x)))

print(integrate(sin(x), (x, 0, pi/2)))



