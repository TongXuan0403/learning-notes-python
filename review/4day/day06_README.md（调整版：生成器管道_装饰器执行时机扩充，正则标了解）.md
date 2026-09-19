# D6 知识卡 · 模块包 + 迭代器/生成器 + 装饰器（正则仅了解）

> 2026-09-17 ｜ 配套 `day06_practice.py` ｜ 对应讲义第 12 章《模块与包》、第 13 章《高级语法》、第 15 章《正则》
> **今日重点（按权重）**：①装饰器（FastAPI/LangChain 到处是 `@`）②迭代器/生成器（对应 LLM 流式输出）
> 正则：**了解即可**，会用 `findall/sub` 提取替换、看得懂简单模式就行，不背元字符、不出大题

---

## ① 知识速整清单

### 1. 模块与包
- **模块**：一个 `.py` 文件就是一个模块
- **包**：一个含 `__init__.py` 的文件夹（Python 3.3+ 可不写，但写上更规范）
- 导入方式：`import 模块`、`from 模块 import 函数`、`import 模块 as 别名`、`from 包.模块 import 类`
- `if __name__ == "__main__":`（D5 已讲）：被 import 时不执行，直接运行时才执行
- 相对导入：`from . import 模块`（同包）、`from .. import 模块`（上一级）

### 2. 虚拟环境与 pip
- `python -m venv venv` 创建虚拟环境
- `source venv/bin/activate`（Mac/Linux）/ `venv\Scripts\activate`（Windows）激活
- `pip install 包名`、`pip freeze > requirements.txt`、`pip install -r requirements.txt`
- 虚拟环境 = 项目隔离的 Python 环境，不同项目依赖不打架

### 3. 浅拷贝 vs 深拷贝
| 方式 | 写法 | 效果 |
|---|---|---|
| 赋值 | `b = a` | 同一个对象，改 b 就是改 a |
| 浅拷贝 | `b = a.copy()` / `b = list(a)` / `b = a[:]` | 外层新对象，**内层嵌套还是共享引用** |
| 深拷贝 | `import copy; b = copy.deepcopy(a)` | 完全独立，嵌套也复制一份 |

> 坑：嵌套列表用浅拷贝，改内层会互相影响。

---

### 4. 迭代器（Iterator）⭐ 重点
- **可迭代对象（Iterable）**：list、dict、str、range、文件对象等，实现了 `__iter__`，能放进 for 循环
- **迭代器（Iterator）**：同时实现了 `__iter__`（返回自身）和 `__next__`（返回下一个值，没了抛 `StopIteration`）
- `iter(可迭代对象)` → 得到迭代器；`next(迭代器)` → 取下一个值
- iter底层 会调用__iter__   next __会调用__next__
- **for 循环本质**：先 `iter()` 拿迭代器，再反复 `next()`，遇到 `StopIteration` 就停止
- 迭代器是**一次性**的：遍历完就"耗尽"了，再 for 一遍什么都没有
- 手写迭代器模板：
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self              # 迭代器返回自身
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 没有下一个了
        self.current -= 1
        return self.current + 1
```

### 5. 生成器（Generator）⭐⭐ 最重点 —— 对应 LLM 流式输出
- **生成器函数**：函数体里用了 `yield`，调用函数时**不执行函数体**，而是返回一个生成器对象
- 每次 `next()`：执行到下一个 `yield`，把值"吐"出来并**暂停**（现场冻结）；下次 `next()` 从暂停处继续
- `return` 在生成器里表示结束（会触发 StopIteration）
- **生成器表达式**：`(x*x for x in range(10))` —— 方括号 `[...]` 是列表推导（一次性全算），圆括号 `(...)` 是生成器表达式（惰性）
- **惰性求值**：不一次性生成所有值，用一个才算一个 → **省内存**
- **生成器管道（pipeline）**：多个生成器可以串联，数据像流水线一样一环一环流过：
```python
def numbers(n):
    for i in range(1, n+1):
        yield i
def evens(it):
    for x in it:
        if x % 2 == 0:
            yield x
def squared(it):
    for x in it:
        yield x * x

for x in squared(evens(numbers(10))):  # 数据流过：取数→筛偶→平方
    print(x)
```
> 即使第一环 `numbers(1亿)`，内存里同一时刻也只有一个数，不会占 1 亿元素的内存。
- `yield from`（了解）：`yield from 另一个可迭代对象` 等价于 for 循环逐个 yield，用于生成器委托
- **AI 视角**：LLM 流式输出就是生成器——`for token in llm.stream("你好"): print(token, end="")`，token 一个一个吐，不用等整句生成完

**列表 vs 生成器内存对比**：
```python
sum([x for x in range(10**8)])   # 列表：先造 1 亿元素的列表，占几个 G 内存
sum(x for x in range(10**8))     # 生成器：逐个算，内存几乎为 0
```

### 6. 闭包（D3 复习，装饰器的基础）
- 内层函数引用外层函数的变量，外层函数返回内层函数对象
- 变量被"包"住了，多次调用共享状态
- **装饰器本质上就是一个"吃函数、吐函数"的闭包**

### 7. 装饰器（Decorator）⭐⭐ 最重点 —— 必须扎实
- **本质**：一个接收函数作为参数、返回一个新函数的函数
- **语法糖**：
```python
@decorator
def my_func():
    pass
