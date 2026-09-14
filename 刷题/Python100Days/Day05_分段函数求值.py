"""
来源：Python-100-Days（骆昊）Day05
题目：分段函数求值

有如下所示的分段函数，要求输入`x`，计算出`y`：
- x > 1 时，y = 3x - 5
- -1 ≤ x ≤ 1 时，y = x + 2
- x < -1 时，y = 5x + 3
"""
"""
分段函数求值

Version: 1.0
Author: 骆昊
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')
