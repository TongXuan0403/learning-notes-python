# D4 知识卡 · 文件操作 + 异常 + JSON

> 2026-09-16 ｜ 配套 `day04_review.py` ｜ 对应讲义第 5、7 章

---

## ① 知识速整清单

### 1. 文件操作
- 文本文件 vs 二进制文件
- 绝对路径 vs 相对路径
- `open(路径, mode, encoding='utf-8')`
- 为什么要 close：不关会占资源
- **with 关键字（重点）**：自动关闭，异常也关，以后一律用 with

**mode 模式表**：
| 模式 | 说明 | 文件不存在时 |
|---|---|---|
| `'r'` | 读（默认） | 报错 |
| `'w'` | 覆盖写（一打开就清空！） | 新建 |
| `'a'` | 追加写 | 新建 |
| `'b'` | 二进制模式（如 `'rb'`/`'wb'`） | — |

**读写方法**：
| 方法 | 说明 | 易混点 |
|---|---|---|
| `f.write(s)` | 写字符串 | 返回字符数，不自动换行 |
| `f.writelines(列表)` | 写多行 | 不自动加 `\n`，自己拼好 |
| `f.read()` | 全读成一个大字符串 | 小文件用 |
| `f.readline()` | 读一行 | 含行尾 `\n` |
| `f.readlines()` | 读所有行成列表 | 一次性进内存 |
| `for line in f:` | 逐行读（首选） | 大文件/日志不爆内存 |

### 2. 异常处理
- 语法错误 vs 运行时异常
- **try-except-else-finally 结构**：
  - `try`：试一段可能出错的代码
  - `except 类型:`：捕获特定异常
  - `else`：没出错才执行
  - `finally`：无论如何都执行（常用于关资源）

**必认的 6 个异常**：
- `FileNotFoundError`：文件不存在
- `KeyError`：字典没这个键
- `IndexError`：列表越界
- `ValueError`：值非法（如 `int('abc')`）
- `TypeError`：类型不对
- `ZeroDivisionError`：除以 0

**抛出与断言**：
- `raise ValueError("消息")`：主动抛错
- `assert 条件, "提示"`：调试断言，False 抛 AssertionError

**异常传递**：函数内不捕获会一层层往上抛

### 3. JSON 模块（四兄弟）
| 函数 | 作用 | 记忆 |
|---|---|---|
| `json.dumps(obj)` | Python 对象 → JSON 字符串 | s = string |
| `json.loads(s)` | JSON 字符串 → Python 对象 | s = string，输入是字符串 |
| `json.dump(obj, f)` | Python 对象 → 写入 JSON 文件 | 没 s，参数里给文件对象 |
| `json.load(f)` | 读取 JSON 文件 → Python 对象 | 没 s，从文件对象读 |

**常用参数**：`ensure_ascii=False`（中文不转 `\uXXXX`）、`indent=2`（缩进美化）

**类型对应**：dict↔object、list↔array、True↔true、None↔null

---

## ② 方法地图

| 想干什么 | 写法 | 易混点 |
|---|---|---|
| 读小文件 | `with open('a.txt', 'r', encoding='utf-8') as f: data = f.read()` | 必须指定 encoding |
| 读大文件/日志 | `for line in f: line = line.strip()` | 逐行读不爆内存 |
| 写文件 | `with open('a.txt', 'w', encoding='utf-8') as f: f.write(s)` | `'w'` 一打开就清空！ |
| 追加写日志 | `with open('a.log', 'a', encoding='utf-8') as f: f.write(...)` | `'a'` 只追加不清空 |
| 捕获特定异常 | `except ValueError as e: print(e)` | 别写裸 `except:` |
| 主动抛错 | `raise ValueError("不能小于0")` | 带错误消息 |
| 字典转 JSON 字符串 | `json.dumps(d, ensure_ascii=False, indent=2)` | 有 s |
| JSON 字符串转字典 | `json.loads(s)` | 有 s，输入是字符串 |
| 字典写入 JSON 文件 | `json.dump(d, f, ensure_ascii=False, indent=2)` | 没 s，给文件对象 |
| 从 JSON 文件读字典 | `d = json.load(f)` | 没 s，从文件对象读 |
