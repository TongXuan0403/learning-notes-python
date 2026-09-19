# -*- coding: utf-8 -*-
"""
================================================================================
 D7 · 进程与线程（严格对应《Python2.0》第 14 章）+ 第 1 周周测（含 D4 换皮复测）
 日期：2026-09-19/20（周末）   模式：周测/复习日
 配套知识卡：day07_README.md（建议 PyCharm 左右分屏，左边 README、右边本文件）

 ※ 范围说明（已按你的反馈调整）：
   今天只学 Python 讲义第 14 章：进程 Process / 进程池 Pool / 线程 Thread /
   线程池 ThreadPoolExecutor / 互斥锁 Lock / GIL / 进程与线程选型。
   【协程 async/await 不在 Python 讲义里】，它属于《FastAPI》第 1 章，
   已挪到 9/25 FastAPI 阶段正式学（学完直接用在接口里），今天完全不碰，不用有压力。
================================================================================

【今日作战卡 · 第 1 周 v1】
 开做前四步法：
   ① 先写样例明确输入输出   ② 中文写步骤（伪代码写注释，不许先写语法）
   ③ 查 README 方法地图按"想干什么"选工具   ④ 翻译成代码，先跑最简样例
 卡住纪律：15 分钟内不看答案——写清"卡在哪一步"、翻方法地图、先写一个最笨但能跑的版本；
           再来问，只给"用什么、往哪想"。

 今日待还债 ⚠（优先级最高，先做这个）：
   ▶ D6-Q6 带参 retry 装饰器【白纸默写】：不看任何旧代码，从零写出三层嵌套
     （外层收 times/delay、中层收 func、内层 wrapper）；装饰一个"前 2 次抛异常、
     第 3 次成功"的函数验证；再改成"每次都失败"，验证最后抛出最后一次异常。
     写完把这一段单独发我复跑。

 今日另外待办：
   ▶ 把改好的 day06_practice.py（Q3 FibIterator、Q5 日志装饰器函数名、Q7 无 wraps 对比版）
     发我，我复跑确认 D6 转 ✅。

 今日盯防薄弱点（2 条）：
   ① 动手前先列"输出点清单"，做完逐条打勾（审题漏输出项老毛病）
   ② 成功分支立即 return，别把同一个函数调用两次（D6-Q6 的坑）

 收工三问：输出点齐了吗？ / 看提示的题标 ⚠ 了吗？ / 每题一句话题眼写了吗？
================================================================================
"""

# 今天会用到的标准库（都自带，不用 pip 安装；没有 asyncio）
import os
import time
import json
import threading
import multiprocessing
import concurrent.futures


# ################################################################################
# ① 热身跟写 W1~W5（约 30~40 分钟）
#    做法：先凭记忆在"你的代码"区写 → 跑通后对照 README 最小示例 → 再"改一个条件"
#    （线程数 2 改 4、sleep 1 改 0.5、进程数 2 改 3），确认你真懂每个参数。亲手敲，别复制。
# ################################################################################

# ---------- W1【多线程】两个线程各打印 5 次 ----------
# 任务：写函数 worker(name)，循环 5 次打印"name + 序号"，每次 time.sleep(0.2)；
#       主线程起两个线程（"线程A""线程B"），start 后 join 等它们都结束，最后打印"全部完成"。
# 预期：两个线程输出交错（不是 A 全打完才轮到 B）。
# 用到：threading.Thread(target=,args=,name=)、start()、join()
# 你的代码：

# def worker(name):
#     for i in range(5):
#         print(f"{name} {i}")
#         time.sleep(0.2)
#
# a = threading.Thread(target=worker, name="01", args=("线程A",))
# b = threading.Thread(target=worker, name="02", args=("线程B",))
# a.start(); b.start()
# a.join(); b.join()

# ---------- W2【线程池】并发跑 3 个"模拟 API 调用" ----------
# 任务：写 call_api(api_name, seconds)：打印"开始调用 xxx"，time.sleep(seconds)，
#       返回 f"{api_name} 返回"；用 ThreadPoolExecutor(max_workers=3) + submit 并发调用
#       3 个（耗时 1/1/2 秒），用 future.result() 按提交顺序收集返回值并打印；
#       观察总耗时≈2s 而不是 1+1+2=4s。
# 用到：concurrent.futures.ThreadPoolExecutor、submit(fn, 参数)、future.result()（推荐 with）
# 你的代码：

