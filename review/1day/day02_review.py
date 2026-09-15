#一、知识速整
#每个点写 "一句话笔记 + 3~5 行最小示例"：
from numpy.ma.core import append

# 1. **序列共性**：索引、切片 `[start:stop:step]`、`len()`、`in`、遍历（列表 / 字符串 / 元组都是序列）
# list,str,tuple。都是有序，可以索引，切片
# 切片，索引，相加，乘法，检查成员，计算长度，求最值


# 2. **列表 List（可变）**：
# 增 `append/extend/insert` 的区别；
# append在末尾添加元素，把[]当成一个整体进行添加lst.append([3,4])  # 输出：[1, 2, [3, 4]]  任意对象
# extend在末尾添加元素，一个一个添加进去lst.extend([3,4])  # 输出：[1, 2, 3, 4]  x 必须是可迭代对象
# insert指定位置插入元素

# 删 `pop(按位置)/remove(按值)/del/clear`；
# pop指定位置删除，默认是删除末尾
# remove删除第一次出现的x
# del删除指定位置的数据或切片
# clear清空列表

# 改 `lst[i]=x`；
# 查 `index/count/in`；
# count返回数量
# in检查元素的存在，返回布尔值
# index返回x在列表中首次出现的位置，可指定起始和结束范围
# `sort()` 原地排序 vs `sorted()` 返回新列表；
# 嵌套列表；
# **列表推导式** `[表达式 for x in 序列 if 条件]`；

# `zip()` 并行遍历
# zip() 函数可将多个可迭代对象中对应元素打包为一个个元组。


# 3. **字符串 String（不可变）**：
# 分隔字符
# `split/join/replace/strip/find/count/startswith`；
# str.split([x][,n])分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数
# x.join(seq)	以x作为分隔符，将序列中所有的字符串合并为一个新的字符串
# str.rsplit([x][,n])	与split()类似，从右边开始分隔


# str.strip([x])	截掉字符串两边的空格或指定字符
# str.find(x[,start][,end])	返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
# str.startswith(x[,start][,end])	检查字符串是否以x开头，可指定字符串开始结束范围
# str.count(x[,start][,end])	返回字符串中x的个数，可指定字符串开始结束范围



# 大小写 `upper/lower`；
# upper所有字符转大写
# lower所有字符转小写

# 判断 `isalpha/isdigit/isspace`
# isalpha 字符
# isdigit 数字
# isspace 空格



# 4. **元组 Tuple（不可变）**：
# 单元素 `(1,)` 逗号不能省；
# 打包解包（`a,b=b,a` 原理）；
# 函数多返回值本质就是元组


# 5. **集合 Set（无序、不重复）**：
# 空集合只能用 `set()`；
# set1 = set()

# `add/remove/discard`；
# remove移除元素，元素不存在报错
# discard移除元素，不存在也不报错

# 交集 `&`、  并集 `|`、  差集 `-`、  对称差 `^`


# 6. **字典 Dict（键唯一）**：
# `d[k]` 与 `get(k, 默认值)` 的区别；
# [] k不存在报错
# get() k不存在报None

# `setdefault/update/pop`；
# pop获取key所对应的value，同时删除该键值对，可设置默认值
# update更新新键值对到字典中

# 遍历 `items()`；
# `in` 判断的是键


# 7. **收尾**：
# 自己画一张 "列表 / 元组 / 集合 / 字典" 区别表（可变性、是否有序、能否重复、典型用途）


#
# 二、分层题目（4–5h，共 10 题）
#
# 基础（必做）
#
# 1. **列表增删改查**：
# 建 `[3,1,4,1,5]`，依次执行 `append(9)`、`insert(0,0)`、`extend([2,6])`、
# `remove(1)`、`pop()`、`sort()`，每步打印，说出 append 和 extend 的区别
# append,视为一个整体进行添加。extend，一个一个进行添加
# list1 = [3,1,4,1,5]
# list1.append(9)
# print(list1)
# list1.insert(0, 0)
# print(list1)
# list1.extend([1,2,3,4,5])
# print(list1)
# list1.remove(1)
# print(list1)
# list1.pop()
# print(list1)
# list1.sort()
# print(list1)


