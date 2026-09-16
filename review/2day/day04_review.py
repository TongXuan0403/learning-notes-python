"""
文件操作 + 异常 + JSON


#文件概念
#   在计算机中，文件是存储在磁盘上的数据集合

文件分类
   1.纯文本文件     有统一的编码，可以被看做存储在磁盘上的长字符串。
       编码格式常见的有ASCII、ISO-8859-1、GB2312、GBK、UTF-8、UTF-16等
   2.二进制文件     没有统一的字符编码，直接由0与1组成。
        如图片文件（jpg、png），视频文件（avi）等

路径
    1.相对路径      从当前位置到指定位置的路径
        ./ 代表当前路径。../ 代表上一级路径
    2.绝对路径      从根目录到指定位置的路径
        如：E:/Hello/hello.py


打开与关闭
    打开  用open()打开或者创建文件
        语法
            open(文件名,模式)
            f = open("test.txt","w")
模式	说明
r	读写方式：只读，文件若不存在会报错。默认此模式
w	读写方式：写入，写入前清空原有数据。文件不存在会创建文件
a	读写方式：追加写入，在原有数据后追加，文件不存在会创建文件
x	读写方式：创建新文件并写入，文件若已存在会报错
b	编码方式：以二进制打开。一般用于非文本文件如图片等
t	编码方式：以文本模式打开，默认此模式
+	能读能写

    关闭
        f.close()


读写
    写入数据
        1.先打开文件
        2.写入数据
        3.关闭文件
        f = open("test.txt","w")
        f.write("sdf")
        f.close()

    读取数据
        1.read([size])  从文件中读取数据，size 表示要从文件中读取的数据的长度,没有size默认读取全部
            f.read(3)
        2.readline([size])      从文件中读取整行数据，也可以通过 size 设置读取数据的长度
            f.readline(3)
        3.readlines([size])     读取所有行并返回列表，若给定 size>0，返回总和大约为 size 字节的行， 实际读取值可能比 size 大。
            f.readlines(3)


文件拷贝
    # source_file : 源文件路径
    # dest_file: 目的地文件路径
def copyFile(source_file_path,dest_file__path):
    # 打开源文件
    source_file = open(source_file_path, 'rb')
    # 打开目的地文件
    dest_file = open(dest_file__path, 'wb')
    # 读取源文件中的内容
    content = source_file.read(1024)
    while content:
        # 将读取到的数据写入到目的地
        dest_file.write(content)
        # 继续从源文件读取数据
        content = source_file.read(1024)
    # 关闭源文件
    # 关闭目的地文件
    dest_file.close()


def copyFile(sc_file,ds_file):
    s_file = open(sc_file, 'rb')
    content = s_file.read()

目标地址
    d_file = open(ds_file, 'wb')
写入目标地
    d_file.write(content)
关闭
    sc_file.close()
    ds_file.close()


优化
def copyFile(sc_file,ds_file):
    s_file = open(sc_file, 'rb')
    d_file = open(ds_file, 'wb')

    content = s_file.read(1024)

    while content:
        写
        d_file.write(content)
        在读取
        content = s_file.read(1024) 分批读取
    d_file.close()




错误与异常
概念
    错误：语法等问题
    异常：语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
    异常进行处理：出现错误的时候提供解决方案，不终止程序，可以让程序继续执行。相当于给了第二方案

语法

异常处理    try-except-else-finally
try except
    try:
        可能发生异常的代码
    except 异常类型1 as 变量名1:
        异常处理的代码
    except 异常类型2 as 变量名2:
            异常处理的代码
    except(异常类型3, 异常类型4, 异常类型5) as 变量名3:
        异常处理的代码
    except:
        异常处理的代码

else    如果try中代码没有发生异常，将执行 else 中的代码。
    try:
        可能发生异常的代码
    except 异常类型1 as 变量名1:
        异常处理的代码
    except 异常类型2 as 变量名2:
        异常处理的代码
    else:
        没有异常时执行的代码

finally
可选地，放在最后。无论是否发生异常都会执行的代码，
通常用于执行一些必须要进行的清理操作，例如关闭文件、释放资源

    try:
        可能发生异常的代码
    except 异常类型1 as 变量名1:
         异常处理的代码
    except 异常类型2 as 变量名2:
        异常处理的代码
    else:
        没有异常时执行的代码
    finally:
        无论是否发生异常都会执行的代码


抛出异常    raise   assert断言

raise
def add(num1,num2):
    isinstance()判断是否是int
    if isinstance(num1,int) and isinstance(num2,int):
        return num1 + num2
    else:
        raise TypeError("类型错误")

assert 表达式 [,异常描述]
等价于：
if not 表达式:
    raise AssertionError([异常描述])


自定义异常  没有合适的异常
class MyError(Exception):
    # def __init__(self, value):
    #     self.value = value
    #
    # def __str__(self):
    #     return repr(self.value)
    pass 上面和pass差不多


异常传递
try 嵌套或函数嵌套时。一层一层向外传递

try:
    try:
        try:
            print(3/0)
        except NameError:
            print("1")
    except ValueError:
        print("2")
except ZeroDivisionError:
    print("3")



with关键字
    语法
        with expression as variable:
            # 代码块
expression：通常是一个对象或函数调用，该对象需要是一个上下文管理器，
即实现了 __enter__和__exit__方法。
(上下文管理器)

1. 进入 `with` → `__enter__`
2. 执行内部代码（可以报错）
3. 退出 `with` → **一定会执行 `__exit__`** ✨ 这是核心价值
4. `__exit__` 的返回值：返回`True`代表捕获并吞掉异常；返回 False，异常继续向外抛出

variable：是可选的，用于存储expression的__enter__方法的返回值







- **开做前**：①先写样例明确输入输出 ②中文伪代码写注释 ③查下方方法地图 ④最简样例先跑通
- **卡住**：15 分钟规则，来问我只给方向
- **今日盯防**：`w` 模式会清空原文件；`dump/dumps`、`load/loads` 谁操作字符串谁操作文件
- **收工三问**：输出点齐吗 / ⚠ 标了吗 / 题眼写了吗

"""
import json

