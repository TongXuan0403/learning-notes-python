# D6 知识卡 · 模块包 + 高级语法 + 正则

> 2026-09-17 ｜ 配套 `day06_practice.py` ｜ 对应讲义第 12 章《模块与包》、第 13 章《高级语法》、第 15 章《正则》
> 重点：装饰器（FastAPI/LangChain 到处是 `@`）、生成器（对应 LLM 流式输出）

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

### 4. 迭代器（Iterator）
- 迭代器协议：实现 `__iter__`（返回自身）和 `__next__`（返回下一个值，没了抛 `StopIteration`）
- `iter(可迭代对象)` → 得到迭代器；`next(迭代器)` → 取下一个
- 可迭代对象：list、dict、str、range、文件对象等（实现了 `__iter__`）
- for 循环本质：先 `iter()` 拿迭代器，再反复 `next()`，遇到 `StopIteration` 停止

### 5. 生成器（Generator）—— 对应 LLM 流式输出
- 生成器函数：函数里用 `yield` 而不是 `return`，调用时**不执行函数体**，返回一个生成器对象
- 每次 `next()` 执行到下一个 `yield`，暂停并返回值；下次 `next()` 从暂停处继续
- 惰性求值：不一次性生成所有值，用一个算一个，**省内存**
- 生成器表达式：`(x*x for x in range(10))`（方括号是列表推导，圆括号是生成器表达式）
- **AI 视角**：LLM 流式输出（token 一个一个吐）就是生成器的典型应用——`for token in llm.stream("你好"): print(token, end="")`

生成器对象创建方式：
推导式
gen = (i for i in range(5)) 
print(next(gen))
for i in gen 
    print(i)
函数     生成器函数    yield 返回数据
def fibo():
    a,b=0,1
    while True
        a,b = b,a+b
        yield b


### 6. 闭包（D3 复习）
- 内层函数引用外层函数的变量，外层函数返回内层函数对象
- 变量被"包"住了，多次调用共享状态
- 装饰器就是闭包的应用

### 7. 装饰器（Decorator）—— 必须扎实
- **本质**：一个接收函数作为参数、返回一个新函数的函数（闭包的应用）
- **语法糖**：`@装饰器名` 写在函数定义上方，等价于 `函数 = 装饰器(函数)`
- 不带参装饰器模板：
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 前置操作
        result = func(*args, **kwargs)
        # 后置操作
        return result
    return wrapper

@decorator
def my_func():
    pass