# def call_api(api_name, seconds):
#     print(f"开始调用 {api_name}")
#     time.sleep(seconds)
#     return api_name,seconds
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
#     fut = [pool.submit(call_api,n,s) for n,s in [("A",1),("B",1),("C",2)]]
#     res = [f.result() for f in fut]
# print(res)


# ---------- W3【互斥锁】保护共享计数器（讲义原例） ----------
# 任务：3 个线程各把共享变量 g_num 做 10 次"tmp=g_num+1; time.sleep(0.01); g_num=tmp"。
#       先不加锁，join 后打印，你会看到经常 <30（丢更新）；
#       再用 threading.Lock()，在"读改写"外面加锁（acquire/release 或 with lock），结果稳定 30。
# 用到：threading.Lock()、lock.acquire()/lock.release() 或 with lock、global
# 你的代码：
#无锁，丢失更新
# g_num = 0
#
# def func():
#     global g_num
#     for i in range(10):
#         tmp = g_num+1
#         time.sleep(0.01)
#         g_num = tmp
#         print(g_num)
#
# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t1.start(); t2.start()
# t1.join(); t2.join()

# 带锁
# g_num = 0
# lock = threading.Lock()
#
# def func():
#     global g_num
#     for i in range(10):
#         with lock:
#             tmp=g_num+1
#             time.sleep(0.02)
#             g_num=tmp
#             print(g_num)
#
# th = [threading.Thread(target=func) for i in range(3)]
# [t.start() for t in th]
# [t.join() for t in th]


# ---------- W4【多进程】起两个子进程（Windows 重点） ----------
# 任务：写 cpu_work(n)：在子进程里打印 os.getpid()（自己）和 os.getppid()（父进程），
#       再打印 1~n 的平方和；主程序起 2 个子进程跑 cpu_work(5)、cpu_work(10)，start+join。
# 边界：所有启动代码必须放在 if __name__ == "__main__": 内，否则 Windows 会无限递归起进程。
# 预期：2 个子进程 pid 不同、ppid 相同；平方和 55、385。
# 用到：multiprocessing.Process(target=,args=)、start、join、os.getpid/os.getppid、__main__ 守卫
# 你的代码：

# def cpu_work(n):
#     print(f"子进程id：{os.getpid()}, 父进程id：{os.getppid()}")
#     print(sum([i*i for i in range(1,n+1)]))
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=cpu_work, args=(5, ))
#     p2 = multiprocessing.Process(target=cpu_work, args=(10, ))
#     p1.start();p2.start()
#     p1.join();p2.join()



# ---------- W5【进程池 · 会用即可】Pool 批量跑任务 ----------
# 任务：写 square_sum(n)：返回 1~n 的平方和；
#       用 multiprocessing.Pool(processes=3) 的 pool.map(square_sum, [5,10,20]) 批量并发，
#       打印结果 [55, 385, 2870]；用完 close()/join()（或 with Pool(3) as pool）。
# 边界：同样要放在 if __name__ == "__main__": 内。
# 用到：multiprocessing.Pool、pool.map（会用 map 即可；apply_async 在 README 里认识一下）
# 你的代码：

# def square_sum(n):
#     return sum(i*i for i in range(1,n+1))
#
# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=3) as pool:
#         print(pool.map(square_sum,[5,10,20]))


# ################################################################################
# ② 正式题（第 1 周周测，换业务外壳；Q1~Q9 必做）
#    纪律：每题先自己走四步法；题面只给一行【本题用到】，不给步骤。
# ################################################################################