# ③ 题目
# **Q1【基础】写对话记录**
# 题目：程序内准备列表 `["用户:你好","AI:你好，有什么可以帮您","用户:讲个笑话"]`，写入 `chat.txt`，每条独占一行；
# 再用**追加模式**加第 4 行 `"AI:好的..."`。
# 【本题用到】open（w/a）、write 或 writelines、`'\n'`
# 验收：文件里共 4 行；思考：为什么前 3 条用 w、第 4 条用 a，顺序反了会怎样？

# list1 = ["用户:你好","AI:你好，有什么可以帮您","用户:讲个笑话"]
# f = open("chat.txt","w",encoding="utf-8")
# for i in list1:
#     f.write(i + "\n" )
#
# f.close()
# with open("chat.txt","a",encoding="utf-8") as f:
#     f.write("AI:好的...")
#
# with open("chat.txt","w",encoding="utf_8") as f:
#     n = [i +"\n" for i in list1]
#     f.writelines(n)
# with open("chat.txt","a",encoding="utf-8") as f:
#     f.write("AI:好的...")




# **Q2【基础】读文件加行号**
# 题目：读取 Q1 的 chat.txt，先一次性 `read()` 打印；
# 再改成逐行读，输出 `1. 用户:你好` 这种带行号格式。
# 输入：chat.txt；输出示例：`1. 用户:你好`；边界：去掉每行末尾换行。
# 【本题用到】open (r)、read、`for line in f`、enumerate、strip

# with open("chat.txt","rt",encoding="utf-8") as f:
#     print(f.read())
# with open("chat.txt","rt",encoding="utf-8") as f:
#     for id,line in enumerate(f,start=1):
#
#         print(f"{id}.{line.rstrip('\n')}")

        #strip()删除字符串首尾所有空白字符：换行`\n`、空格、制表符`\t`     常用
        #rstrip()只删除末尾的换行 `\n`，开头空格保留！  读文件用


