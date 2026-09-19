# D7 知识卡：进程与线程（对应《Python2.0》第 14 章）+ 第 1 周周测

> 今天是**周测日**。范围严格限定在 Python 讲义第 14 章「进程与线程」：进程 `Process`、进程池 `Pool`、线程 `Thread`、线程池 `ThreadPoolExecutor`、互斥锁 `Lock`、GIL、进程/线程选型。
>
> **协程（async/await）不在 Python 讲义里**，它属于《FastAPI&SQLAlchemy》第 1 章，已安排到 9/25 FastAPI 阶段正式学（学完立刻用在接口里），今天不碰。
>
- 🟥 核心（独立手写）：线程池并发、互斥锁、本周旧知识周测、D4 换皮复测（JSON 持久化/异常分层/return）
- 🟧 会用（能跑通、能改参数）：`threading.Thread`、`multiprocessing.Process`、进程池 `Pool.map`
- 🟨 了解（建立认知）：进程通信 `Queue`、`apply_async`、GIL 原理细节、死锁概念（讲义未展开，知道"多把锁互相等"即可）

---

## 一、进程 vs 线程（先建立概念）

- **进程**：操作系统**资源分配**的基本单位，一个运行中的程序就是一个进程，有**独立内存**，互不干扰，一个崩了一般不连累别人；创建开销大。
- **线程**：CPU **调度执行**的基本单位，一个进程至少一个线程，线程**共享进程内存**，创建开销小；一个线程崩了可能拖垮整个进程。

| 对比项 | 进程 | 线程 |
|---|---|---|
| 内存/资源 | 独立地址空间，互不共享 | 共享所属进程的内存 |
| 创建/切换开销 | 大 | 小 |
| 通信 | 麻烦（Queue/管道/共享内存） | 简单（直接读写共享变量，但要加锁） |
| 稳定性 | 一个崩不影响别的 | 一个崩可能拖垮整个进程 |
| 适合 | **CPU 密集**、要隔离 | **IO 密集**、要共享数据 |

---

## 二、多线程 `threading`（🟧 会用）

```python
import threading, time

def worker(name):
    for i in range(5):
        print(name, i)
        time.sleep(0.2)

t1 = threading.Thread(target=worker, args=("线程A",))
t2 = threading.Thread(target=worker, args=("线程B",))
t1.start(); t2.start()   # start：启动，开始并发
t1.join();  t2.join()    # join：主线程在这等，直到它结束
print("全部完成")
```

- `Thread(target=函数, args=(元组,), name=...)`；`args` 必须是**元组**，一个参数也要带逗号 `(x,)`。
- `start()` 启动、`join()` 等待。**只 start 不 join，主线程可能提前结束**。
- 也可以继承 `threading.Thread`、重写 `run()`（讲义有，认识即可）。

### 线程池 `ThreadPoolExecutor`（最常用）

```python
import concurrent.futures, time

def call_api(name, seconds):
    time.sleep(seconds)          # 模拟网络等待（IO）
    return f"{name}结果"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    futs = [pool.submit(call_api, n, s) for n, s in [("A",1),("B",1),("C",2)]]
    results = [f.result() for f in futs]   # result() 取返回值，顺序=提交顺序
print(results)   # 总耗时≈2s（最慢那个），不是 4s
```

- `submit(fn, *args)` 返回一个 `Future`；`future.result()` 取结果（任务里抛的异常也会在 `.result()` 时抛出，正好用来做 Q9 的异常隔离）。
- `pool.map(fn, 可迭代对象)` 类似内置 map，在线程池里并发，直接返回结果迭代器。

---

## 三、互斥锁 `Lock`（🟥 重点）

线程共享内存，"读出来→改→写回去"三步若中间被打断，就会**丢更新**（讲义原例：3 线程各 +10 次，加了 `sleep(0.01)` 后结果常是 10 而不是 30）。

```python
import threading, time
lock = threading.Lock()
g_num = 0

def func():
    global g_num
    for _ in range(10):
        with lock:                 # 推荐：进入加锁、离开自动释放
            tmp = g_num + 1
            time.sleep(0.01)
            g_num = tmp

threads = [threading.Thread(target=func) for _ in range(3)]
[t.start() for t in threads]
[t.join()  for t in threads]
print(g_num)   # 加锁后稳定 30
```

- 写法二：`lock.acquire()` … `lock.release()`（记得 release，否则死等；`with lock` 更安全）。
- 口诀：**多个线程要改同一个共享变量，就用 `with lock:` 把"读改写"包成原子操作。**
- 🟨 死锁（了解）：线程 A 拿着锁 1 等锁 2，线程 B 拿着锁 2 等锁 1，互相等。避免方法：尽量只用一把锁、固定加锁顺序、用 `with`。

---

## 四、GIL（🟨 会判断选型即可）

- GIL（全局解释器锁）：CPython 里**同一时刻只有一个线程执行 Python 字节码**。
- 所以**多线程对纯 Python 的 CPU 密集计算几乎没加速**（多核用不上）；
- 但 **IO 等待（网络/文件/sleep）时线程会释放 GIL**，所以 IO 密集用多线程依然有效。
- 结论：**CPU 密集 → 多进程（绕开 GIL 真并行）；IO 密集 → 多线程。**

---

## 五、多进程 `multiprocessing`（🟧 会用）

