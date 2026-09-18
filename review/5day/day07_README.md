# D7 知识卡：进程 / 线程 / 协程（async）会用 + 第 1 周周测

> 今天是**周测日**。进程/线程/协程对 AI 应用开发都属于 **🟧 会用**层（不是让你去写操作系统级并发），目标是：看到并发代码不慌、能起线程池/协程跑 IO 任务、知道什么时候选哪个、能解释 GIL。知识取自《Python2.0》第 14 章与《FastAPI&SQLAlchemy》第 1 章。
>
- 🟥 核心（要独立手写）：本周旧知识的周测、D4 换皮复测（JSON 持久化 / 异常分层 / return）
- 🟧 会用（能跑通、能改参数）：`threading` 线程与线程池、`Lock`、`multiprocessing` 起子进程、`async/await` + `gather`
- 🟨 了解（建立认知即可）：进程池/Queue 通信、事件循环底层、`wait_for`/`cancel`、`to_thread`

---

## 一、知识速整（先用自己的话复述，再敲最小示例）

### 1. 并发 vs 并行；进程 vs 线程 vs 协程

- **并发**：一个 CPU 在多个任务间**交替**执行（宏观同时、微观切换）。
- **并行**：多个 CPU 核**同一时刻真的各干各的**。
- **进程**：操作系统**资源分配**的基本单位。一个正在运行的程序就是一个进程，有**独立内存**，互不干扰，崩溃一般不连累别人；创建开销大。
- **线程**：CPU **调度执行**的基本单位。一个进程至少一个线程，线程**共享进程内存**，创建开销小；一个线程崩了可能拖垮整个进程。
- **协程**：用户态的"轻量级线程"，**不由操作系统调度，由程序自己（事件循环）调度**；靠 `await` 主动让出 CPU，切换开销极小，单线程可跑上万个；同一时刻只有一个协程在跑，**无需加锁**。

| 机制 | 谁调度 | 切换开销 | 内存 | 适用 | 短板 |
|---|---|---|---|---|---|
| 进程 | 操作系统 | 大（内核级） | 完全隔离 | **CPU 密集**、要隔离 | 重、数量有限、通信麻烦 |
| 线程 | 操作系统 | 较大（内核级） | 共享（要加锁） | **IO 密集**、低并发 | 受 GIL 限制，线程多了切换/加锁成本高 |
| 协程 | 程序的事件循环 | 极小（函数调用级） | 共享（无需锁） | **IO 密集、极高并发**（Web） | 必须用"异步库"，阻塞调用会卡死整个循环 |

### 2. 多线程 `threading`（🟧）

```python
import threading, time

def worker(name):
    for i in range(5):
        print(name, i)
        time.sleep(0.2)

t1 = threading.Thread(target=worker, args=("线程A",), name="A")
t2 = threading.Thread(target=worker, args=("线程B",), name="B")
t1.start(); t2.start()   # start：启动，线程开始并发跑
t1.join();  t2.join()    # join：主线程在这等，直到对应线程结束
print("全部完成")
```

- `Thread(target=函数, args=(参数元组,), name=...)`：造线程；`args` 必须是**元组**，一个参数也要写逗号 `(x,)`。
- `start()` 启动；`join()` 阻塞等待。**只 start 不 join，主线程可能提前结束**。
- `daemon=True` 守护线程：主进程结束时它自动被带走（后台任务用）。

**线程池**（更常用，不用手动管一堆线程）：

```python
import concurrent.futures

def call_api(name, seconds):
    time.sleep(seconds)
    return f"{name}结果"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    futs = [pool.submit(call_api, n, s) for n, s in [("A",1),("B",1),("C",2)]]
    results = [f.result() for f in futs]   # result() 取返回值；顺序与提交一致
print(results)   # 总耗时≈2s（最慢那个），不是 4s
```

### 3. 线程安全与互斥锁 `Lock`（🟧）

多个线程**共享变量**，"读出来→改→写回去"三步如果中间被打断，就会**丢更新**。

```python
import threading
lock = threading.Lock()
counter = 0

def add():
    global counter
    for _ in range(10):
        with lock:                 # 进入加锁，离开自动释放（推荐，等价 acquire/release）
            tmp = counter + 1
            time.sleep(0.01)
            counter = tmp

ts = [threading.Thread(target=add) for _ in range(3)]
[t.start() for t in ts]; [t.join() for t in ts]
print(counter)   # 加锁后稳定 30；不加锁经常 <30
```

> 口诀：**多个线程要改同一个共享变量，就用 `with lock:` 把"读改写"包起来。**

