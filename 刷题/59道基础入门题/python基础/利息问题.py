"""
编写一个程序来计算单利和最终金额。

计算利息和最终金额的公式：

简单利息 = P * R * T * 0.01
最终金额 = P + 简单利息
这里，P是本金，R是利率，T是时间（年）。

通过输入浮点数分别获得："本金"、"利率 "和 "时间"。
使用公式计算单利，并将结果存储在interest变量中。
使用公式计算最终金额，并将其存储在total_sum变量中。
在不同的行中打印interest 和total_sum。
输入格式

三个浮点数

示例输入
7500
7.6
4
示例输出
2280.0
9780.0

"""

P = float(input())
R = float(input())
T = float(input())

interest = P * R * T * 0.01
total_sum = P + interest

print(interest)
print(total_sum)