# 上面这行 @decorator 等价于：
# my_func = decorator(my_func)
```

**执行时机（关键，容易混）**：
- `@decorator` 写在函数定义上方，**在"定义函数那一刻"外层就执行了一次**（完成"包装"，把原函数换成 wrapper）
- 之后每次**调用** `my_func()`，实际执行的是 wrapper 里的代码

**不带参装饰器模板（两层）**：
```python
def decorator(func):                    # 外层：接收被装饰的函数
    @functools.wraps(func)
    def wrapper(*args, **kwargs):       # 内层：真正替代原函数的新函数
        # ---- 前置逻辑 ----
        result = func(*args, **kwargs)  # 调用原函数
        # ---- 后置逻辑 ----
        return result
    return wrapper                      # 外层返回新函数
```
- `*args, **kwargs` 保证 wrapper 能接收原函数的任意参数，原样转发

**带参装饰器模板（三层）**：
```python
def repeat(times):                      # 最外层：接收你写的参数
    def decorator(func):                # 中间层：接收被装饰的函数
        @functools.wraps(func)
        def wrapper(*args, **kwargs):   # 最内层：替代原函数
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)                        # 等价于 greet = repeat(3)(greet)
def greet():
    print("你好")
```
> 记忆：不带参两层（收函数→wrapper），带参三层（收参数→收函数→wrapper）。

**`functools.wraps`**：
- 不加：被装饰后 `my_func.__name__` 变成 `"wrapper"`，`__doc__` 也丢了，调试混乱
- 加了：保留原函数名和文档。养成习惯，wrapper 上方一律写 `@functools.wraps(func)`

**多个装饰器叠加（洋葱模型）**：
```python
@A
@B
def f(): ...
# 等价于 f = A(B(f))
# 执行顺序：B 先包装（靠近函数的先包），调用时 A前置 → B前置 → f → B后置 → A后置
```

### 8. 正则表达式 re（【了解】会提取/替换即可）
- 只需先记住两个最常用函数：

| 函数 | 作用 | 返回 |
|---|---|---|
| `re.findall(pattern, s)` | 找出**所有**匹配 | 列表 |
| `re.sub(pattern, repl, s)` | 替换匹配内容 | 新字符串 |

- 看得懂的几个元字符（不用背，用到查）：
  - `\d` 一个数字、`\w` 字母数字下划线、`+` 前面的出现1次或多次、`*` 0次或多次
  - `[3-9]` 3到9中的一个字符、`{9}` 重复9次
- 一律用原始字符串 `r'...'`，避免反斜杠转义
```python
import re
text = "电话13812345678，备用13987654321"
print(re.findall(r'1[3-9]\d{9}', text))        # ['13812345678','13987654321']
print(re.sub(r'\d+', '#', text))               # 电话#，备用#
```
> 以后真要写复杂正则（邮箱/URL/清洗文本）再查文档，现阶段知道"正则能干提取和替换、findall/sub 怎么调"就够。

---

## ② 方法地图（按"想干什么"查）

### 导入与包
| 想干什么 | 写法 | 易混点 |
|---|---|---|
| 导入整个模块 | `import math` | 用 `math.sqrt()` |
| 导入模块中特定函数 | `from math import sqrt` | 直接用 `sqrt()` |
| 起别名 | `import numpy as np` | |
| 导入包中模块 | `from sklearn.linear_model import LinearRegression` | |

### 拷贝
| 想干什么 | 写法 | 嵌套是否独立 |
|---|---|---|
| 引用同一个对象 | `b = a` | ❌ 完全共享 |
| 浅拷贝 | `b = a.copy()` / `b = a[:]` | ❌ 内层共享 |
| 深拷贝 | `import copy; b = copy.deepcopy(a)` | ✅ 完全独立 |

### 迭代器与生成器 ⭐
| 想干什么 | 写法 | 说明 |
|---|---|---|
| 手写迭代器类 | 实现 `__iter__`（返回self）+ `__next__` | `__next__` 末尾抛 `StopIteration` |
| 生成器函数 | 函数内用 `yield` | **调用不执行**，返回生成器对象 |
| 生成器表达式 | `(x for x in range(10))` | 圆括号，惰性、省内存 |
| 取下一个值 | `next(生成器)` | 没了抛 `StopIteration` |
| 遍历生成器 | `for x in 生成器:` | 自动处理 StopIteration |
| 生成器串联 | 在生成器里 `for x in 另一个生成器: yield ...` | 管道，数据逐环流过 |
| 委托生成器 | `yield from 可迭代对象` | 了解即可 |

### 装饰器 ⭐
| 想干什么 | 写法 | 说明 |
|---|---|---|
| 不带参装饰器 | 两层：`def deco(func): def wrapper(*args,**kwargs)` | 外层收函数，内层包逻辑 |
| 应用装饰器 | `@deco` 写在函数上方 | 等价 `func = deco(func)`，定义时执行一次 |
| 保留原函数名 | wrapper 上方写 `@functools.wraps(func)` | 不加则 `__name__` 变 wrapper |
| 带参装饰器 | 三层：`deco(arg)` → `inner(func)` → `wrapper` | 等价 `func = deco(arg)(func)` |
| 多个叠加 | `@A` 换行 `@B` | 从下往上包：`f = A(B(f))` |
| 原样转发参数 | wrapper 里写 `func(*args, **kwargs)` | 适配任意参数列表 |

---

## ③ 最小示例（热身 W1~W7 照这些敲）

### 最小示例 1：模块导入（对应 W1）
```python
import math
from math import sqrt
print(math.pi)
print(sqrt(16))
```

### 最小示例 2：浅拷贝 vs 深拷贝（对应 W2）
```python
import copy
a = [[1, 2], [3, 4]]
b = a.copy()              # 浅拷贝
c = copy.deepcopy(a)      # 深拷贝
a[0][0] = 99
print(b[0][0])            # 99（内层共享，被影响）
print(c[0][0])            # 1（完全独立）
```

### 最小示例 3：手写迭代器（对应 W3）
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(3):     # 3, 2, 1
    print(n)
```

