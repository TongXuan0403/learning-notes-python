"""
来源：Python-100-Days（骆昊）Day06
题目：最大公约数

要求：输入两个大于 0 的正整数，求两个数的最大公约数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数。
"""
"""
输入两个正整数求它们的最大公约数

Version: 1.0
Author: 骆昊
"""
x = int(input('x = '))
y = int(input('y = '))
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数: {i}')
        break
