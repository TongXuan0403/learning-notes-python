# 知识梳理

# 函数的组成
# def 函数名(参数):
#   函数体
#   return 返回值

# 参数
#   形参
#       创建函数指定的参数
#   实参
#       调用函数，给函数传递的参数

# 参数的传递
#   不可变类型   地址变化
#   可变类型    地址不变，值发生变化

# 参数传递形式
#   位置参数
"""
def func(a, b):
func(1,2)
"""
import time
from functools import reduce

#   默认值参数
"""
def func(a=1, b=2):
"""
#   关键字参数
"""
def func(a, b):
func(b=12,a=1)  #指定名称传参
"""
#   不定长参数
# 形式一   封装元组
"""
def func(*args)  或者   def func(a,*args) 
第二种要用到关键字传参
"""
# 形式二   封装字典
"""
def func(**kwargs)
"名字 = 值"这样传
"""

# 解包传参
"""
def func(a,b,c):
#传递形式
func(1,2,3)     位置传参
func(a=1,b=2,c=3)       关键字传参

tup=(1,2,3)
func(*tup)      #解包，把tup解开，然后分别传给a,b,c

dic={"a":1,"b":2,"c":3}}
func(**dic)
"""
# 强制使用位置参数或关键字参数
"""
约束
/ 前的参数必须使用位置传参，* 后的参数必须用关键字传参。
def f(a, b, /, c, d, *, e, f)
f(1, 2, 3, d=4, e=5, f=6)
"""


# 函数说明
# def func():
#     """说明"""
#

# return 返回到函数调用位置,在向下执行.底层会默认添加return
# def func(a,b):
#     print(a)
#     print(b)
#     return #后面没有东西，返回None
# func(1,2)
# print("end")


# 闭包  1函数的嵌套  2 内部函数访问外部函数的变量  3 外层函数的返回值是内存函数对象
# 作用    内部函数访问外部函数的变量


# 作用域
# 	L （Local） 局部作用域
#   E （Enclosing）嵌套作用域 闭包函数外的函数中
# 	G （Global） 全局作用域
# 	B （Built-in） 内建作用域
# 以 L –> E –> G –>B 的规则查找
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的

# 全局变量和局部变量
#   全局变量：作用在全局作用域的变量
#   局部变量：作用在局部作用域的变量

# 关键字
# global和nonlocal

# 你在函数内部对一个变量进行赋值操作时，Python 默认会把这个变量当作局部变量
# global
# num=10
# def func():
#     global num      #global 声明全局变量后，可以修改全局变量
#     num = 20

# nonlocal
# 内部作用域(局部作用域)修改外部作用域(嵌套作用域)
# def function_outer():
#     var1 = 1      嵌套作用域
#     def function_inner():
#         nonlocal var1     局部作用域   nonlocal 声明嵌套变量后，可以修改嵌套变量
#         var1 = 200


# 递归
#     函数体中调用自己
# 阶乘
# def func(n):
#     return n * func(n-1)        #死递归

# 要给死递归 做一个出口
# def func(n):
#     if n == 1:
#         return 1
#     return n*func(n-1)

# 匿名函数
# lambda 来定义匿名函数，所谓匿名，指其不用 def 的标准形式定义函数。
# lambda 参数列表: 表达式
# def function(a, b, add):      add表示要做的操作
#     return add(a, b)
# print(function(1, 2, lambda x, y: x + y))     #lambda省掉了def 函数名，参数不能省
# lambda 参数1, 参数2: 要做的操作
# student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
# sorted(student_list, key=lambda x: x["age"])        #key后面是排序规则

# map_result = map(lambda x: x * x, [0, 1, 3, 7, 9])
# print(list(map_result))  # [0, 1, 9, 49, 81]

# filter_result = filter(lambda x: x >= 0, [-0, -1, -3, 7, 9])
# print(list(filter_result))  # [0, 7, 9]   筛选

# red = reduce(lambda x, y: x + y, [1, 2, 3])
# print(red)

# sorted,map,filter,reduce


# 基础题（只标套路，方法都在方法地图里）
# Q1【基础】写 max2(a, b) 返回较大者（用一行条件表达式 a if a>b else b）。套路：比较选值。
# 方法一
# def max_num(a,b):
#     return max(a,b)
# print(max_num(1,2))

# 方法二
# def max_num(a, b):
    # return a if a > b else b
# print(max_num(1, 2))




# Q2【基础】写 register(name, age=18, *hobbies, **info)：print 出姓名、年龄、兴趣元组、其他信息字典；
# 用三种方式调用它（位置、关键字、混合），观察输出。套路：参数形式演练。新方法：
# *hobbies 打包元组、**info 打包字典，见上图。
# def register(name,age=18,*hobbies):
# def register(name,age=18,*hobbies,**info):
#     print(name,age,hobbies,info)


# 位置
# dict1 = {"a": 1, "b": 2, "c": 3}
# tup = ("打篮球","唱歌")
# register("李四", 20,  "打篮球",key2 = 30)
# 关键字
# register(name="尼斯", age=28, key2 = 30)
# 混合
# register("name","age","hobbies")




# Q3【基础・陷阱】运行这段代码两次并解释：
# python
# 运行
# def add(x, lst=[]):     # x形参  lst=[]是后面要做的操作
#     lst.append(x)       #把x添加到列表中
#     return lst          #return返回值为lst,后跳到调用函数的后面的部分
#
# print(add(1))   # [1]
# print(add(2))   # ？先猜再跑lst列表中[1,2]
# # 套路：观察 + 推理；方法：默认参数 / 可变对象引用（这就是图里的坑①，你要亲眼看到）。