### 最小示例 4：生成器（对应 W4）
```python
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield b            # 暂停，返回 b
        a, b = b, a + b

for x in fib_gen(5):       # 1, 1, 2, 3, 5
    print(x)
```

### 最小示例 5：最简单装饰器（对应 W5）
```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.5)
slow()                     # slow 耗时 0.5001s
```

### 最小示例 6：带参装饰器 + wraps（对应 W6）
```python
import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet():
    print("你好")
greet()                    # 你好 你好 你好
print(greet.__name__)      # greet（有 wraps 才保留原名）
```

### 最小示例 7：正则（对应 W7，了解）
```python
import re
text = "联系电话：13812345678"
print(re.findall(r'1[3-9]\d{9}', text))   # ['13812345678']
print(re.sub(r'\d+', '***', text))        # 联系电话：***
```

---

## ④ 今日易错点

1. **生成器函数调用不执行**：`gen = fib_gen(5)` 只是创建生成器对象，函数体一行都没跑；要 `next(gen)` 或 `for` 才执行。
2. **迭代器一次性**：遍历完就耗尽，再 for 一遍是空的；列表可以反复遍历。
3. **装饰器忘加 `@functools.wraps`**：被装饰函数的 `__name__` 变成 `wrapper`，调试和文档会乱。
4. **带参装饰器少一层**：不带参两层（deco→wrapper），带参三层（deco(arg)→inner(func)→wrapper）。
5. **执行时机混淆**：`@deco` 在函数**定义时**就执行外层完成包装；wrapper 里的逻辑在函数**调用时**才执行。
6. **多个装饰器顺序**：`@A` `@B` `def f()` 等价 `f = A(B(f))`，B 先包、A 后包，调用时 A 先进入。
7. **浅拷贝嵌套共享**：`b = a.copy()` 后改 `b[0][0]`，a 也会变——嵌套结构必须用 `deepcopy`。
8. **正则（了解层面）**：用 `r''` 原始字符串；`findall` 返回所有匹配的列表。

---

## ⑤ AI 开发视角

- **装饰器（最高频）**：FastAPI 的 `@app.get("/")`、`@app.post`，LangChain 的 `@tool`、各种追踪 `@observe`、重试 `@retry`、缓存 `@lru_cache` 全是装饰器——写 AI 应用每天都在写 `@`，必须能手写不带参和带参两种。
- **生成器（核心）**：LLM 流式输出 `for token in llm.stream("你好"): print(token, end="")` 就是生成器——token 逐个吐，不一次性加载整段回复，省内存、首字延迟低、体验好。RAG 里分批读文档、大数据逐行处理也是同一套。
- **迭代器**：`for chunk in response.iter_content()`（流式下载）、`for row in cursor`（数据库逐行取）都是迭代器协议。
- **模块包**：以后每个 AI 项目都是一个包，`from my_app.llm import ChatClient` 这种导入每天都在写。
- **正则（够用即可）**：从用户输入提取手机号/邮箱/URL、清洗文本时用，复杂模式查文档，不需要花大量时间背语法。