# ---------- Q1【🟧 线程池 · AI 场景】并发检索多个文档 ----------
# 题目：客服机器人同时去 3 个知识库检索，每个检索是网络等待（用 sleep 模拟）。
#       写 retrieve(doc_name, seconds)：打印"开始检索 doc_name"，sleep(seconds)，
#       返回 f"{doc_name} 的检索结果"。3 个库耗时 1、1、2 秒。
# 输入：[("产品库",1),("订单库",1),("FAQ库",2)]
# 输出：并发提交全部任务，按"提交顺序"收集并打印 3 条返回值，最后打印总耗时。
# 示例：3 个"开始检索"几乎同时出现；结果顺序为 产品库、订单库、FAQ库；总耗时约 2.0x 秒（不是 4s）。
# 边界：max_workers≥3；必须等所有任务结束程序才退出。
# 验收：总耗时≈2s；结果 3 条且顺序正确。
# 【本题用到】ThreadPoolExecutor、submit、future.result、time.sleep、time.time
# 你的代码：

# def retrieve(doc_name, seconds):
#     print(f"开始检索{doc_name}")
#     time.sleep(seconds)
#     return f"{doc_name,seconds}"
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
#     start = time.time()
#     futures = [pool.submit(retrieve,n,s) for n,s in [("产品库",1),("订单库",1),("FAQ库",2)]]
#     res = [f.result() for f in futures]
#     end = time.time()
# print(res)
# print(f"总耗时约{(end - start):.2f}s")



# ---------- Q2【🟥 互斥锁】多线程汇总各分片 token 数 ----------
# 题目：4 个线程分别统计自己分片的 token 数（用 len 模拟），再累加到共享 total_tokens，
#       每次累加模拟 0.01s 处理延迟。
# 输入：shards = ["你好世界", "今天天气", "Python并发", "大模型应用"]（每片 token 数=字符数）
# 输出：total_tokens 稳定等于 4 片长度之和（4+4+8+5=21）。
# 边界：先故意不加锁跑几次观察 <21 的丢更新；再用 Lock 保证永远是 21。
# 验收：加锁版连续运行 5 次都是 21；一句话说"为什么不加锁会丢"。   线程跑的时候中停一下就有可能被别的线程占用数据
# 【本题用到】threading.Thread、threading.Lock、with lock、global、join
# 你的代码：
# total_tokens = 0
# lock = threading.Lock()
# shards = ["你好世界", "今天天气", "Python并发", "大模型应用"]
#
# def func(token):
#     global total_tokens
#     with lock:
#         for i in token:
#             time.sleep(0.01)
#             total_tokens += 1
#         return total_tokens
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
#     futures = [pool.submit(func,n) for n in shards]
#     for f in futures:
#         print(f.result())


# ---------- Q3【🟧 多进程】起子进程跑 CPU 小任务 ----------
# 题目：写 cpu_work(n)：打印子进程 os.getpid() 和父进程 os.getppid()，再打印 1~n 平方和。
#       主程序起 2 个子进程跑它，start 后 join。
# 输入：cpu_work(5)、cpu_work(10)
# 输出：每个子进程打印 pid/ppid 和平方和；主进程最后打印"子进程全部结束"。
# 边界（Windows 重点）：启动代码全部放 if __name__ == "__main__": 内。
# 验收：2 个不同子进程 pid、相同 ppid；平方和分别 55、385。
# 【本题用到】multiprocessing.Process、start、join、os.getpid、os.getppid、__main__ 守卫
# 你的代码：

# def cpu_work(n):
#     print(f"子id{os.getpid()},父id{os.getppid()}")
#     print(sum(i*i for i in range(1,n+1)))
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=cpu_work, args=(5, ))
#     p2 = multiprocessing.Process(target=cpu_work, args=(10, ))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()



# ---------- Q4【🟧 进程池 · 会用】进程池批量算平方和 ----------
# 题目：用进程池并发计算多组数据的平方和，体会"CPU 活交给进程池"。
#       square_sum(n) 返回 1~n 平方和；用 Pool(processes=3) 对 [5,10,20,30] 批量并发，
#       收集结果并打印；记录总耗时。
# 输出：[55, 385, 2870, 9455]（顺序与输入一致）
# 边界：放 __main__ 守卫内；函数必须能被 pickle（顶层普通函数，别写成嵌套闭包）。
# 验收：结果 4 个且顺序正确；用的是 Pool.map（或 apply_async 收集）。
# 【本题用到】multiprocessing.Pool、pool.map（或 apply_async+get）、__main__ 守卫
# 你的代码：