# Q4【基础】写 calc(a, b) 返回 a+b, a-b, a*b 三个值，用 s, d, p = calc(7, 3)
# 解包输出。方法：多值返回 = 元组 + 解包。
# def calc(a,b):
#     s=a+b
#     d=a-b
#     p=a*b
#     return s,d,p
# print(calc(7,3))



# Q5【基础】写一个函数 change() 用 global 把全局变量 count 加 1，调用 3 次看变化。方法：global。
# count = 0
# def change():
#     global count
#     count += 1
#     return count
# print(change())
# print(change())
# print(change())




# 进阶题（先自己走四步法，卡 15 分钟再展开提示）
# Q6【进阶】递归阶乘：写 fact(n) 求 n!，跑 fact(5)；要有递归出口，不然就是死递归
# 再写递归版斐波那契，和迭代版对比 n=35 的耗时，说出原因。
# 套路：递归三要素（出口 + 递推式 + 缩小规模）。本题用到：递归 / 迭代 /time 模块计时。
# 1
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# 2
# def fact(n):
#     n,n+1=n+1,n+2
#     return n
#
# print(fact(3))





# Q7【进阶・D2 回炉】给成绩字典 {'Alice': 92, 'Bob': 78, 'Tom': 85, 'Eve': 92}：
# ①按分数降序输出 "姓名 分数"；
# ②分数并列时按姓名升序（先字母序）—— 提示 key=lambda x: (-x[1], x[0]) 想明白为什么。
# 套路：排序取序 / 多级排序。本题用到：sorted/items/lambda（D2 的 key 套路正式版）。
# dict1={'Alice': 92, 'Bob': 78, 'Tom': 85, 'Eve': 92}
# print(sorted(dict1.items(), key=lambda x: (-x[1],x[0])))



# Q8【进阶】闭包计数器：写 make_counter()，返回一个内层函数，
# 每次调用 +1 并返回当前值，且用 nonlocal 修改外层变量。
# 套路：闭包 + nonlocal。本题用到：嵌套函数 /nonlocal。

# def make_counter():
#     counter = 0
#     def count():
#         nonlocal counter
#         counter += 1
#         return counter
#     return count            # ✓ 不带括号！返回函数对象
# c = make_counter()          #返回的是函数对象
# print(c())
# print(c())
# print(c())









# 综合 / 实战
# Q9【综合・递归经典】汉诺塔：hanoi(n, a, b, c) 打印把 n 个盘子从 a 移到 c 的每一步（借助 b）。
# 跑 hanoi(3, 'A', 'B', 'C')。
# 套路：递归 = 把问题拆成 "移上面 n-1 个 + 移最下面 1 个 + 再移 n-1 个"。
# def func(n):





# Q10【实战・函数化改造】把今天开头的小实战改写成两个函数：get_scores() 负责循环录入返回字典；
# analyze(d) 负责输出人数 / 总分 / 平均 / 最高分 / 降序
# （含空字典保护：if not d: print("无数据"); return）。
# 套路：一个职责一个函数。本题用到：def/return/ 空字典判空。
#
# def get_scores():
#     dict1 = {}
#     while True:
#         data = input().split()
#         if len(data) == 1 and data[0] == "q":
#             dict1 = {}
#             break
#         name, score = data
#         dict1[name] = float(score)
#     return dict1
#
#
#
# def analuze(d):
#     if not d:
#         print("无数据")
# # 负责输出人数 / 总分 / 平均 / 最高分 / 降序
#     else:
#         print(len(d))
#         print(sum(d.values()))
#         print(round(sum(d.values()) / len(d),2))
#         print(max(d, key=d.get))
#         print(sorted(list(d.items()),key=lambda x:-x[1]))
# get_scores()
# analuze(dict1)


# ④ 联想微训练（只写几行思路，不写完整代码）
# 每题回答三句话：什么套路？用到哪些方法？为什么。10 分钟内完成。
# "判断字符串 s 是不是回文（如 'abcba'）"—— 你会想到哪些方法？
#做判断，把字符串倒序，用切片倒序。比较内容是否一致


# " 统计一句话里每个单词出现次数，输出出现最多的单词 "—— 这是 D2 哪个套路的变式？
#字符串统计。先用split把单词拆开，然后放到字典中去，单词是k，次数是v。
# 用get去统计次数(或者setdefault)。再用mxa，item，lambda得到最多次数的单词


# " 写一个函数，随便传多少个数字都行，返回最大值和平均值 "—— 用哪个参数形式？为什么用 sum/max 而不是自己写循环？
# 用可变位置参数(不定长参数)*args。sum和max是内置函数，可以自己比较，直接得到。


# **小实战**：
# 学生成绩管理 —— 循环输入 "姓名 成绩"，输入 `q` 结束，输出人数、总分、平均分、最高分学生姓名、
# 按成绩降序的完整名单（列表 + 字典综合，面向对象案例的前置练习）
# dic = {}
# while True:
#     data = input().split()
#     if len(data) == 1 and data[0] == "q":
#         break
#     name,age = data
#     dic[name] = int(age)
# print(len(dic))
# print(sum(dic.values()))
# print(round(sum(dic.values()) / len(dic),2))
# print(max(dic, key=dic.get))
# print(sorted(list(dic.items()),key=lambda x:-x[1]))
# dic = {'sa': 212, 'ds': 342}
# data = ['dsf', '12']
# name,age = data
# dic["name"] = int(age)
#
# print(dic)











