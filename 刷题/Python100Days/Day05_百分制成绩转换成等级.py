"""
来源：Python-100-Days（骆昊）Day05
题目：百分制成绩转换成等级

要求：如果输入的成绩在90分以上（含90分），则输出`A`；输入的成绩在80分到90分之间（不含90分），则输出`B`；输入的成绩在70分到80分之间（不含80分），则输出`C`；输入的成绩在60分到70分之间（不含70分），则输出`D`；输入的成绩在60分以下，则输出`E`。
"""

"""
百分制成绩转换为等级制成绩

Version: 1.0
Author: 骆昊
"""
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }')