# def square_sum(n):
#     return sum(i*i for i in range(1, n+1))
# l = [5,10,20,30]
# if __name__ == '__main__':
#     with multiprocessing.Pool(3) as pool:
#         res = pool.map(square_sum, l)
#         for i in res:
#             print(i)

# ---------- Q5【🟨 认知口述】GIL 与进程/线程选型（只写注释，不写代码） ----------
# 用自己的话回答（每题 2~4 句，对照 README 选型表自查）：
#  (1) GIL 是什么？它让 Python 多线程在哪类任务上"几乎等于单线程"？
#  (2) 大量网络/文件等待（IO 密集）选多线程还是多进程？为什么？
#  (3) 大量纯 Python 数值计算（CPU 密集）想利用多核，选什么？
#  (4) 进程和线程在"内存是否共享、创建开销、一个崩了是否连累别人"三点上的区别？
# 验收：方向正确即可；协程/async 不用答（FastAPI 阶段才学）。
# 【本题用到】口述题：GIL、IO 密集 vs CPU 密集、进程 vs 线程
# 你的答案：
# (1)是 CPython 解释器级的一把互斥锁，同一时刻只允许一个线程执行 Python 字节码，所以 CPU 密集的多线程没法真并行
# (2)用多线程，数据共享，占用小。io吃网络。
# (3)选择多进程，给多cup，算力强，数据不会乱
# (4)进程，内存独立，创建开销大，崩了不要影响其他进程。线程，共享内存，创建开销小，坏了影响其他线程


# ---------- Q6【🟥 D4 换皮复测 · JSON 持久化】收藏的 Prompt 持久化 ----------
# 题目（D4-Q8 换外壳，考同一个套路：load 不到返回默认 + 'w' 整体覆盖）：
#       load_favorites(path)：读 favorites.json 返回列表，文件不存在返回 []。
#       save_favorites(data, path)：把列表整体写回（中文正常）。
#       模拟"一轮收藏"：读出列表 → 追加 {"role":"user","content":"怎么学装饰器"}
#       → 追加 {"role":"assistant","content":"先理解闭包"} → 存回。把这轮流程连续执行两次。
# 输出：第一轮后 2 条，第二轮后 4 条；文件始终是"一个合法 JSON 数组"，不是两个 JSON 拼接。
# 边界：第二轮要在原有基础上累加，不能覆盖旧数据，也不能用 'a' 直接拼 JSON。
# 验收：两轮后 len==4；json.load 能一次读回（不报 JSONDecodeError）。
# 【本题用到】json.load/json.dump、with open("r"/"w")、FileNotFoundError、list.append
# 你的代码：

# def load_favorites(path):
#     try:
#         with open(path,"r",encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []
#
# def save_favorites(data, path):
#     with open(path,"w",encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
#
# his = load_favorites("favorites.json")
# print(his)
#
# his.append({"role":"user","content":"怎么学装饰器"})
# his.append({"role":"assistant","content":"先理解闭包"})

# save_favorites(his, "favorites.json")
#




# ---------- Q7【🟥 D4 换皮复测 · 日志统计 + 异常分层】工单日志 ----------
# 题目（合并 D4-Q6/Q7，换外壳）：
#       底层 read_lines(path) 负责读文件，文件不存在时"让异常抛出去"（这层不吞）；
#       主程序调用它，在调用处 except FileNotFoundError 给友好提示并结束本题。
#       读到后统计每行第 2 列级别（INFO/WARN/ERROR）次数，输出字典；
#       并把所有 ERROR 行用 'w' 整体写入 errors.txt；空行跳过。
# 输入：tickets.log，10 行，形如 "2026-09-20 INFO 工单已创建"，其中 INFO 5、WARN 3、ERROR 2，含 1 个空行
# 输出：{'INFO':5,'WARN':3,'ERROR':2}；errors.txt 恰好 2 行 ERROR
# 边界：文件不存在 → 打印"日志文件不存在"而不是崩溃；空行不计。
# 验收：统计正确；删掉 tickets.log 后给友好提示；体现"底层抛、调用处接"。
# 【本题用到】open、for line in f（禁止混用 readline）、split、dict.get 计数、raise/except FileNotFoundError
# 你的代码：
# d = {}
# ll = []
# def read_lien(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         return f.readlines()
# try:
#     lines = read_lien("tickets.log")
# except FileNotFoundError:
#     print("日志文件不存在")
#
# else:
#     for line in lines:
#         l = line.strip()
#         if not l:
#             continue
#         l1 = l.split()
#         l2 = l1[1]
#         d[l2] = d.get(l2, 0) + 1
#         if l2 == "ERROR":
#             ll.append(l + '\n')
#     print(d)
#     with open("errors.txt", "w", encoding="utf-8") as f:
#         f.writelines(ll)


