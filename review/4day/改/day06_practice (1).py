# -*- coding: utf-8 -*-
# ============================================================
#  D6 练习册 · 模块包 + 迭代器/生成器 + 装饰器（正则仅了解）（2026-09-17）
#  配套知识卡：day06_README.md（建议 PyCharm 左右分屏）
#  今日重点：①迭代器/生成器（LLM 流式输出的底层）②装饰器（FastAPI/LangChain 到处是 @）
#  正则：仅 W7 热身快速过，会 findall/sub 即可，不出大题
#  今日流程：① 热身跟写 W1~W7（约1h）→ ② 正式题 Q1~Q10（约4~5h）→ ③ 联想微训练（口述）
#  做完直接保存本文件发我，不用另存。
# ============================================================
#
#  【每日作战卡 · 第1周 v1】
#  开做前四步：①先写样例明确输入输出 ②中文写步骤(写成注释) ③查知识卡方法地图 ④最简样例先跑通
#  卡住纪律：15分钟不看答案——写清卡在哪一步、翻知识卡、先写个笨版本；来问我只给方向
#  今日待还债 ⚠：周末（D7 周测时）白纸重写 D4 的 Q4/Q6/Q7/Q8
#  今日盯防：生成器调用不执行(yield)；装饰器忘加 wraps；带参装饰器少一层；浅拷贝嵌套共享
#  收工三问：输出点齐吗？ 看提示的题标 ⚠ 了吗？ 每题写题眼(一句话)了吗？
#
# ============================================================
#  第一部分 · 基础热身跟写（先做，约1h）
#  做法：打开 README.md，照着「最小示例」亲手敲一遍并运行，再完成每条的「微调」。
# ============================================================

import json
import time
import copy
import functools
import re


# ---------- W1 模块导入 ----------
# 跟写：照 README【最小示例1】敲 import / from...import / as 别名
# 微调：导入 os 模块并起别名 op，打印 op.getcwd()

# 你的代码：
# import os as op
# print(op.getcwd())

# ---------- W2 浅拷贝 vs 深拷贝 ----------
# 跟写：照 README【最小示例2】敲嵌套列表的 copy / deepcopy，观察内层是否被影响
# 微调：把 a 改成字典嵌套列表 {"a":[1,2]}，再试浅拷贝改内层

# 你的代码：
# a = {"a":[1,2]}
# b = copy.copy(a)
# c = copy.deepcopy(a)
# a["a"][1] = 99
# print(b["a"][1])
# print(c["a"][1])


# ---------- W3 手写迭代器 ----------
# 跟写：照 README【最小示例3】敲 CountDown 迭代器类（__iter__ + __next__ + StopIteration）
# 微调：仿写一个 CountUp 迭代器，从 0 数到 n（含）

# 你的代码：


# 一种
# class my_list_data:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         res = self.data[self.index]
#         self.index += 1
#         return res
#
# class my_list:
#     def __init__(self,data):
#         self.data = data
#
#     def __iter__(self):
#         return my_list_data(self.data)
# ml = my_list([1,3,5,2])
# mld = iter(ml)
# print(next(mld))
# print(next(mld))
# print(next(mld))
# print(next(mld))
# print(next(mld))


# 第二种
# class Count:
#     def __init__(self,data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         result = self.data[self.index]
#         self.index += 1
#         return result
#
# c = Count([3,4,5,62,13])
# cl = iter(c)
# print(next(cl))
# print(next(cl))
# print(next(cl))
# print(next(cl))
# print(next(cl))
# print(next(cl))


# 第三种
# class Count:
#     def __init__(self,data):
#         self.data = data
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= self.data:
#             raise StopIteration
#         self.count += 1
#         return self.count
#
# for n in Count(3):
#     print(n)

# ---------- W4 生成器 ----------
# 跟写：照 README【最小示例4】敲 fib_gen 生成器函数（yield）
# 微调：仿写一个 even_gen(n) 生成器，yield 0~n 内的所有偶数

# 你的代码：
# def fib_gen(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#         yield b
#
# for x in fib_gen(10):
#     print(x)


# def even_gen(n):
#    for i in range(n):
#        if i % 2 == 0 and not i == 0:
#            yield i
# for x in even_gen(10):
#     print(x)

# ---------- W5 最简单装饰器（计时）----------
# 跟写：照 README【最小示例5】敲 timer 装饰器，装饰一个 sleep 函数
# 微调：仿写一个 log_call 装饰器，打印"调用了函数名"和参数

# 你的代码：
# def timer(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper
#
# @timer
# def slow():
#     time.sleep(1)
# slow()


# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__, args, kwargs)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log_call
# def cs(a,b):
#     return a+b
#
# @log_call
# def cs2(a,b):
#     return a*b
#
# @log_call
# def cs3(name):
#     return name
# cs(1,4)
# cs2(5,9)
# cs3(name = "张三")


# ---------- W6 带参装饰器 + wraps ----------
# 跟写：照 README【最小示例6】敲 repeat(times) 带参装饰器 + functools.wraps
# 微调：把 @functools.wraps 注释掉，打印 greet.__name__ 看变成什么

# 你的代码：
# def repeat(time):
#     def decorator(func):
#         @functools.wraps(func)    #注释掉。打印greet.__name__显示wrapper这个函数名
#         def wrapper(*args, **kwargs):
#             for i in range(time):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet():
#     print("hello")
# greet()
# print(greet.__name__)
#
#@functools.wraps(func)会获取到func这个函数的函数名



# ---------- W7 正则（了解即可，会用 findall/sub 就行，不深究）----------
# 跟写：照 README【最小示例7】敲 re.findall 提取手机号、re.sub 替换数字
# 目标：知道正则能干"提取/替换"这件事、看得懂简单模式即可，不用背元字符

# 你的代码：

# text = "联系电话：138123456789"
# print(re.findall(r'1[3-9]\d{9}',text))
# print(re.sub(r'\d+','***',text))


# ============================================================
#  第二部分 · 正式题目 Q1~Q10（每题先走四步法，再动手）
#  规则：每题只给【本题用到】的方法名，不给步骤；卡15分钟再来问。
#  题量分布：迭代器/生成器 Q3/Q4/Q9/Q10；装饰器 Q5/Q6/Q7/Q8/Q10
# ============================================================

# ---------- Q1【基础】模块与 __name__ ----------
# 题目：写一个模块 my_math.py（实际新建文件），里面有函数 add(a,b) 返回 a+b；
#       模块底部写 if __name__ == "__main__": 测试 print(add(1,2))。
#       然后在另一个文件里 import my_math，调用 my_math.add(3,4)，观察测试代码是否执行。
# 输入：两个文件的代码
# 输出：直接运行 my_math.py 时打印 3；import 时不打印 3
# 验收：说清为什么 import 时测试代码不执行
# 【本题用到】import、__name__、if __name__ == "__main__"

# 你的代码（或写在独立文件里，把内容贴这）：

# import my_math
# my_math.add(3, 4)       #不打印，因为my_math模块中的add函数只是放回了计算值，my_math.add(3,4)是调用add这个函数然后传俩实参
# print(my_math.add(3, 4))        #打印


# ---------- Q2【基础】浅拷贝 vs 深拷贝 ----------
# 题目：给定嵌套列表 data = [[1,2],[3,4],[5,6]]，分别做：
#   ① 赋值 ref = data
#   ② 浅拷贝 shallow = data.copy()
#   ③ 深拷贝 deep = copy.deepcopy(data)
#   然后修改 data[0][0] = 99，分别打印 ref[0][0]、shallow[0][0]、deep[0][0]
# 输出：三个值 + 一句话解释为什么 shallow 被影响而 deep 没有
# 验收：三个值正确（99、99、1）
# 【本题用到】= 赋值、.copy()、copy.deepcopy()、嵌套列表

# 你的代码：

# data = [[1,2],[3,4],[5,6]]
# ref = data
# shallow = data.copy()
# deep = copy.deepcopy(data)
# data[0][0] = 99
# print(ref[0][0])
# print(shallow[0][0])
# print(deep[0][0])   #deep是深拷贝。内层数据地址独立



# ---------- Q3【进阶】手写迭代器：斐波那契 ----------
# 题目：写一个 FibIterator 类，实现迭代器协议，迭代时依次产出斐波那契数列前 n 项。
# 输入：FibIterator(6)
# 输出：for 循环打印 1 1 2 3 5 8
# 验收：实现 __iter__ 返回 self、__next__ 产出下一项、超过 n 抛 StopIteration
# 【本题用到】class、__iter__、__next__、StopIteration

# 你的代码：

# class FibIterator:
#     def __init__(self,n):
#         self.n = n
#         self.index = 0
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.index >= self.n:
#             raise StopIteration
#         self.index += 1
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
# fib = FibIterator(6)
# for i in fib:
#     time.sleep(0.3)
#     print(i)


# ---------- Q4【进阶·AI场景】生成器模拟 LLM 流式输出 ----------
# 题目：写一个生成器函数 stream_tokens(text, delay=0.05)，把 text 按字符逐个 yield，
#       每个字符之间 time.sleep(delay) 模拟模型逐字输出。
#       主程序：for token in stream_tokens("你好，我是AI助手"): print(token, end="", flush=True)
# 输入：字符串 "你好，我是AI助手"
# 输出：逐字打印（不是一次性全出来）
# 验收：函数用 yield；调用时不立即执行，for 遍历时才逐字产出
# 【本题用到】def + yield、生成器、time.sleep、for 遍历生成器、print(end="",flush=True)

