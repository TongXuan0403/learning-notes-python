"""
集合的基本使用
"""
# 集合创建
# 以通过{}或set()创建集合，但创建空集合需要使用set()而非{}，因为{}会创建空字典。
# set()创建
# set1 = set([1, 2, 3])

# {}创建
# set1 = {1, 2, 3}

# 推导式
# set1 = set((i for i in range(10)))
# print(set1)


# 添加元素
# set1 = {1, 2, 3}
# set1.add(4)
# set1.add(6)
# print(set1)

# 删除元素
# set1 = {1, 2, 3}
# set1.remove(2)
# print(set1)

# 检查成员是否为集合中元素
# set1 = {1, 2, 3, 4, 5}
# print(3 in set1)

# 获取长度
# set1 = {1, 2, 3, 4, 5}
# print(len(set1))

# 求最值
# set1 = {1, 2, 3, 4, 5}
# print(max(set1),min(set1),sum(set1))

# 遍历
#直接遍历
# set1 = {1, 2, 3, 4, 5}
# for i in set1:
#     print(i)


# 常用函数
# set.add(x)	添加元素
# set.update(x)	添加元素，x可以为列表、元组、字符串、字典等可迭代对象
# set.union(x)	添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
# set.remove(x)	从集合中移除x，x不存在则报错
# set.discard(x) 	从集合中移除x，x不存在也不报错
# set.pop()	随机取出集合中的一个元素，如果集合为空则报错
# set.clear()	清空集合
# set.difference(x1,...)	求set1和x1的差集，返回一个新的集合
# set.difference_update(x1,...)	求set1和x1的差集
# set.intersection(x1,...)	求set1和x1的交集，返回一个新的集合
# set.intersection_update(x1,...)	求set1和x1的交集
# set1 & set2	两集合求交集
# set1 | set2	两集合求并集
# set1 - set2	两集合求差集
# set1.isdisjoint(set2)	判断两集合是否没有交集
# set1.issubset(set2)	判断set1是否为set2的子集
# set1.issuperset(set2)	判断set2是否为set1的子集
# set1.symmetric_difference(set2)	求两集合中不重复的元素，返回一个新的集合
# set1.symmetric_difference_update(set2)	求两集合中不重复的元素
# set.copy()	拷贝集合
# len(set)	返回集合元素个数
# max(set)	求集合中元素的最大值
# min(set)	求集合中元素的最小值
# sum(set)	求集合中元素的加和






























