"""
来源：Python-100-Days（骆昊）Day04
题目：判断闰年

要求：输入一个 1582 年以后的年份，判断该年份是不是闰年。
"""

"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')