# **Q3【基础】安全数字输入**
# 题目：循环让用户输入，输入数字就打印它的平方；输入非数字**不崩溃**，提示 "请输入有效数字" 后继续；输入 `q` 退出。
# 示例：输入 `abc` → 重新输入；输入 `5` → 打印 25；输入 `q` → 结束。
# 【本题用到】while、try/except ValueError、int、break
# while True:
#     try:
#         num = input()
#         if len(num) == 1 and num == "q":
#             break
#         print(int(num) ** 2)
#
#     except ValueError:
#         print("请输入有效数字")




    # **Q4【基础】文件不存在不崩溃**
# 题目：写 `read_first_line(path)`：文件存在返回第一行内容；
# 不存在返回字符串 `"文件不存在"`；其他错误不用管。
# 【本题用到】try/except FileNotFoundError、with open、readline 或 for

# def read_first_line(path):
#     try:
#         with open(path, "rt",encoding="utf-8") as f:
#             return f.readline().strip()
#     except FileNotFoundError:
#         return "文件不存在"
# read_first_line("chat.txt")
# 函数像一台自动售货机，`return` 是出货口，`print` 只是机器上亮了个灯


# **Q5【进阶・AI 场景】解析一次大模型返回**
# 题目：给定字符串（模拟 API 响应）：
#
# ```
# response = '{"code":200,"msg":"success","data":{"answer":"Python很好学","tokens":128},"choices":[1,2,3]}'
# ```
# 要求：①转成字典；②取出 answer 和 tokens；③把 code 改成 201，新增字段 `"model":"qwen"`；
# ④转回**中文正常、缩进 2 格**的 JSON 字符串打印；⑤存成 `response.json` 再读回来，确认 code 是 201。
# 【本题用到】json.loads/dumps/dump/load、字典取值与赋值、ensure_ascii=False、indent=2

# response = '{"code":200,"msg":"success","data":{"answer":"Python很好学","tokens":128},"choices":[1,2,3]}'
#
# dict1=json.loads(response)
#
# print(dict1)
# print(dict1["data"]["answer"])
# print(dict1["data"].get("tokens"))
# print(dict1.get("data").values())
# # print(dict1.get("data"))
# dict1["code"] = 201
# dict1["model"] = "qwen"
# print(dict1)
# str1 = json.dumps(dict1, ensure_ascii=False,indent=2)
# print(str1)
#
# with open("response.json","w",encoding="utf-8") as f:
#     json.dump(dict1,f,ensure_ascii=False,indent=2)
# with open("response.json","r",encoding="utf-8") as f:
#     print(json.load(f))



# **Q6【进阶】训练日志统计**
# 题目：自己造一个 `access.log`，写 10 行，
# 每行 `"时间 级别 消息"` 格式，其中 INFO 5 行、WARNING 3 行、ERROR 2 行；
# 读文件统计各级别次数输出字典 `{'INFO':5,...}`，并把所有 ERROR 行另存到 `error.log`。
# 边界：遇到空行跳过。
# 【本题用到】open 读写、`for line in f`、split、字典计数 `d[k]=d.get(k,0)+1`、write

# with open("access.log","w",encoding="utf-8") as f:
#     for i in range(10):
#         str1 = input().strip()
#         f.write(str1+"\n")
# with open("access.log","r",encoding="utf-8") as f:
#     d={}
#     l = []
#     for line in f:
#         lines = f.readline()
#         j1 = lines.split()
#         l.append(j1)
#
#     for line in j1:
#         if line.isalpha():
#             k = line.lower()
#             if k.islower():
#                 d[k] = d.get(k,0)+1
#     print(d)




# **Q7【进阶】异常四段结构**
# 题目：写 `safe_div(a,b)`，当 b==0 时 `raise ValueError("除数不能为0")`；
# 调用处用 try-except-else-finally 完整结构：except 里用 `as e` 打印错误，else 里打印成功结果，
# finally 打印 `"计算结束"`。分别用 (10,2)、(10,0) 调用，把两次完整输出贴上来，并说明 else 和 finally 各在什么时候执行。
# 【本题用到】raise、try/except...as e、else、finally

# def safe_div(a,b):
#     try:
#         if b == 0:
#             raise ValueError("除数不能为0")
#     except ValueError as e:
#         return e
#     else:
#         return a / b
#     finally:
#         return "计算结束"

# safe_div(10,2)
# safe_div(10,0)

