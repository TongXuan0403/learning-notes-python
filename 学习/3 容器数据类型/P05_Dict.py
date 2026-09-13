"""
字典的基本使用
"""
# 字典的创建
# 可以通过{}或dict()创建字典。
# {}创建
# dict1 = {}
# dict2 = {1: '1', 2: '2', 3: '3'}
# print(dict1)
# print(dict2)

# dict()创建
# dict1 = dict(a=1, b=2, c=3)
# print(dict1)
# dict2 = dict([("name", "Tom"), ("age", 22), ("gender", "male")])
# print(dict2)

#推导式创建
# dict1 = {i: i*2 for i in range(10)}
# print(dict1)

# 访问字典

# 通过key去访问value，通过不存在的key去访问会报错
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# print(dict1["name"])

# 通过get()访问，若不存在，返回None
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# print(dict1.get("name"))
# print(dict1.get("sex"))


# 向字典中添加元素
# 为字典指定的key赋值value，若key原本不存在则会被添加。
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# dict1["address"] = "earth"
# print(dict1)

# 修改字典中元素
# 通过key修改对应的value。
# dict1 = {"name": "Alice", "age": 18, "gender": "male"}
# dict1["name"] = "Bob"

# 检查成员是否为字典中的key
# dict1 = {"name": "Alice", "age": 81, "gender": "male"}
# print("name" in dict1)
# print("Alice" in dict1)

# 获取字典长度
# dict1 = {"name": "Alice", "age": 81, "gender": "male"}
# print(len(dict1))


# 遍历
my_dict = {'Name': 'Tom', 'Age': 17}

# 遍历key
# keys = my_dict.keys() #keys()返回字典中的key
# for k in keys:
#     print(k)

#遍历value
# vals = my_dict.values()
# for v in vals:
#     print(v)

# 遍历k-v
# keys = my_dict.keys()
# for key in keys:
#     print(key, my_dict[key])

# kv = my_dict.items()
# for k in kv:
    # print(k)


#删除字典元素
# my_dict = {'Name': 'Tom', 'Age': 17}
# del my_dict['Name'] # 删除键 'Name'
# my_dict.clear()     # 清空字典
# del my_dict         # 删除字典

# print (my_dict)


# 常用函数
# del dict[key]	根据key删除键值对
# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
# dict.clear()	清空字典
# dict1.update(dict2)	将dict2中的键值对更新到dict1中
# dict.get(key[,default])	获取字典中key对应value，可设置默认值
# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值
# dict.keys()	获取字典所有的key，返回一个视图对象。字典改变，视图也会跟着变化
# dict.values()	获取字典所有的value，返回一个视图对象
# dict.items()	获取字典所有的(key,value)，返回一个视图对象
# dict.copy()	拷贝字典
# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值
