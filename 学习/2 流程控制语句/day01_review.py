### 1. 知识速整（1.5–2h，边写边敲）
import random

# 用**注释写一句话笔记 + 下面跟 3–5 行可运行代码**，覆盖：

# 1. 变量：创建、命名规则、常量约定

#变量创建：变量名 = 变量值  每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# var = 2     #单个变量创建
# a, b, c = 1, 2, 3       #一次创建多个变量
#
# # 命名规则：开头不能以数字开头，不与关键字重名。可以按大小写字母，下划线开头。常见有大小驼峰命名，蛇形命名
# NameId = 10     #大驼峰命名
# lowerCamelCase = 10      #小驼峰命名
# name_id = 10        #蛇形命名
#
# # 常量  一般约定使用全大写变量名来表示常量。
# PI = 3.14159


# 2. 数据类型：int/float/bool/str 与类型互转
# 数据类型转换
    #隐式转换
# num1 = 1     #默认为int型
# num2 = 2
# print(num2/num1)        #调整为float型

    #显示转换   通过函数强行转换
# int1 = 123
# str1 = "467"
# float1 = 2.54
# bool1 = True     #0表示False 1 表示Ture

# print(int(str1),type(str1))
# print(str(float1),type(float1))
# print(float(int1),type(int1))
# print(bool(int1),type(bool1))


# 3. 进制：`bin()/oct()/hex()` 及互转
# 进制表示。二进制0b  八进制0o  十进制 正常数字  十六进制0x
# bin(x)	将一个整数转换为一个二进制字符串
# oct(x)	将一个整数转换为一个八进制字符串
# hex(x)	将一个整数转换为一个十六进制字符串
# ord(x)	将一个字符转换为它的ASCII整数值
# chr(x)	将一个整数转换为一个Unicode字符
# dec = 10
# b_num = 0b101001
# o_num = 0o15
# x_num = 0xD
#
# print(bin(o_num))
# print(oct(x_num))
# print(hex(b_num))


# 4. 输入输出：`input()`、`print` 的 `sep/end`、f-string
# 输入input()
# put1 = input()         #默认字符串
# put2 = int(input())     #控制输入的类型

# 输出print(" ", end="")
# print("adfcv", end=" ")     #默认会以 end="\n"为结尾，不显示


# 格式化字符串
# %占位
# print("十进制数: %d,浮点数: %f,字符串: %s,八进制数: %o,十六进制: %x" % (int1,float1,str1,o_num,x_num))
#
# # format
# print("十进制数: {},浮点数: {},字符串: {}" .format(int1,float1,str1))#按顺序
#
# print("十进制数: {2},浮点数: {1},字符串: {0}" .format(int1,float1,str1))#下标指定位置
#
# print("十进制数: {c},浮点数: {a},字符串: {b}" .format(a=int1,b=float1,c=str1))#设置参数
#
# #f-string
# print(f"十进制数: {int1},浮点数: {float1},字符串: {str1}")

# 5. 运算符：算术 / 比较 / 逻辑 / 成员 `in`/ 身份 `is`、短路求值

# 算数运算符
# +	加
# -	减、或取负
# *	乘
# /	除
# //	整除，除后向下取整
# %	模，返回除法的余数
# **	幂

# 比较运算符
# ==	相等，比较两者的值
# !=	不相等
# >	大于
# <	小于
# >=	大于等于
# <=	小于等于

# 逻辑运算符
# and	与，x and y，若x为False返回x的值，否则返回y的值
# or	或，x or y，若x为True返回x的值，否则返回y的值
# not	非，not x，若x为True返回False，若x为False返回True

# 成员运算符
#in
# a in ["a","b","c"]
#not in
# a not in ["a","b","c"]

# 身份运算符     is和==的区别，地址的不同
#is 比较两个对象的内存地址是不是同一个
#== 比较两个对象的值（内容）是否相等
#is
#not is
# a = [1,2,3]
# b = a
#
# print(b is a)  # True
# print(b == a)  # True
#
# b = a[:] #浅拷贝
# print(b)
# print(b is a)  # False
# print(b == a)  # True

# 6. 分支：if-elif-else、嵌套、match-case、三目运算符
#单分支if
# if 表达式:
#     语句

# a, b = 1, 2
# if a<b:
#     print(a)

#双分支if-else
# if 表达式:
#     语句
# else:
#     语句

# if a>b:
#     print(a)
# else:
#     print(b)

# if-elif-else
# if 表达式1:
#     语句1
# elif 表达式2:
#     语句2
# elif 表达式3:
#     语句3
# else:  # else如不需要可以省略
#     语句4

# print("age:",age := random.randint(1,100))      #  :=  海象运算符 赋值并返回值
# if age<2:
#     print("2")
# elif age<5:
#     print("5")
# elif age<20:
#     print("20")
# elif age<40:
#     print("40")
# else:
#     print("69")

# 嵌套
# if 表达式1:
#     if 表达式2:
#         语句1
#     else:
#         语句2
# else:
#     if 表达式3:
#         语句3
#     else:
#         语句4