```python
import os, multiprocessing

def cpu_work(n):
    print("子进程", os.getpid(), "父进程", os.getppid(),
          "平方和", sum(i*i for i in range(1, n+1)))

if __name__ == "__main__":          # Windows 必须有，否则无限递归起进程
    p1 = multiprocessing.Process(target=cpu_work, args=(5,))
    p2 = multiprocessing.Process(target=cpu_work, args=(10,))
    p1.start(); p2.start()
    p1.join();  p2.join()
```

- 进程**不共享全局变量**（各自一份内存拷贝）；要通信用 `multiprocessing.Queue`（🟨 了解，今天不考）。
- **Windows 没有 fork，启动代码必须放进 `if __name__ == "__main__":`**，这是最常见报错原因；被提交的函数得是顶层普通函数（能被 pickle）。

### 进程池 `Pool`（🟧 会用 map）

```python
import multiprocessing

def square_sum(n):
    return sum(i*i for i in range(1, n+1))

if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        print(pool.map(square_sum, [5, 10, 20]))   # [55, 385, 2870]
```

- `pool.map(func, 列表)`：把列表每个元素丢给进程池并发处理，**按输入顺序返回结果**，最常用。
- `apply_async(func, args)`（🟨 认识）：异步提交，返回 AsyncResult，用 `.get()` 取；配 `close()`+`join()`。

---

## 六、方法地图（按"想干什么"查）

| 我想干什么 | 用什么 | 关键写法 |
|---|---|---|
| 起一个线程跑函数 | `threading.Thread` | `t=Thread(target=fn,args=(x,)); t.start(); t.join()` |
| 并发跑一批 IO 任务、收返回值 | 线程池 | `with ThreadPoolExecutor(max_workers=N) as p:` → `submit` → `f.result()` |
| 多线程改同一个变量防丢更新 | 互斥锁 | `lock=threading.Lock()`；`with lock: 读改写` |
| 起子进程跑 CPU 任务 | `multiprocessing.Process` | 同 Thread；Windows 包 `__main__` 守卫 |
| 批量把 CPU 任务分给多核 | 进程池 | `with Pool(3) as p: p.map(fn, 数据)` |
| 进程之间传数据（了解） | `multiprocessing.Queue` | `q.put(x)` / `q.get()` |

### 选型决策（一句话版）

```
任务在等什么？
├─ 大部分时间等网络/磁盘（IO 密集）→ 多线程 / 线程池（等待时释放 GIL）
└─ 大部分时间在算（CPU 密集，纯 Python 循环）→ 多进程 / 进程池（绕开 GIL 用多核）
多线程要改共享变量 → 加 Lock。
（极高并发 Web 用的"协程 async/await" → 9/25 FastAPI 阶段学，今天不用。）
```

---

## 七、常见错误与排查

| 现象 / 报错 | 原因 | 处理 |
|---|---|---|
| Windows 多进程疯狂起进程/冻结 | 启动代码没放进 `__main__` 守卫 | 进程创建/`start`/`Pool` 全放进 `if __name__=="__main__":` |
| 进程池任务报 pickle / 找不到函数 | 函数写成了嵌套闭包或 lambda | 用模块顶层的普通 `def` |
| 主线程没等子线程就打印结果 | 只 `start()` 没 `join()` | 逐个 `join()`；线程池/进程池用 `with` |
| 共享计数结果偏小 | 多线程丢更新 | `with lock:` 包住读改写 |
| 一个任务报错整批崩 | 没在收集结果处捕获 | `future.result()` 外面 `try/except`（Q9） |
| 开了多线程 CPU 任务却没加速 | GIL，纯 Python 计算无法并行 | 换多进程/进程池 |

---

## 八、AI 开发视角

1. **并发调用多个模型 / 多路 RAG 检索**（都是网络等待）：脚本里用 `ThreadPoolExecutor` 同时发，总耗时≈最慢一路。
2. **大批量纯 Python 文本清洗/特征计算想用多核**：进程池 `Pool.map`；若用 numpy/pandas（底层 C 会释放 GIL），线程也能加速，数据分析阶段会遇到。
3. **并发 + 异常隔离是工程基本功**：一批请求里某条超时/坏数据不能拖垮整批（Q9 练的就是这个，也是真实客服系统的要求）。
4. **FastAPI 的 `async def` 协程**是另一种更高并发的并发模型，依赖异步 HTTP 库，属于后端阶段内容，9/25 跟着《FastAPI》第 1 章学，今天先把进程/线程/锁这一层吃透即可。

---

## 九、本周方法地图回顾（周测自查，能口述即过关）

- 函数：五种参数、`*args/**kwargs`、lambda、闭包、递归 vs 迭代
- 容器：字典计数 `d[k]=d.get(k,0)+1`、`sorted/max(key=lambda)`、`zip(*)`、推导式
- 文件/异常/JSON：**快照模型**（load→改内存→`'w'`整体覆盖）、`'a'` 只用于日志、异常分层（底层 raise/调用处 except）、`for line in f` 不混 readline
- OOP：`self`、类属性 vs 实例属性、`@property`、继承 `super`、多态、组合 has-a、`__str__` 要 return
- 高级：装饰器（装修 vs 营业、带参三层、wraps、叠加）、生成器（调用不执行/暂停记现场/一次性/流式）
- 并发（今天）：线程池 / 锁 / 多进程 / 进程池，按 IO 密集 vs CPU 密集选型