# 2. **列表推导式**：
# a) 生成 1~100 偶数的平方列表；b) 再筛出能被 3 整除的；c) 把 `["AbC","dEf"]` 全部转小写
# list1 = [i**2 for i in range(1,101) if i % 2 == 0]

# print([i**2 for i in range(1, 101) if i % 6 == 0])        # b) 偶数且被3整除=被6整除
#

# list2 = ["AbC","dEf"]
# for i in list2:
#     j=i.lower()
#     print(j)
# list2 = [i.lower() for i in ["AbC","dEf"]]


# 3. **字符串**：
# `s = "  Hello, Python World  "`，完成 `strip`、按逗号 `split`、`replace`、`find("Python")`、
# # `count("o")`、`upper`；再用 `join` 把 `["2026","09","14"]` 拼成 `"2026-09-14"`
# s = "  Hello, Python World  "
# print(s.strip())    #Hello, Python World 默认去掉两边的空格
# print(s.split(","))    #['Hello,', 'Python', 'World']
# print(s.replace('Python', 'Java'))      #Hello, Java World   替换
# print(s.find('Python'))     #返回索引位置
# print(s.count('o'))       #统计指定元素个数
# print(s.upper())    #字符串全改大写
#
# x = ["2026","09","14"]
# x1 = "-"
# print(x1.join(x))


# 4. **元组解包**：
# 写函数 `min_max(nums)` 一次返回最小值和最大值，调用处解包成两个变量；
# 再验证为什么 `(1)` 不是元组而 `(1,)` 是
# def min_max(nums):
#     min_value = min(nums)
#     max_value = max(nums)
#     return min_value, max_value
# # 解包
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a, b = min_max(data)
# print(a, b)

# print(type((1)), type((1,)))



# 5. **集合运算**：
# `a={1,2,3,4}`、`b={3,4,5,6}`，输出交 / 并 / 差集；& | -
# 给 `[1,2,2,3,3,3]` 去重 —— 写出**三种**写法（对比你 D1 卡住的 Q4）
# a={1,2,3,4}
# b={3,4,5,6}
# print(a&b)
# print(a|b)
# print(a-b)
# list1 = [1,2,2,3,3,3]
# print(list(set(list1)))   #利用集合的特性


# 不推荐
# new = []
# [new.append(x) for x in list1 if x not in new]  推导式 和 not in
# print(new)

# new = []
# for i in list1:
#     if i not in new:
#         new.append(i)
# print(new)

# print(list(dict.fromkeys(list1)))     #字典key不可重复..以序列seq中元素做字典



# 6. **字典基础**：
# 建一个学生字典，演示 `d[k]`、`get(键, 默认值)`、`update`合并、
# `pop` 删除、用 `items()` 遍历打印 "姓名: xx，分数: xx"
# dict1 = dict(name="Bob", age=20, gender="female")
# print(dict1["age"])
# print(dict1["name1"])
# print(dict1.get("age"))
# print(dict1.get("age1"))
# dict2 = dict(nam1e="John", ag1e=30, gende1r="male")
# dict1.update(dict2)
# print(dict1)
# dict1.pop("name")
# print(dict1)
# for i,j in dict1.items():
#     print(i,j)

# `items()` 要解包成 `for k, v in d.items(): print(f"{k}: {v}")`

#
# 进阶
#
# 7. **词频统计（摸底 Q5，今天必须拿下）**：
# 统计 `"the cat sat on the mat the cat"`
# 中每个单词的次数，并按次数**降序**输出（`get/setdefault` 计数 + `sorted(items, key=lambda x: x[1], reverse=True)`）
# str1 ="the cat sat on the mat the cat"
# str1.split()    #把字符拆开
# d = {}      #创建字典，key放字符，value放出现次数
# for i in str1.split():
#     d.setdefault(i, 0)      #遍历出来，创建字典
#     d[i] += 1               #重复的字符value+1
# print(d)
#
# #d.items() k和v的字典，`lambda x: x[1]`：匿名函数，
# # 拿到每一个元素`x`，返回`x[1]`作为排序依据
# red = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(red)