### 4. GIL（🟨 会判断选型即可）

- GIL（全局解释器锁）是 CPython 的一把大锁：**同一时刻只有一个线程执行 Python 字节码**。
- 所以**多线程不适合纯 Python 的 CPU 密集计算**（多核用不上，≈单线程）；
- 但 **IO 等待（网络/文件/sleep）时线程会释放 GIL**，所以 IO 密集用多线程依然有效。
- 结论：**CPU 密集 → 多进程（绕开 GIL，真并行）；IO 密集 → 多线程或协程。**

### 5. 多进程 `multiprocessing`（🟧 会起子进程即可）

```python
import os, multiprocessing

def cpu_work(n):
    print("子进程", os.getpid(), "父进程", os.getppid(), "平方和", sum(i*i for i in range(1, n+1)))

if __name__ == "__main__":          # Windows 必须有这个守卫，否则无限递归起进程
    p1 = multiprocessing.Process(target=cpu_work, args=(5,))
    p2 = multiprocessing.Process(target=cpu_work, args=(10,))
    p1.start(); p2.start()
    p1.join();  p2.join()
```

- 进程**不共享全局变量**（各自一份内存拷贝）；要通信用 `multiprocessing.Queue`（🟨 了解，今天不深究）。
- Windows 没有 fork，**所有启动代码必须放在 `if __name__ == "__main__":` 内**，这是最常见的报错原因。

### 6. 协程 `async / await`（🟧，FastAPI 的地基，重点）

```python
import asyncio, time

async def task(name, seconds):       # async def 定义"协程函数"
    print("开始", name)
    await asyncio.sleep(seconds)     # await：在这里让出 CPU，去跑别的协程
    print("完成", name)
    return f"{name}结果"

async def main():
    # 并发：先包成 Task（立即在后台开始），再 gather 等全部完成
    t1 = asyncio.create_task(task("C", 1))
    t2 = asyncio.create_task(task("D", 2))
    results = await asyncio.gather(t1, t2)
    print(results)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())              # asyncio.run：启动事件循环（入口）
    print(f"并发耗时 {time.time()-start:.2f}s")   # ≈2s，不是 3s
```

四个必须想清楚的点：

1. **调用协程函数不会执行函数体**，只返回一个协程对象（和"调用生成器函数不执行"一模一样）；要靠事件循环驱动。
2. **`asyncio.run(主协程)`** 是入口：创建并跑起事件循环，直到主协程结束。
3. **`await` = 让出 CPU**：遇到 `await asyncio.sleep/网络` ，当前协程挂起，事件循环去跑别的就绪协程，等 IO 好了再回来从 `await` 下一行继续。
4. **`create_task` + `gather` 才并发**：`create_task` 把协程注册到后台开始跑；`gather` 等它们全部完成并**按提交顺序**收集结果。
   - 串行：`await task("A",1)` 再 `await task("B",2)` → 总耗时 1+2=3s。
   - 并发：两个都 `create_task` 再 `gather` → 总耗时 ≈ max(1,2)=2s。
   - **坑**：只 `create_task` 不 `gather`/不 await，主协程瞬间结束，任务体来不及跑（0.00s）。

### 7. 协程的限制：别用阻塞库（🟨）

- 协程跑在**单线程**里。一旦写出**阻塞调用**（`time.sleep`、`requests.get`、同步文件读写），整个事件循环和所有协程一起卡住，并发失效。
- 对应换法：`time.sleep` → `await asyncio.sleep`；`requests` → 异步库 `aiohttp` / `httpx.AsyncClient`。
- 实在要用同步阻塞库：`await asyncio.to_thread(同步函数, 参数...)` 把它丢到线程池（知道有这招即可）。
- `asyncio.wait_for(协程, timeout=2)`：给异步任务设超时，超时抛 `asyncio.TimeoutError`（了解）。

---

## 二、方法地图（按"想干什么"查）

