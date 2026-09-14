"""
来源：Python-100-Days（骆昊）
示例：递归调用——阶乘、斐波那契数列（递归版/迭代版），并用 lru_cache 加速递归。
"""
# ---- 代码块8 ----
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

# ---- 代码块10 ----
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 21):
    print(fib1(i))

# ---- 代码块11 ----
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# ---- 代码块12 ----
from functools import lru_cache


@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))
