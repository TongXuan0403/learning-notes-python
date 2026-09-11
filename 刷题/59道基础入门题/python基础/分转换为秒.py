"""
编写一个程序，将分转换为秒。

从输入获取一个整数，赋值给变量time_minutes。
通过与60相乘将time_minutes转换为秒。(1分钟=60秒)。
以秒为单位打印结果。
输入格式

一个整数

示例输入
2
示例输出
120

"""

time_minutes = int(input())
print(time_minutes*60)