# num = 0b011
# if num & 0b100 == 0b100:
#     print("100")
# else:
#     if num & 0b010 == 0b010:
#         if num & 0b001 == 0b001:
#             print("011")
#         else:
#             print("010")
#     else:
#         print("001")

# match-case
# match x:
#     case a:
#         语句1
#     case b:
#         语句2
#     case _:
#         语句3

# match month := (random.randint(1, 12)):
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(31)
#     case  4 | 6 | 9 | 11:
#         print(30)
#     case _:
#         print(28)


# 三目运算符
# 表达式1 if 判断条件 else 表达式2
# num1 = random.randint(1, 10)
# num2 = 5
#
# print(num1 if num1 > num2 else num2)

# 7. 循环：for/range、while、break/continue/pass、循环 else

#for 知道循环次数
# for 循环可以用来遍历可迭代对象，如列表或字符串。

# for 临时变量 in 可迭代对象:
#     语句


# for 循环后也可以加上 else，循环结束后会执行 else 中语句。

# for 临时变量 in 可迭代对象:
#     语句1
# else:
#     语句2

# list1 = [2, 3, 5, 7, 11, 13, 17, 19]
# for i in list1:
#     print(i)

#range(start,stop,step)  生成数列，它返回一个可迭代对象



#while 不知道循环次数
"""
第1周有2只兔子，此后每周兔子的数量都增加上周数量的2倍，
且期间没有兔子死亡，求第10周共有多少只兔子：
"""
# rabbit = 2
# week = 1
# while week <= 10:
#     rabbit *= rabbit
#     week += 1
# print(rabbit)

# while-else
# 当 while 表达式结果为 False 时会执行 else 中的语句。
# else一般和 break一起使用，循环通过break终止后，else中的代码不会执行


# break 直接跳出整个循环，结束整个循环
# for i in range(10):
#     if i == 6:
#         break
#     print(i)


# continue 只是跳出当前这个循环，下轮循环继续
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)


#pass 跳过，占位用


# 嵌套循环
# 使用嵌套循环打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end='\t')
#     print()  #起到换行的作用，不然会连在一起输出


# 2. 分层题目（4–5h）

# **基础（必做）**

# 1. 补做 Q1：打印 `float("3.14")` 的类型和值；42 转二进制；再试 `int("ff",16)`、`ord('A')`、`chr(97)`
# float1= 3.14
# num = 42
# print(float1,type(float1))
# print(bin(num))
# print(int("ff",16))
# print(ord('A'))
# print(chr(ord('A')))
# print(chr(97))

# 函数	转换方向	例子	结果
# int(s, base)	某进制字符串 → 十进制整数	int("ff",16)	255
# hex(n) / bin(n) / oct(n)	十进制整数 → 进制字符串	hex(255)	'0xff'
# ord(c)	字符 → 编号	ord('A')	65
# chr(n)	编号 → 字符	chr(97)	'a'



# 2. 输入圆半径，输出周长和面积，保留 2 位小数(:.2f)
# r = eval(input())
# s = 3.14 * r**2
# l = 2 * 3.14 * r
# print(f"s:{s:.2f},l:{l:.2f}")


# 4. 嵌套循环打印九九乘法表
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()


# 5. while 写猜数字：随机 1~100，提示 "大了 / 小了"，猜对时输出一共猜了多少次
# num = random.randint(1, 100)
# sum = 1
# while True:
#
#    i = int(input())
#    if i == num :
#        print(sum)
#        break
#    elif i > num :
#        print("大了")
#        sum += 1
#    elif i < num :
#        print("小了")
#        sum +=1



# **进阶（选做，尽量写）**

# 6. 打印所有三位水仙花数（各位数字立方和等于自身） abc = a**3 + b**3 + c**3    `%10` 取末位，`//10` 砍末位
# for i in range(100,1000):
#     a = i % 10  #保留个位数
#     b = i // 100  #保留第一位数
#     c = i % 100 // 10  #先保留后面两位，再保留第一位
#     if a**3 + b**3 + c**3 == i:
#         print(i)


# 7. 百钱百鸡：公鸡 5 元、母鸡 3 元、3 只小鸡 1 元，100 元买 100 只，输出所有买法
# 公鸡最多20只，母鸡最多33只
# for x in range(0,21):
#     for y in range(0,34):
#         z = 100 - x - y
#         if z>=0 and z % 3 ==0 and 5*x+3*y+z*(1/3) == 100:
#             print(f"{x},{y},{z}")



# 8. 输入一行字符，统计字母、数字、空格、其他字符各多少个  遍历+分类+计数
# letter number space other
# 分类用  字母isalpha()  数字isdigit()  空白isspace()
# letter = number = space = other = 0
#
# str1 = input()
# for s in str1:
#     if s.isalpha():
#         letter += 1
#     elif s.isdigit():
#         number += 1
#     elif s.isspace():
#         space += 1
#     else:
#         other += 1
# print(letter, number, space, other)















