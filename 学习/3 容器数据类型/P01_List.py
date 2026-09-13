"""
    列表的基本使用
"""
#创建列表 1用[]创建。2用list()创建  3推导式

# list1 = [100,200,300,400,500]
# print(type(list1))
# print(list1)

# list1 = list([123,34])
# print(type(list1))
# print(list1)

# list1 = list(i for i in range(10))
# print(list1)

#列表索引访问[下标]
# print(list1[2])
# print(list1[-3])

#列表切片list[开始:结束:步长]
# list1 = [100,200,300,400,500]
# # 取全部元素
# print(list1)
# # 复制整个列表
# print(list1[:])
# # 取索引从2开始到4(不包含)的元素
# print(list1[2:4])
# # 取索引从2开始到末尾的元素
# print(list1[2:])
# # 取索引从2开始到-1(不包含)的元素
# print(list1[2:-1])
# # 取索引从0开始到2(不包含)的元素
# print(list1[0:2])
# # 倒序取元素
# print(list1[::-1])


# 列表中添加元素 1 末尾添加list.append(元素) 。2 指定添加list.insert(下标，元素)
# list1 = [100,200,300,400,500]
# # append在末尾添加元素。insert在指定位置添加元素
# list1.append(600)
# list1.insert(1,500)
# print(list1)

# 列表相加
# list1 = [100,200,300]
# list2 = ["a","b","c"]
# print(list1 + list2)

# 列表乘法
# list1 = [1, 2, 3]
# print(list1 * 2)

# 修改列表中元素 1，下标修改list[下标] = 元素  2，切片修改 list[开始：结束]=[元素]
# 下标修改
# list1 = [100, 200, 300, 400, 500]
# list1[0] = 200
# print(list1)

# 切片修改
# list1 = [100, 200, 300, 400, 500]
# list1[2:4] = [30,10]
# print(list1)

# 检查成员是否为列表中元素 使用in   元素 in list 返回布尔值
# list1 = [100, 200, 300, 400, 500]
# print(100 in list1)

# 检查列表长度  使用len(list())
# list1 = [100, 200, 300, 400, 500]
# print(len(list1))

# 求列表中元素的最值，求和
# list1 = [100, 200, 300, 400, 500]
# print(max(list1))
# print(min(list1))
# print(sum(list1))

# 遍历列表,1直接遍历。2通过下标遍历。3使用enumerate()获取下标和元素
# list1 = [100, 200, 300, 400, 500]
# 直接遍历
# for _ in list1:
#     print(_)

# 通过下标遍历
# for i in range(len(list1)):
#     print(list1[i])

# 使用enumerate()同时获取列表的下标和元素

# for i, val in enumerate(list1):
#     print(i, val)
#


# del删除列表指定位置元素或者切片
# list1 = [100, 200, 300, 400, 500]
# del list1[3]
# print(list1)


# 嵌套列表 list = [元素，[元素]]  访问 lsit[索引][索引]
# list1 = [1, 2, 3, [1, 2, 3], [5, 6, 7]]
# print(list1[3][2])

# 列表推导式
# （1）基础的列表推导式  list = [表达式 for i in range(4)]
# list1 = [i*2 for i in range(1, 11)]
# print(list1)
# （2）带条件的列表推导式  list = [表达式 for i in range[5] 条件]
# list1 = [i*2 for i in range(1, 11) if i % 2 == 1]
# print(list1)
# （3）使用现有列表的列表推导式
# list1 = [1, 2, 3, 4, 5]
# print([i for i in list1 if i != 2])  #[1, 3, 4, 5]
# （4）包含多个循环的列表推导式
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# tuple_list = [(i,j) for i in list1 for j in list2]
# print(tuple_list)

#zip()函数
# zip() 函数可将多个可迭代对象中对应元素打包为一个个元组。
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# zipped = zip(list1, list2)
# print(list(zipped))


# 常用函数
# list1 = [1, 2, 3]
# list.insert(index,x)	在指定位置插入x
# print(list1.insert(2,5))

# list.append(x)	在列表末尾追加x
# print(list1.append(4))

# list1.extend(list2)	在列表1的末尾追加列表2的数据
# list2 = [4, 5, 6, 7]
# list1.extend(list2)
# print(list1)

# del list[index]	删除指定位置的数据或切片
# del list1[2]
# print(list1)

# list.remove(x)	删除第一次出现的x
# list2 = [2, 2, 10, 4, 5, 6]
# list2.remove(2)
# print(list2)

# list.pop([index])	删除指定位置的数据，默认为末尾数据
# list2.pop(2)
# print(list2)


# list.clear()	清空列表中元素
# list2.clear()
# print(list2)


# list[index] = x	修改指定位置的数据
# list2[2] = 1
# print(list2)


# list1[start:end] = list2	修改列表切片的数据


# sorted(list[,reverse=True])	返回排序后的新列表，可选降序
# print(sorted(list2, reverse=True))

# list.sort([reverse=True])	对列表就地排序，可选降序
# list2.sort(reverse=True)
# print(list2)

# list.reverse()	反转列表中的元素
# list2.reverse()
# print(list2)

# list.index(x[,start,[,end]])	返回x在列表中首次出现的位置，可指定起始和结束范围

# list.count(x)	返回x的数量
# print(list2.count(2))

# len(list)	返回列表元素个数

# max(list)	返回列表中最大值

# min(list)	返回列表中最小值

# sum(list)	返回列表中所有元素和

# list.copy()	拷贝列表
# list4 = list1.copy()
# print(list4,id(list4))
# print(list1,id(list1))

# 列表中的删除问题
# 将列表中的1全删除掉
# 可以用列表的推导式 或者 重新copy一个新列表
# list1 = [1, 2, 3, 4, 1, 1, 6, 1]
# for item in list1:
#     if item == 1:
#         list1.remove(item)
# print(list1)

# 推导式
# print([i for i in list1 if i != 1])



















