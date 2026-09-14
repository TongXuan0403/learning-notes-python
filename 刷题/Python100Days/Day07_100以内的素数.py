"""
来源：Python-100-Days（骆昊）Day07
题目：100以内的素数

说明：素数指的是只能被 1 和自身整除的正整数（不包括 1），之前我们写过判断素数的代码，这里相当于是一个升级版本。
"""

"""
输出100以内的素数

Version: 1.0
Author: 骆昊
"""
for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