# 8. **二维列表**：
# `[[88,76,92],[66,77,88],[99,91,85]]`，
# 输出每人平均分、每科平均分、总平均分（提示：`zip(*scores)` 可以按列取）
# list1 = [[88,76,92],[66,77,88],[99,91,85]]
# zippend = zip(*list1)
# list1 = []
# for item in zippend:
#
#
#     avg = sum(item)/len(item)
#
#     print(item, avg)
# print(num / len(list1))

# 修改
# scores = [[88, 76, 92], [66, 77, 88], [99, 91, 85]]
# print("每人平均:", [round(sum(r)/len(r), 2) for r in scores])       # [85.33, 77.0, 91.67]
# print("每科平均:", [round(sum(c)/len(c), 2) for c in zip(*scores)]) # [84.33, 81.33, 88.33]
# print("总平均:", round(sum(sum(r) for r in scores)/9, 2))           # 84.67
# for r in zip(*scores):
#     print(r)              #解包后同索引的放在以个元组中




# print(list(zipped))

# 9. **薄弱点回炉①（数位）**：
# 写函数 `digits(n)` 把整数每位拆成列表（`12345 → [1,2,3,4,5]`）；
# 再用列表收集 100~999 全部水仙花数，重做 D1 的 Q6 并核对结果应为 153/370/371/407
# def digits(n):
#     list1 =[int(i) for i in str(n)]
#     # list1 = []
#     # for i in str(n):
#     #     list1.append(int(i))
#
#     list2 = []
#     for i in range(100,999):
#         a = i % 10
#         b = i // 100
#         c = i % 100 // 10
#         if a ** 3 + b ** 3 + c ** 3 == i:
#             list2.append(i)
#     print(list2)
#     print(list1)
# digits(12345)


# def digits(n):
#     res = []
#     while n>0:
#         res.append(n % 10)
#         n //= 10
#     print(res[::-1])
# digits(12345)






# 10. **薄弱点回炉③（字符统计）**：
# 重做 D1 的 Q8（字母 / 数字 / 空格 / 其他计数），
# 并额外统计每个字母（不区分大小写）出现次数存入字典，输出出现次数最多的字母
# letter number space other
# 分类用  字母isalpha()  数字isdigit()  空白isspace()
# letter = number = space = other = 0
# str1 = input()
# letter, number, space, other = 0,0,0,0      #统计次数
# dict1 = {}                                  #创建字典，key放字符，value放出现次数
# for item in str1:
#     if item.isalpha():                      #分类，字符
#         letter += 1
#         dict1.setdefault(item, 0)           #实现字典k-v，k接受出现的字符。v暂设为0
#         dict1[item] +=1                     #表示value，key出现，value加1
#
#     elif item.isdigit():                    #分类，数字
#         number +=1
#     elif item.isspace():                    #分类，空格
#         space += 1
#     else:
#         other += 1
# print(letter, number, space, other)
# print(dict1)
# print(max(dict1.items(),key=lambda x: x[1]))          #
# print(max(dict1, key=dict1.get))      #只拿字母

# 对字母统计的修改
# d = {}
# for ch in s:
#     if ch.isalpha():
#         k = ch.lower()
#         d[k] = d.get(k,0)+1         #d.get(k,[默认值])获取字典中key对应value，可设置默认值
#       letter += 1
#       dict1.setdefault(item, 0)   #实现字典k-v，k接受出现的字符。v暂设为0
#       dict1[item] +=1

# lambda x: x[1]      匿名函数，x 接收上面每一个(k,v)元组
# key=lambda x:x[0] → 按key（键）排序
# key=lambda x:x[1] → 按value（值）排序









#
# **小实战**：
# 学生成绩管理 —— 循环输入 "姓名 成绩"，输入 `q` 结束，输出人数、总分、平均分、最高分学生姓名、
# 按成绩降序的完整名单（列表 + 字典综合，面向对象案例的前置练习）


dict1 = {}
while True:
    data = input().split()
    if len(data) == 1 and data[0] == 'q':
        break
    name, score = data
    dict1[name] = int(score)
list1 = list(dict1.items())
# print(dict1)
print(list1)