# ---------- Q8【🟥 D4 换皮复测 · return 不是 print】取 FAQ 首问 ----------
# 题目（D4-Q4 换皮）：写 first_question(path)：文件存在时"返回"第一行去空白后的内容；
#       文件不存在时"返回" "暂无FAQ"。用 print(first_question(...)) 验证两种情况。
# 输入：faq.txt（第一行写"如何退货？"）和一个不存在的路径
# 输出：存在 → 返回 '如何退货？'；不存在 → 返回 '暂无FAQ'
# 边界：必须用 return 交出结果，函数里不许直接 print 结果。
# 验收：调用处能接住返回值再打印；两种路径都正确返回。
# 【本题用到】def/return、with open、readline 或 for、strip、except FileNotFoundError
# 你的代码：

# def first_question(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as f:
#             return f.readline().strip()
#     except FileNotFoundError:
#         return "暂无FAQ"
# print(first_question("D6-Q6"))
# print(first_question("faq.txt"))

# ---------- Q9【🟥 综合 · 客服主线小型集成】多线程工单批处理器 ----------
# 题目：把本周的 函数/异常/线程/JSON 串起来（不要求完整管理系统）：
#   1) handle_ticket(ticket: str) -> str：
#      - ticket 为空或去空白后为空 → raise ValueError("工单内容不能为空")；
#      - 否则 time.sleep(0.3) 模拟处理，返回 f"已回复：{ticket}"。
#   2) tickets = ["查订单", "退款进度", "", "改地址", "  "]（含 2 个空工单）；
#      用 ThreadPoolExecutor(max_workers=3) 并发处理；
#      - 正常工单：{工单原文: 回复} 收进 results；
#      - 空工单的异常不能让整批崩：在 future.result() 外面 try/except，失败原文记进 failed。
#   3) 全部结束后用 'w' 把 results 存进 results.json（ensure_ascii=False）；
#      打印成功几条、失败原文是哪几条。
# 输出示例：成功处理 3 条；失败工单：['', '  ']；results.json 里 3 个键值对
# 边界：空/纯空白算失败；某条失败不影响其他条；results.json 是合法 JSON 对象。
# 验收：成功=3、失败=2；json.load 能读回且只有 3 条。
# 【本题用到】函数+raise ValueError、ThreadPoolExecutor、submit/result、try/except、json.dump、'w'
# 你的代码：

# tickets = ["查订单", "退款进度", "", "改地址", "  "]
#
# def handle_ticket(ticket: str) -> str:
#     if ticket is None or str(ticket).strip() == "":
#         raise ValueError("工单内容不能为空")
#
#     time.sleep(0.3)
#     return f"已回复：{ticket}"
# results = {}
# failed = []
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
#     futures = [pool.submit(handle_ticket,n) for n in tickets]
#     for i in futures:
#         try:
#             i.result()
#             print(i.result())
#         except ValueError as e:
#             print(e)
# with open("result.json", "w", encoding="utf-8") as f:
#     json.dump(results, f, ensure_ascii=False)
def handle_ticket(ticket: str) -> str:
    """处理单张工单；空串或纯空白直接抛 ValueError。"""
    if ticket is None or str(ticket).strip() == "":
        raise ValueError("工单内容不能为空")
    time.sleep(0.3)
    return f"已回复：{ticket}"