# 并说明 else 和 finally 各在什么时候执行
# else是没有异常时执行  finally是只要结束就执行


# **Q8【进阶・AI 场景】对话历史持久化**
# 题目：消息历史形如 `[{"role":"user","content":"你好"},{"role":"assistant","content":"你好呀"}]`。
# 写两个函数：`save_history(history, path)` 存成 JSON 文件；
# `load_history(path)` 读回，**文件不存在时返回空列表 `[]` 而不是报错**。
# 然后模拟：读取历史→追加一轮 user→追加一轮 assistant→保存；再跑一次同样流程，验证历史累积到 4 条不丢。
# 【本题用到】json.dump/load、with open、except FileNotFoundError、list.append
# his=[{"role":"user","content":"你好"},{"role":"assistant","content":"你好呀"}]

# 先读（把文件中的内容放入列表中） - 再存放（把新添加的数据和旧数据纯到文件中） -在读

# def load_history(path):
#     try:
#         with open(path,"r",encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []
#
# def save_history(history, path):
#     with open(path,"w",encoding="utf-8") as f:
#         json.dump(history,f,ensure_ascii=False)
#
# data = load_history("history.json")
# print(data)
#
# data.append({"role":"user","content":"你好"})
#
# save_history(data,"history.json")
#
# data = load_history("history.json")
# print(data)
#
# data.append({"role":"assistant","content":"你好呀"})
#
# save_history(data,"history.json")


# **Q9【综合】成绩存档（串联 D2~D4）**
# 题目：复用你的成绩录入（`姓名 分数`，q 结束）；
# 程序启动时先读 `scores.json`（不存在就从空字典开始），新录入的合并进去，结束时存回；最后输出按分数降序的完整名单。
# 验收：连续运行两次，第二次能看到第一次录的人。
# 【本题用到】njson、iput 循环、字典、sorted+lambda、FileNotFoundError


# def sc():
#     try:
#         with open("scores.json", "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
# sc()
# dic = sc()
#
# while True:
#     data = input().split()
#     if len(data) == 1 and data[0] == "q":
#         break
#     name,age = data
#     dic[name] = int(age)
# print(sorted(dic.items(), key=lambda item: -item[1]))
# with open("scores.json", "w", encoding="utf-8") as f:
#     json.dump(dic, f, ensure_ascii=False)





# **Q10【选做】大文件词频 Top5**
# 题目：逐行（不许 read 一次性读）统计一个文本文件里每个单词出现次数（不区分大小写），输出出现最多的前 5 个；
# 一句话回答：为什么大文件不能用 read ()。#大文本内容多，read()不限制会直接读完
#
# 为什么不能 read ()" 补一句关键的：**一次性载入内存，大文件会把内存撑爆；逐行读时内存里始终只有一行**。
#
# 【本题用到】`for line in f`、split、lower、字典计数、sorted+lambda、切片 `[:5]`
# d = {}
# with open("chat.txt", "r",encoding="utf-8") as f:
#     for line in f:
#         l = line.lower().split()
#         for i in l:
#             d[i] = d.get(i,0) + 1
#     print(sorted(d.items(), key=lambda x: -x[1])[0:5])     #sorted返回的是元组










# ## ④ 联想微训练（只口述，10 分钟）
#
# 1. 程序要连续处理 1000 条大模型请求，某一条超时 / 返回坏 JSON 都不能让整个程序崩 —— 用什么结构？
# 哪些异常该捕获、哪些（比如代码写错的 TypeError）不该捕获？
"""
用try-except
`FileNotFoundError` 文件不存在
`KeyError` 字典没这个键
`IndexError` 列表越界
`ValueError` 值非法（如 `int('abc')`）
`TypeError` 类型不对
`ZeroDivisionError` 除以 0。
捕获
"""




# 2. 怎么一秒记住 `dumps/dump`、`loads/load` 谁操作字符串、谁操作文件？
"""
带s的都是处理数据
不带s都是处理文件
"""


# 3. 为什么大文件推荐 `for line in f` 而不是 `readlines()`？从内存角度说一句。
"""
readlines()是一次性访问内存
for line in f 是遍历，一层一层去访问数据
"""


