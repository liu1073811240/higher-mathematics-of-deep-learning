import math
import sympy

# limit x-->0: sin(x)/x = 1
print(math.sin(100) / 100)
print(math.sin(10) / 10)
print(math.sin(1) / 1)

print(math.sin(1e-1) / 1e-1)
print(math.sin(1e-3) / 1e-3)
print(math.sin(1e-5) / 1e-5)
print(math.sin(1e-7) / 1e-7)
print(math.sin(1e-9) / 1e-9)

# limit x--> ∞： （1+1/x）^x=e
print((1+1/1e1)**1e1)
print((1+1/1e5)**1e5)
print((1+1/1e10)**1e10)

# limit x-->0:(1+x)^(1/x)=e
print((1+1e-10)**(1/1e-10))

# 定义符号变量
x = sympy.symbols("x")
print(sympy.limit(1/x, x, 0))
print(sympy.limit(x/1, x, 0))