# 你的代码：

# def stream_tokens(text, delay=0.05):
#     for i in text:
#         time.sleep(delay)
#         yield i
#
# for token in stream_tokens("你好，我是AI助手"):
#     print(token, end="", flush=True)


# ---------- Q5【进阶】不带参装饰器：日志 ----------
# 题目：写一个 log_decorator 装饰器，被装饰函数调用时打印：
#   "调用函数：函数名，参数：(args, kwargs)"，函数执行完打印"返回值：xxx"
#       用它装饰一个 add(a,b) 函数，调用 add(3,5) 验证
# 输入：add(3,5)
# 输出：调用函数：add，参数：((3, 5), {})；返回值：8
# 验收：装饰器不修改原函数逻辑；*args/**kwargs 能接收任意参数
# 【本题用到】def 嵌套（闭包）、*args/**kwargs、@装饰器语法糖

# 你的代码：
# def log_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"调用函数：{func.__name__},参数:({args},{kwargs});返回值：{result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
# add(3, 5)



# ---------- Q6【进阶】带参装饰器：重试（AI 调 API 必用）----------
# 题目：写一个 retry(times, delay) 带参装饰器：被装饰函数如果抛异常，就重试 times 次，
#       每次重试间隔 delay 秒；全部失败则抛最后一次异常。
#       用它装饰一个"前2次抛异常、第3次成功"的函数，调用验证重试行为。
# 输入：@retry(times=3, delay=0.1) 装饰一个前2次失败第3次成功的函数
# 输出：打印每次重试提示，最终成功返回结果
# 验收：三层嵌套（外层收参数、中层收函数、内层wrapper）；try/except 捕获异常
# 【本题用到】带参装饰器三层嵌套、try/except、time.sleep

# 你的代码：
# def retry(times, delay):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             count = None
#             for i in range(times):
#                try:
#                    func(*args, **kwargs)
#                    return f"第 {i+1} 次成功"
#                except Exception as e:
#                     count  = e
#                     print(f"第 {i+1} 次失败：{e}，{delay}s 后重试")
#                     time.sleep(delay)
#             raise count
#         return wrapper
#     return decorator
#
# dic = {"n":0}
# @retry(times=3, delay=0.1)
# def func():
#     dic["n"] += 1
#     if dic["n"] < 3:
#         raise RuntimeError(f"网络抖动，第 {dic['n']} 次")
# print(func())


# ---------- Q7【基础】functools.wraps 的作用 ----------
# 题目：写两个版本的计时装饰器：
#   版本A：不加 @functools.wraps
#   版本B：加 @functools.wraps(func)
#   分别装饰同一个函数，打印被装饰后函数的 __name__ 和 __doc__
# 输入：同一个函数被两个版本装饰
# 输出：版本A __name__ = wrapper；版本B __name__ = 原函数名
# 验收：说清 wraps 解决了什么问题
#解决了被访问到函数名，被访问可能对重复函数名，会起冲突
# 【本题用到】@functools.wraps、__name__、__doc__

# 你的代码：

# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return result
#     return wrapper
# @timer
# def show():
#     time.sleep(1)
# show()
# print(show.__name__)
# print(show.__doc__)


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return result
#     return wrapper
# @timer
# def show():
#     time.sleep(1)
# show()
# print(show.__name__)
# print(show.__doc__)



# ---------- Q8【进阶】多个装饰器叠加执行顺序 ----------
# 题目：写两个装饰器 A 和 B，每个在函数执行前后打印标记（如"A前置"/"A后置"/"B前置"/"B后置"）。
#       然后：
#         @A
#         @B
#         def func(): print("函数执行")
#       调用 func()，观察打印顺序
# 输入：func()
# 输出：A前置 → B前置 → 函数执行 → B后置 → A后置（洋葱模型，从下往上包）
# 验收：说清为什么 B 比 A 先执行（靠近函数的先包）
# 【本题用到】多个 @ 叠加、装饰器本质（函数 = A(B(函数))）、print 标记

#先装饰b再装饰a，先执行a再执行b

# 你的代码：

# def A(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("A前置")
#         func(*args, **kwargs)
#         print("A后置")
#         # return func(*args, **kwargs)
#     return wrapper
# def B(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("B前置")
#         func(*args, **kwargs)
#         print("B后置")
#         # return func(*args, **kwargs)
#     return wrapper
# @A
# @B
# def func():
#     print("函数执行")
# func()

