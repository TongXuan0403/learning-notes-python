"""
来源：Python-100-Days（骆昊）Day04
题目：计算圆的周长和面积

要求：输入一个圆的半径（r），计算出它的周长（ 2 π r ）和面积（ π r² ）。
"""
"""
输入半径计算圆的周长和面积

Version: 1.0
Author: 骆昊
"""
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
