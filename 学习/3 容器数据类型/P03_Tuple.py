"""
    元组的基本使用
"""

# 元组的创建
# ()创建，使用()创建元组，只有一个元素时加 ,  tuple = (元素, )
# tuple1 = (100, 200, 300, 400, 500)
# tuple1 = (100,)

# tuple创建
# tuple1 = tuple([1, 2, 3])

# 推导式创建
# tuple1 = tuple((i for i in range(10)))
# print(tuple1)

# 访问元组
# tuple1 = (100, 200, 300, 400, 500)
# print(tuple1[2])
# print(tuple1[2:])
# print(tuple1[:-2])
# print(tuple1[:])

# 元组相加
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# print(tuple1+tuple2)

# 元组乘法
# tuple1 = (1, 2, 3)
# print(tuple1 * 3)


# 检查成员是否为元组中元素
# tuple1 = (100, 200, 300, 400, 500)
# print(200 in tuple1)

# 获取长度
# tuple1 = (100, 200, 300, 400, 500)
# print(len(tuple1))


# 求最值
# tuple1 = (100, 200, 300, 400, 500)
# print(max(tuple1),min(tuple1),sum(tuple1))

# 遍历
# 直接遍历
# tuple1 = (100, 200, 300, 400, 500)
# for i in tuple1:
#     print(i)

#下标遍历
# tuple1 = (100, 200, 300, 400, 500)
# for i in range(len(tuple1)):
#     print(tuple1[i])

# enumerate()
# tuple1 = (100, 200, 300, 400, 500)
# for i,val in enumerate(tuple1):
#     print(i, val)

# 元组的不可变性
# 元组的不可变指的是元组所指向的“内存中的内容"不可变，但可以重新赋值。

# tuple1 = (100, 200, 300)
# print(id(tuple1), tuple1)
# tuple1 = tuple1 + (1, 2, 3)
# print(id(tuple1), tuple1)

# 如果元组中元素是可变数据类型，其嵌套项可以被修改
# tuple1 = (100, 200, 300, [1, 2, 3])
# tuple1[3].append(4)
# print(tuple1)  # (100, 200, 300, [1, 2, 3, 4])