def main():
    tickets = ["查订单", "退款进度", "", "改地址", "  "]
    results = {}    # 成功：{工单原文: 回复}
    failed = []     # 失败：工单原文

    # 3 个员工的线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        # ① 一次派完 5 张单，拿到 5 张小票（submit 立刻返回，不等结果）
        futures = [pool.submit(handle_ticket, t) for t in tickets]
        # ② 原文 t 和小票 f 配对，逐张取；每张一套 try，坏一张不连累其他
        for t, f in zip(tickets, futures):
            try:
                results[t] = f.result()   # 成功：回复存字典，键是原文
            except ValueError:
                failed.append(t)          # 失败：只记原文，循环继续

    # ③ 全部结束后，把成功结果整体快照写盘（'w' 覆盖，不是 'a' 拼接）
    with open("results.json", "w", encoding="utf-8") as fp:
        json.dump(results, fp, ensure_ascii=False, indent=2)

    print(f"成功处理 {len(results)} 条；失败工单：{failed}")

if __name__ == "__main__":
    main()

# ################################################################################
# ③ 联想微训练（只口述，每题几句话写在下面，不写完整代码，约 8 分钟）
# ################################################################################
#
# 微训练 1：RAG 要同时检索 5 个文档（全是网络等待）。用线程池还是多进程？为什么？
#           （更高并发的"协程"先不用答，FastAPI 阶段会专门学）
# 答：
#用线程池，网络i/o 不许要多少算力
# 微训练 2：一个函数用纯 Python 的 for 循环做几亿次数值计算（没用 numpy）。
#           开 4 个线程能快约 4 倍吗？为什么？想利用多核该换什么？
# 答：
#不能，线程用不了多少cpu算力，多进程可以多核一起，算力更强
# 微训练 3：多个线程同时给同一个全局计数器 +1，结果比预期小。这是什么问题？用什么解决？
# 答：数据没更新上，多线程是共用数据内存，可能导致一个线程任务还没跑完，被别的线程占了使用。开始执行它的任务


# ################################################################################
# ④ 收工提交清单（做完自查，然后把本文件发我批改）
# ################################################################################
#  □ 还债：D6-Q6 retry 白纸默写已单独发我
#  □ day06 改好的 Q3/Q5/Q7 已发我复跑
#  □ W1~W5 热身亲手敲完并各"改了一个条件"
#  □ Q1~Q9 完成，输出点逐条打勾
#  □ Q6/Q7/Q8（D4 换皮复测）独立写出、没翻旧代码
#  □ 联想微训练 3 题写了口述答案
#  □ 每题一句话题眼；看了提示/答案的题已标 ⚠
#
# 收工三问：输出点齐了吗？ / ⚠ 标了吗？ / 题眼写了吗？
# 说"收工"我再归档同步 GitHub；问问题按"要实现什么/试过什么/卡在哪报什么错"描述。
#（注：内容由AI生成）


"""
线程创建

th = threading.Thread(target=func, args=())
th.start
th.join

进程创键

if __name__ == '__main__'
    mp = multiprocessing.Process(target=func, args=())
    mp.start
    mp.join

线程池创建

with concurrent.futures.ThreadPoolExecutor() as pool:
    

进程池创建
if __name__ = '__main__':
    with multiprocessing.Pool(2) as pool:
    

"""

"""

def work(x):
    time.sleep(0.2)
    return f"输入{x} → 结果{x * x}"

if __name__ == "__main__":
    data = [1, 2, 3, 4]
    print("========== 1. ThreadPoolExecutor + submit ==========")
    
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(work, num) for num in data]
        for f in futures:
            print(f.result())

    print("\n========== 2. ThreadPoolExecutor + map ==========")
    with ThreadPoolExecutor(max_workers=2) as pool:
        res_iter = pool.map(work, data)
        for r in res_iter:
            print(r)

    print("\n========== 3. ProcessPoolExecutor + submit ==========")
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(work, num) for num in data]
        for f in futures:
            print(f.result())

    print("\n========== 4. ProcessPoolExecutor + map ==========")
    with ProcessPoolExecutor(max_workers=2) as pool:
        res_iter = pool.map(work, data)
        for r in res_iter:
            print(r)
"""