| 我想干什么 | 用什么 | 关键写法 / 返回 |
|---|---|---|
| 起一个线程跑函数 | `threading.Thread` | `t=Thread(target=fn,args=(x,)); t.start(); t.join()` |
| 并发跑一批 IO 任务、收返回值 | 线程池 | `with ThreadPoolExecutor(max_workers=N) as p:` → `submit(fn,args)` → `f.result()` |
| 多个线程改同一个变量 | 互斥锁 | `lock=threading.Lock()`；`with lock: 读改写` |
| 起子进程跑 CPU 任务 | `multiprocessing.Process` | 同 Thread；**Windows 包在 `if __name__=="__main__":` 里** |
| 定义可暂停的异步函数 | 协程 | `async def f(): await ...`，调用只返回协程对象 |
| 启动异步程序 | 事件循环入口 | `asyncio.run(main())` |
| 在协程里"等待/让出" | await | `await asyncio.sleep(1)`（**不是** `time.sleep`） |
| 并发跑多个协程 | Task + gather | `ts=[create_task(c) for c in ...]; await gather(*ts)` |
| 协程里调同步阻塞库 | 隔离到线程 | `await asyncio.to_thread(同步fn, 参数)` |
| 给异步任务限时 | 超时 | `await asyncio.wait_for(coro, timeout=2)` |

### 选型决策（一句话版）

```
任务在等什么？
├─ 大部分时间在等网络/磁盘（IO 密集）
│    ├─ 代码是普通同步函数、并发量不大      → 线程池 ThreadPoolExecutor
│    └─ 用 async 框架（FastAPI/异步 HTTP）  → 协程 asyncio + gather（极高并发）
└─ 大部分时间在算（CPU 密集，纯 Python 循环）
     └─ 多进程 multiprocessing（绕开 GIL 用多核）
共享变量被多线程改 → 加 Lock；协程单线程无需锁。
```

---

## 三、常见错误与排查

| 现象 / 报错 | 原因 | 处理 |
|---|---|---|
| Windows 多进程疯狂起进程 / 冻结 / `RuntimeError` | 启动代码没放进 `__main__` 守卫 | 进程创建与 `start()` 全部放进 `if __name__=="__main__":` |
| 主线程没等子线程就打印结果 | 只 `start()` 没 `join()` | 对每个线程 `join()`；线程池用 `with` |
| 共享计数结果偏小 | 多线程丢更新 | `with lock:` 包住读改写 |
| `create_task` 后任务没跑、耗时 0.00s | 没人等它，main 提前结束 | `await asyncio.gather(*tasks)` |
| 协程并发后总耗时还是各任务之和 | 用了 `await a(); await b()` 串行，或协程里 `time.sleep` | 改 `create_task+gather`；等待用 `asyncio.sleep` |
| `coroutine object is not ...` / 函数没执行 | 直接 `f()` 没放进事件循环 | `asyncio.run(f())` 或 `await f()` |
| 一个线程/任务报错整批崩 | 没在收集结果处捕获 | `future.result()` 外面、或每个任务外面 `try/except` |

---

## 四、AI 开发视角（为什么今天要学这些）

1. **FastAPI 的接口就是 `async def`**：`@app.get("/ask")` + `await model.ainvoke(...)`。一个事件循环能同时扛成千上万个连接，靠的就是协程在等模型/数据库时让出 CPU。
2. **并发调用多个模型 / 多路 RAG 检索**：用 `asyncio.gather` 同时检索多个知识库、或同时调多个模型，总耗时≈最慢的一路，而不是相加；同步脚本里则用 `ThreadPoolExecutor`。
3. **LLM 的 Python SDK 大多同时给同步/异步两套**：`client.chat.completions.create()`（同步，配线程池）与 `await client.chat.completions.create(...)`（异步，配 gather）。
4. **数据预处理/批处理是 CPU 活**：大批量纯 Python 文本清洗想用多核 → 多进程；但如果用 numpy/pandas（底层 C 会释放 GIL），线程也能加速，后面数据分析阶段会遇到。
5. **并发 + 异常隔离是工程基本功**：一批请求里某一条超时/坏数据，不能拖垮整批（Q9 练的就是这个，也是真实客服系统的要求）。

---

## 五、本周方法地图回顾（周测自查，能口述即过关）

- 函数：五种参数、`*args/**kwargs`、lambda、闭包、递归 vs 迭代
- 容器：字典计数 `d[k]=d.get(k,0)+1`、`sorted/max(key=lambda)`、`zip(*)`、推导式
- 文件/异常/JSON：**快照模型**（load→改内存→`'w'`整体覆盖）、`'a'` 只用于日志、异常分层（底层 raise/调用处 except）、`for line in f` 不混 readline
- OOP：`self`、类属性 vs 实例属性、`@property`、继承 `super`、多态鸭子类型、组合 has-a、`__str__` 要 return
- 高级：装饰器（`f=deco(f)`、装修 vs 营业、带参三层、wraps、叠加）、生成器（调用不执行/暂停记现场/一次性/流式）
- 并发（今天）：线程池/锁/多进程/协程 gather，按 IO 密集 vs CPU 密集选型