# ---------- Q9【进阶】生成器管道（数据处理 pipeline）----------
# 题目：用生成器串成一条数据处理管道，每一环都是"接收一个可迭代对象、yield 处理结果"：
#   ① numbers(n)：yield 1~n 的整数
#   ② evens(it)：从 it 中只 yield 偶数
#   ③ squared(it)：从 it 中把每个数平方后 yield
#   主程序：for x in squared(evens(numbers(10))): print(x)
# 输入：numbers(10)
# 输出：4 16 36 64 100（即 2² 4² 6² 8² 10²）
# 验收：三个函数都用 yield（不是 return 列表）；理解数据是"流过"管道、每环惰性处理
# 思考题（写注释）：如果 numbers 改成 yield 1~1亿，管道会不会占 1 亿个元素的内存？为什么？

# 不会，yield是用多在取多少。一用一取

# 【本题用到】def + yield、生成器之间串联（一个生成器 for 遍历另一个）、惰性求值

# 你的代码：


# def numbers(n):
#     for i in range(1,n+1):
#         yield i
#
# def evens(it):
#     for x in it:
#         if x % 2 == 0:
#             yield x
#
# def squared(it):
#     for x in it:
#         yield x ** 2
#
# for x in squared(evens(numbers(10))):
#     print(x)





# ---------- Q10【综合·AI场景】装饰器 + 生成器：可计时的流式 LLM ----------
# 题目：综合今天两大重点：
#   1) 写一个 @timing 装饰器（计时，必须加 functools.wraps），装饰普通函数时打印耗时
#   2) 写一个生成器函数 fake_llm_stream(prompt)：
#        - 先根据 prompt 拼出一句固定回复，如 f"关于「{prompt}」，我的回答是：……"（自己写一句10字以上的话）
#        - 把回复按字符逐个 yield，每个 yield 前 time.sleep(0.03)
#   3) 主程序：for token in fake_llm_stream("什么是装饰器"): print(token, end="", flush=True)
#      逐字打印结束后，另打印总耗时（在主程序用 time.time() 自己计时即可；
#      若想挑战，可尝试让 timing 装饰一个"驱动生成器跑完"的函数，能做到哪种算哪种，注释说明）
# 输入：prompt = "什么是装饰器"
# 输出：逐字打印回复 + 总耗时
# 验收：生成器用 yield 逐字产出；装饰器加了 wraps；能口述"为什么生成器适合流式输出"
# 【本题用到】def + yield 生成器、time.sleep、@装饰器 + functools.wraps、time.time、print(end="",flush=True)

# 你的代码：

# def timming(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @timming
# def fake_llm_stream(prompt):
#     start = time.time()
#     for i in f"关于「{prompt}」，我的回答是：这就是装饰器":
#         time.sleep(0.03)
#         yield i
#     print(f":耗时{time.time() - start:.3f}s")
#
# for token in fake_llm_stream("什么是装饰器"):
#     print(token, end="", flush=True)




# ============================================================
#  第三部分 · 联想微训练（只口述/写几句，不写完整代码，约10分钟）
# ============================================================
# 1. LangChain / OpenAI SDK 里的 llm.stream("你好") 返回的是一个生成器，
#    用 for token in llm.stream(...): print(token) 可以逐字打印。
#    用今天的知识说：为什么流式输出要用生成器而不是 return 一个完整字符串？
# 答：生成器是用多少调度多少，内存使用是跟随用的情况来的。而return，太吃内存
#
# 2. 装饰器和闭包是什么关系？@decorator 写在函数定义上方时，装饰器代码在什么时机执行？
#    （提示：是"定义函数那一刻"执行外层，还是"调用函数那一刻"才执行？想清楚外层和 wrapper 的区别）
# 答：装饰器一定是闭包的，装饰器外层接受一个函数作为参数，内层是要执行的部分。所以装饰器一定是闭包的。
# 外层在 "定义时" 跑一次，wrapper 在 "每次调用时" 跑
#
# 3. Q9 的生成器管道，如果第一环 numbers 产出 1 亿个数，程序会占 1 亿元素的内存吗？为什么？
# 答：不会，yield的作用，yield后面的表达式作为值返回，然后停止。知道下次调用，才会从停止位置再次开始执行
# 所以它是调依次，使用一点内存。而不是一次性占用大量内存


# ============================================================
#  提交清单（收工自查）
#  [ ] W1~W7 跟写+微调全部跑通（W7 正则了解即可）
#  [ ] Q1~Q8 完成；Q9/Q10 生成器综合尽量做
#  [ ] 每题运行输出贴在题目下方
#  [ ] 联想3题写了口述答案
#  [ ] 周末 D4 四题还债已记在待办
# ============================================================
#（注：内容由AI生成）
