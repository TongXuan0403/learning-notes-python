# -*- coding: utf-8 -*-
"""
================================================================================
 D7 · 进程/线程会用 + async/await 认知 + 并发小实跑 + 第 1 周周测（含 D4 换皮复测）
 日期：2026-09-19/20（周末）   模式：周测/复习日（约 6~7h，不硬赶）
 配套知识卡：day07_README.md（建议 PyCharm 左右分屏，左边 README、右边本文件）
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

# 今天会用到的标准库（都自带，不用 pip 安装）
import time
import json
import threading
import multiprocessing
import concurrent.futures
import asyncio


# ################################################################################
# ① 热身跟写 W1~W5（约 30~40 分钟）
#    做法：先凭记忆在"你的代码"区写 → 跑通后对照 README 最小示例 → 再"改一个条件"
#    （比如把线程数 2 改成 4、sleep 1 改成 0.5），确认你真的理解每个参数。
#    热身是"亲手敲"，不是"复制粘贴"，可以慢，但每行都要知道在干嘛。
# ################################################################################

# ---------- W1【多线程】两个线程各打印 5 次 ----------
# 任务：写函数 worker(name)，循环 5 次打印"name + 序号"，每次 time.sleep(0.2)；
#       主线程起两个线程（名字分别叫"线程A""线程B"），start 后用 join 等它们都结束，
#       最后主线程打印"全部完成"。
# 预期：两个线程的输出交错出现（不是 A 全打完才轮到 B）。
# 用到：threading.Thread(target=worker, args=(...), name=...), start(), join()
# 你的代码：


# ---------- W2【线程池】并发跑 3 个"模拟 API 调用" ----------
# 任务：写函数 call_api(api_name, seconds)，先打印"开始调用 xxx"，time.sleep(seconds)
#       模拟网络等待，再返回 f"{api_name} 耗时{seconds}s 返回"；
#       用 ThreadPoolExecutor(max_workers=3) + submit 并发调用 3 个（耗时分别 1/1/2 秒），
#       用 future.result() 收集 3 个返回值并打印；观察总耗时≈2s 而不是 1+1+2=4s。
# 用到：concurrent.futures.ThreadPoolExecutor、executor.submit(fn, 参数...)、future.result()
#       （推荐 with ThreadPoolExecutor(...) as executor: 自动回收）
# 你的代码：


# ---------- W3【互斥锁】保护共享计数器 ----------
# 任务：先做"不加锁版"：3 个线程各对共享变量 counter 做 10 次
#       "tmp = counter + 1; time.sleep(0.01); counter = tmp"，join 后打印 counter
#       ——你会看到结果经常小于 30（丢更新）；
#       再做"加锁版"：在修改共享变量的三行外面用 threading.Lock() 保护
#       （with lock: 或 acquire/release），结果稳定为 30。
# 用到：threading.Lock()、with lock:、global
# 你的代码：


# ---------- W4【协程串行】async def + await + asyncio.run ----------
# 任务：写 async def task(name, seconds)：打印"开始 name"，await asyncio.sleep(seconds)，
#       打印"完成 name"，return f"{name}结果"；
#       写 async def main_serial()，里面用两次 await 串行调用 task("A",1)、task("B",2)；
#       在 if __name__ == "__main__": 里用 asyncio.run(main_serial()) 启动，计时，确认≈3s。
# 注意：协程函数"调用不执行"，只返回协程对象，必须靠事件循环（asyncio.run）驱动——和生成器一个道理。
# 用到：async def、await、asyncio.sleep、asyncio.run
# 你的代码：


# ---------- W5【协程并发】create_task + gather ----------
# 任务：写 async def main_concurrent()，把 task("C",1)、task("D",2) 用
#       asyncio.create_task(...) 包成两个任务，再 results = await asyncio.gather(t1, t2)，
#       打印 results；计时确认总耗时≈2s（=最慢的那个），两个"开始"几乎同时出现。
# 坑（必踩一次并记住）：如果只 create_task 却不 await gather，main 瞬间结束、任务体来不及跑（0.00s）。
# 用到：asyncio.create_task、asyncio.gather
# 你的代码：


# ################################################################################
# ② 正式题（第 1 周周测，换业务外壳；Q1~Q9 必做，Q10 选做）
#    纪律：每题先自己走四步法；题面只给一行【本题用到】，不给步骤。
# ################################################################################

# ---------- Q1【🟧 多线程并发 · AI 场景】并发检索多个文档 ----------
# 题目：客服机器人要同时去 3 个知识库检索，每个检索都是网络等待（用 sleep 模拟）。
#       写 retrieve(doc_name, seconds)：打印"开始检索 doc_name"，sleep(seconds)，
#       返回 f"{doc_name} 的检索结果"。3 个库耗时分别为 1、1、2 秒。
# 输入：3 个待检索库 [("产品库",1),("订单库",1),("FAQ库",2)]
# 输出：先并发提交全部任务，再按"提交顺序"收集并打印 3 条返回值，最后打印总耗时。
# 示例（顺序可能交错，但收集到的结果顺序与提交一致）：
#       开始检索 产品库 / 开始检索 订单库 / 开始检索 FAQ库（几乎同时）
#       ['产品库 的检索结果', '订单库 的检索结果', 'FAQ库 的检索结果']
#       并发总耗时约 2.0x 秒
# 边界：max_workers 至少为 3；必须等所有任务结束程序才退出。
# 验收：总耗时≈2s（不是 4s）；结果是 3 条且顺序正确。
# 【本题用到】ThreadPoolExecutor、submit、future.result、time.sleep、time.time
# 你的代码：


# ---------- Q2【🟥 线程安全】多线程汇总各分片的 token 数 ----------
# 题目：把一段长文本切成 4 个分片，4 个线程分别"统计自己分片的 token 数（这里用 len 模拟）"，
#       然后累加到共享的总计数 total_tokens 里。每个线程累加时模拟 0.01s 处理延迟。
# 输入：shards = ["你好世界", "今天天气", "Python并发", "大模型应用"]（每片 token 数=字符数）
# 输出：最终 total_tokens 必须稳定等于 4 片长度之和（4+4+8+5=21）。
# 边界：先故意不加锁跑几次观察会出现 <21 的丢更新；再用 Lock 保证永远是 21。
# 验收：加锁版连续运行 5 次结果都是 21；说一句"为什么不加锁会丢"。
# 【本题用到】threading.Thread、threading.Lock、with lock、global、join
# 你的代码：


# ---------- Q3【🟧 多进程会用】起子进程跑 CPU 小任务 ----------
# 题目：写 cpu_work(n)：在子进程里打印自己的进程号 os.getpid() 和父进程号 os.getppid()，
#       然后做一个小循环（求 1~n 的平方和）并打印结果。
#       主程序起 2 个子进程跑它，start 后 join 等它们结束。
# 输入：cpu_work(5)、cpu_work(10) 各一个子进程
# 输出：每个子进程打印自己的 pid/ppid 和平方和；主进程最后打印"子进程全部结束"。
# 边界（Windows 重点）：所有启动代码必须放在 if __name__ == "__main__": 里面，否则会无限递归起进程。
# 验收：能看到 2 个不同的子进程 pid，ppid 相同（都是主进程）；平方和分别为 55、385。
# 【本题用到】multiprocessing.Process(target=,args=)、start、join、os.getpid、os.getppid、__main__ 守卫
# 你的代码：


# ---------- Q4【🟧 async/await】串行 vs 并发调用 3 个"异步模型" ----------
# 题目：写 async def amodel(name, seconds)：打印"请求模型 name"，await asyncio.sleep(seconds)，
#       返回 f"{name}回复"。
#       (1) main_serial：用 3 次 await 串行调用，耗时 1+1+2；
#       (2) main_gather：用 create_task + gather 并发 3 个，耗时≈max=2。
#       分别 asyncio.run 并打印两种总耗时和结果列表。
# 输入：[("模型A",1),("模型B",1),("模型C",2)]
# 输出：串行≈4s、并发≈2s；并发结果列表顺序仍是 A、B、C。
# 边界：协程里等待只能用 await asyncio.sleep，不能用 time.sleep（否则并发失效）。
# 验收：两种耗时差距明显；一句话解释"为什么并发≈最慢的一个"。
# 【本题用到】async def、await、asyncio.sleep、asyncio.run、create_task、gather
# 你的代码：


# ---------- Q5【🟨 认知口述 + 一个小例子】进程/线程/协程/GIL 选型 ----------
# 题目：用注释口头回答下面 4 个问题（每题 2~4 句，说人话），再完成 (5) 的小例子。
#   (1) GIL 是什么？它让 Python 多线程在什么任务上"形同单线程"？
#   (2) 大量网络/文件等待（IO 密集）选线程还是进程？为什么？极高并发 Web 用什么？
#   (3) 大量纯 Python 数值计算（CPU 密集）想利用多核，选线程还是进程？
#   (4) 为什么协程里写 time.sleep(2) / requests.get() 会让整个事件循环卡住？该换成什么？
#   (5) 小例子：把一个同步阻塞调用 time.sleep 用 asyncio.to_thread 包到线程里，
#       在 async main 里 await 它，验证协程没被卡死（知道有这招即可，不深究）。
# 验收：4 个问题答案方向正确（对照 README 选型表自查）；(5) 能跑通。
# 【本题用到】口述题 + asyncio.to_thread（3.9+）
# 你的答案/代码：


# ---------- Q6【🟥 D4 换皮复测 · JSON 持久化】收藏的 Prompt 持久化 ----------
# 题目（D4-Q8 换业务外壳，考同一个套路：load 不到返回默认 + 'w' 整体覆盖）：
#       写 load_favorites(path)：读 favorites.json 返回列表；文件不存在返回 []。
#       写 save_favorites(data, path)：把列表整体写回（中文正常）。
#       模拟"一轮收藏"：读出列表 → 追加一条 {"role":"user","content":"怎么学装饰器"}
#       → 追加一条 {"role":"assistant","content":"先理解闭包"} → 存回。
# 输入：程序连续运行两轮（把"一轮收藏"这段流程执行两次）
# 输出：第一轮后文件里 2 条，第二轮后 4 条；文件始终是"一个合法 JSON 数组"，不是两个 JSON 拼接。
# 边界：第二次运行前文件已存在，要在原有基础上累加，不能覆盖掉旧数据，也不能用 'a' 直接拼 JSON。
# 验收：两轮后 len == 4；用 json.load 能一次读回（不报 JSONDecodeError）。
# 【本题用到】json.load/json.dump、with open(.., "r"/"w")、FileNotFoundError、list.append
# 你的代码：


# ---------- Q7【🟥 D4 换皮复测 · 日志统计 + 异常分层】工单日志 ----------
# 题目（合并 D4-Q6 计数/error.log 与 Q7 异常分层，换业务外壳）：
#       底层函数 read_lines(path)：负责读文件，文件不存在时"让异常抛出去"（不在这层吞）。
#       主程序：调用 read_lines，在调用处 except FileNotFoundError 给友好提示并结束本题。
#       读到内容后统计每行第 2 列的级别（INFO/WARN/ERROR）次数，输出字典；
#       并把所有 ERROR 行用 'w' 整体写入 errors.txt；空行跳过。
# 输入：tickets.log，10 行，形如 "2026-09-20 INFO 工单已创建"，其中 INFO 5、WARN 3、ERROR 2，含 1 个空行
# 输出：统计字典 {'INFO':5,'WARN':3,'ERROR':2}；errors.txt 里恰好 2 行 ERROR
# 边界：文件不存在 → 主程序打印"日志文件不存在"而不是崩溃；空行不计入。
# 验收：统计数字正确；删除 tickets.log 后运行给友好提示；体现"底层抛、调用处接"。
# 【本题用到】open、for line in f（禁止混用 readline）、split、dict.get 计数、raise/except FileNotFoundError
# 你的代码：


# ---------- Q8【🟥 D4 换皮复测 · return 不是 print】取 FAQ 首问 ----------
# 题目（D4-Q4 换皮）：写 first_question(path)：文件存在时"返回"第一行去掉首尾空白后的内容；
#       文件不存在时"返回"字符串 "暂无FAQ"。写好后用 print(first_question(...)) 验证两种情况。
# 输入：faq.txt（自己造，第一行写"如何退货？"）；以及一个不存在的路径
# 输出：存在 → 返回 '如何退货？'；不存在 → 返回 '暂无FAQ'
# 边界：必须用 return 把结果交出去，函数里不许直接 print 结果。
# 验收：调用处能接住返回值再打印；两种路径都正确返回。
# 【本题用到】def/return、with open、readline 或 for、strip、except FileNotFoundError
# 你的代码：


# ---------- Q9【🟥 综合 · 客服主线小型集成】并发工单处理器 ----------
# 题目：做一个"迷你客服批处理器"，把本周的 函数/异常/线程/JSON 串起来（不要求完整管理系统）：
#   1) 写同步函数 handle_ticket(ticket: str) -> str：
#      - 若 ticket 为空字符串或去掉空白后为空，raise ValueError("工单内容不能为空")；
#      - 否则 time.sleep(0.3) 模拟处理，返回 f"已回复：{ticket}"。
#   2) 一批工单 tickets = ["查订单", "退款进度", "", "改地址", "  "]（含 2 个空工单）；
#      用 ThreadPoolExecutor(max_workers=3) 并发处理；
#      - 正常工单：把 {工单原文: 回复} 收进结果字典 results；
#      - 空工单抛的异常不能让整批崩溃：在收集结果处（future.result() 外面）try/except 接住，
#        把失败工单记进 failed 列表。
#   3) 全部结束后，用 'w' 把 results 存进 results.json（ensure_ascii=False）；
#      并打印：成功几条、失败的原文是哪几条。
# 输出示例：成功处理 3 条；失败工单：['', '  ']；results.json 里是 3 个键值对
# 边界：空/纯空白工单算失败；某条失败不影响其他条；results.json 是合法 JSON 对象。
# 验收：成功数=3、失败数=2；results.json 可被 json.load 读回且只有 3 条。
# 【本题用到】函数+raise ValueError、ThreadPoolExecutor、submit/result、try/except、json.dump、'w'
# 你的代码：


# ---------- Q10【选做 · 余力再做】Q9 的 async 协程版 ----------
# 题目：把 Q9 的处理改成 async 版：async def handle_ticket_async(ticket) 用 await asyncio.sleep(0.3)，
#       空工单同样 raise ValueError；用 gather 并发，想办法让某条抛异常时其他条仍能拿到结果
#       （提示方向：gather 有一个控制"是否把异常直接抛出"的参数 return_exceptions，自己查 README/文档它怎么用），
#       最后同样汇总成功/失败并存 results_async.json。
# 验收：总耗时≈0.3s（并发）而非 3×0.3；成功 3、失败 2。
# 【本题用到】async def、await asyncio.sleep、create_task、gather(return_exceptions=...)、json
# 你的代码：


# ################################################################################
# ③ 联想微训练（只口述，每题几句话，写在下面注释里，不写完整代码，约 10 分钟）
# ################################################################################
#
# 微训练 1：RAG 要同时检索 5 个文档（全是网络等待）。用线程池还是多进程？为什么？
#           如果整个服务是 FastAPI 的 async 接口，更地道的做法是什么，前提（用什么 HTTP 库）是什么？
# 答：
#
# 微训练 2：一个函数用纯 Python 的 for 循环做几亿次数值计算（没用 numpy）。
#           开 4 个线程能变快约 4 倍吗？为什么？想利用多核该换什么？
# 答：
#
# 微训练 3：你 create_task 了 3 个协程却没 await，main 立刻结束、任务体没跑完（0.00s）。
#           该补哪一步？这说明 create_task 和 gather 各负责什么？
# 答：


# ################################################################################
# ④ 收工提交清单（做完自查，然后把本文件发我批改）
# ################################################################################
#  □ 还债：D6-Q6 retry 白纸默写已单独发我
#  □ day06 改好的 Q3/Q5/Q7 已发我复跑
#  □ W1~W5 热身亲手敲完并各"改了一个条件"
#  □ Q1~Q9 完成（Q10 选做），输出点逐条打勾
#  □ Q6/Q7/Q8（D4 换皮复测）独立写出、没翻旧代码
#  □ 联想微训练 3 题写了口述答案
#  □ 每题一句话题眼；看了提示/答案的题已标 ⚠
#
#  收工三问：输出点齐了吗？ / ⚠ 标了吗？ / 题眼写了吗？
#  说"收工"我再归档同步 GitHub；问问题时按"要实现什么/试过什么/卡在哪报什么错"描述。