```
- 带参装饰器：再多包一层（外层接收参数，中间层接收函数，内层 wrapper）
- `functools.wraps(func)`：装饰后保留原函数的 `__name__`、`__doc__` 等元信息（不加会变成 wrapper）
- 多个装饰器叠加：**从下往上执行**（靠近函数的先执行），类似洋葱模型

### 8. 正则表达式 re
- 常用函数对比：

| 函数 | 作用 | 返回 |
|---|---|---|
| `re.match(pattern, s)` | 从**开头**匹配 | 匹配对象或 None |
| `re.search(pattern, s)` | 找**第一个**匹配 | 匹配对象或 None |
| `re.findall(pattern, s)` | 找**所有**匹配 | 列表 |
| `re.sub(pattern, repl, s)` | 替换 | 新字符串 |
| `re.split(pattern, s)` | 按模式分割 | 列表 |

- 常用元字符：
  - `.` 任意字符（除换行）、`*` 0次或多次、`+` 1次或多次、`?` 0次或1次
  - `\d` 数字、`\w` 字母数字下划线、`\s` 空白、`\b` 单词边界
  - `[abc]` 字符集、`[^abc]` 非字符集、`(abc)` 分组、`a|b` 或
  - `{n,m}` 重复 n 到 m 次、`^` 开头、`$` 结尾
- 贪婪 vs 非贪婪：`.*` 贪婪（尽可能多），`.*?` 非贪婪（尽可能少）
- 匹配对象 `.group()` 取匹配内容，`.group(1)` 取第一个分组

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

### 迭代器与生成器
| 想干什么 | 写法 | 说明 |
|---|---|---|
| 手写迭代器类 | 实现 `__iter__` + `__next__` | `__next__` 末尾抛 `StopIteration` |
| 生成器函数 | 函数内用 `yield` | 调用返回生成器对象，不执行 |
| 生成器表达式 | `(x for x in range(10))` | 圆括号，惰性 |
| 取下一个 | `next(生成器)` | 没了抛 `StopIteration` |
| 遍历生成器 | `for x in 生成器:` | 自动处理 StopIteration |

### 装饰器
| 想干什么 | 写法 | 说明 |
|---|---|---|
| 最简单装饰器 | `def deco(func): def wrapper(*args,**kwargs): ...; return wrapper` | 外层收函数，内层包逻辑 |
| 应用装饰器 | `@deco` 写在函数上方 | 等价于 `func = deco(func)` |
| 保留原函数元信息 | `import functools; @functools.wraps(func)` 写在 wrapper 上方 | 不加则 `func.__name__` 变成 wrapper |
| 带参数装饰器 | 再多包一层：`def deco(arg): def inner(func): def wrapper...` | 三层嵌套 |
| 多个装饰器叠加 | `@deco1` `@deco2` 连续写 | 执行顺序：从下往上（deco2 先包，deco1 再包） |

### 正则
| 想干什么 | 写法 | 说明 |
|---|---|---|
| 找所有手机号 | `re.findall(r'1[3-9]\d{9}', text)` | 原始字符串 r'' 避免转义 |
| 找所有邮箱 | `re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)` | |
| 替换 | `re.sub(r'\d+', '***', text)` | 把数字替换成 *** |
| 提取分组 | `m = re.search(r'(\d{4})-(\d{2})', s); m.group(1)` | group(1) 第一组 |
| 非贪婪匹配 | `re.search(r'<.*?>', html)` | `.*?` 尽可能少 |

---

## ③ 最小示例（热身 W1~W7 照这些敲）

### 最小示例 1：模块导入（对应 W1）
```python
import math
from math import sqrt
import numpy as np
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

### 最小示例 7：正则（对应 W7）
```python
import re
text = "联系电话：13812345678，邮箱：test@example.com"
phones = re.findall(r'1[3-9]\d{9}', text)
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
print(phones)              # ['13812345678']
print(emails)              # ['test@example.com']
```

---

## ④ 今日易错点

1. **生成器函数调用不执行**：`gen = fib_gen(5)` 只是创建生成器对象，函数体一行都没跑；要 `next(gen)` 或 `for` 才执行。
2. **装饰器忘加 `@functools.wraps`**：被装饰函数的 `__name__` 变成 `wrapper`，调试和文档会乱。
3. **带参装饰器少一层**：不带参是两层（deco→wrapper），带参是三层（deco(arg)→inner(func)→wrapper），别搞混。
4. **多个装饰器执行顺序**：`@A` `@B` `def f()` 等价于 `f = A(B(f))`，B 先执行，A 后执行——**从下往上**。
5. **浅拷贝嵌套共享**：`b = a.copy()` 后改 `b[0][0]`，a 也会变——嵌套结构必须用 `deepcopy`。
6. **正则用原始字符串**：`r'\d+'` 而不是 `'\\d+'`，r 前缀避免反斜杠转义地狱。
7. **`re.match` 只匹配开头**：要在字符串中间找用 `re.search` 或 `re.findall`。

---

## ⑤ AI 开发视角

- **装饰器**：FastAPI 的 `@app.get("/")`、LangChain 的 `@tool`、`@observe` 全是装饰器——你以后写 AI 应用每天都在写 `@`。
- **生成器**：LLM 流式输出 `for token in llm.stream("你好"): print(token, end="")` 就是生成器——token 一个一个吐，不一次性加载全部回复，省内存、用户体验好。
- **迭代器**：`for chunk in response.iter_content()`（requests 流式下载）、`for row in cursor`（数据库逐行取）都是迭代器协议。
- **正则**：从用户输入提取结构化信息（手机号/邮箱/URL）、清洗文本、提取 JSON 字段——AI 应用前后处理高频使用。
- **模块包**：你以后写的每个 AI 项目都是一个包，`from my_app.llm import ChatClient` 这种导入每天都在写。
