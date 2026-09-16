# ============================================================
#  D5 练习册 · 面向对象（2026-09-16）
#  配套知识卡：day05_README.txt（建议 PyCharm 左右分屏：左 README，右本文件）
#  今日流程：① 热身跟写 W1~W7（约1h）→ ② 正式题 Q1~Q10（约4~5h）→ ③ 联想微训练（口述）
#  做完直接保存本文件发我，不用另存。
# ============================================================
#
#  【每日作战卡 · 第1周 v1】
#  开做前四步：①先写样例明确输入输出 ②中文写步骤(写成注释) ③查知识卡方法地图 ④最简样例先跑通
#  卡住纪律：15分钟不看答案——写清卡在哪一步、翻知识卡、先写个笨版本；来问我只给方向
#  今日待还债 ⚠：明早(D6开工前)合上资料，白纸重写 D4 的 Q4/Q6/Q7/Q8（约30分钟）
#  今日盯防：self 到底是谁；类属性 vs 实例属性；__str__ 里是 return 不是 print
#  收工三问：输出点齐吗？ 看提示的题标 ⚠ 了吗？ 每题写题眼(一句话)了吗？
#
# ============================================================
#  第一部分 · 基础热身跟写（先做，约1h）
#  做法：打开 README，照着「最小示例」亲手敲一遍并运行，再完成每条的「微调」。
#       必须敲，不要复制；微调部分是防止"只跑demo不过脑"的关键。
# ============================================================

# ---------- W1 类、__init__、self、实例方法 ----------
# 跟写：照 README【最小示例1】敲 Dog 类：属性 name；bark(self) 返回 f"{self.name}: 汪汪"
#       创建 d = Dog("旺财")，打印 d.bark()
# 微调：仿写 Cat 类，meow(self) 返回 f"{self.name}: 喵"，创建对象调用。

# 你的代码：


# ---------- W2 亲眼看 self ----------
# 跟写：在 bark 方法里加一行 print(self)；方法外 print(d)，对比两个输出的内存地址。
# 结论（一句话写这）：self 到底是谁？


# 你的代码：


# ---------- W3 类属性 vs 实例属性 ----------
# 跟写：照 README【最小示例2】敲：类属性 kind = "犬科"，实例属性 name；
#       创建 d1、d2，打印 Dog.kind / d1.kind / d2.kind
# 微调：执行 d1.kind = "柴犬" 后，再打印 d1.kind、d2.kind、Dog.kind，
#       哪些变了哪些没变？写一句解释。

# 你的代码：


# ---------- W4 三种方法同台 ----------
# 跟写：照 README【最小示例3】敲一个类，里面各放 1 个实例方法、
#       1 个 @classmethod、1 个 @staticmethod，并全部调用成功。

# 你的代码：


# ---------- W5 @property 数据校验 ----------
# 跟写：照 README【最小示例4】敲 temperature 的 property + setter 校验（合法 0~1）。
# 微调：把合法范围改成 0~2，尝试赋值 3，确认抛出 ValueError 并截图/贴出报错。

# 你的代码：


# ---------- W6 继承、super、方法重写 ----------
# 跟写：照 README【最小示例5】敲 Animal/Bird，跑通 eat() 和 fly()。
# 微调：把 super().__init__(name) 这行注释掉再运行，观察报什么错、为什么。

# 你的代码：


# ---------- W7 魔术方法初体验 ----------
# 跟写：写 Box 类，__init__ 接收一个列表存为 self.items；
#       实现 __str__（返回 f"Box({len(self.items)}件)"）和 __len__（返回物品数量）。
# 验证：print(box) 和 len(box) 都能正常工作。

# 你的代码：


# ============================================================
#  第二部分 · 正式题目 Q1~Q10（每题先走四步法，再动手）
#  规则：每题只给【本题用到】的方法名，不给步骤；卡15分钟再来问。
# ============================================================

# ---------- Q1【基础】消息类 ----------
# 定义 Message 类：实例属性 role、content；实例方法 show() 返回 "role: content"。
# 输入：代码内创建3个对象（user/你好、assistant/在的、user/讲个笑话）
# 输出示例：user: 你好
# 验收：3个对象相互独立，改一个不影响其他。
# 【本题用到】class、__init__、self、实例方法、return

# 你的代码：


# ---------- Q2【基础】让 print 直接好看 ----------
# 给 Q1 的 Message 加 __str__，使 print(m) 输出 [user] 你好 格式。
# 对比实验：先故意不加 __str__ 打印一次对象，把 <__main__.Message object at 0x...> 也贴上来。
# 边界：__str__ 里用 return，不能用 print。
# 【本题用到】__str__、f-string

# 你的代码：


# ---------- Q3【基础】类属性计数器（含坑实验）----------
# 定义 ChatSession 类：类属性 count = 0，每创建一个实例计数 +1。
# 实验①：__init__ 里写 self.count += 1，创建3个实例后分别打印 ChatSession.count
#        和某个实例的 count，观察结果。
# 实验②：改成 ChatSession.count += 1（或 type(self).count += 1），再观察。
# 输出：两组实验结果 + 一句话解释①为什么不对。
# 【本题用到】类属性、实例属性、__init__、type(self)

# 你的代码：


# ---------- Q4【进阶·AI场景】封装一个 LLMClient ----------
# 构造参数：api_key(字符串)、model 默认 "qwen"、temperature 默认 0.7
# 要求：
#   1) api_key 设为私有属性；show_key(self) 返回脱敏字符串，只露后4位，形如 "sk-***1234"
#   2) temperature 用 @property + setter 校验：不在 0~1 就 raise ValueError
#   3) chat(self, prompt) 返回 f"[{self.model}] 对「{prompt}」的回复（temperature={self.temperature}）"
# 验收：chat("你好") 输出正确；client.temperature = 2 抛出 ValueError；
#       直接访问 client.__api_key 报什么错也贴上来。
# 边界：key 不足4位时也要能正常运行（自己决定怎么处理，注释说明）。
# 【本题用到】私有属性、@property、@x.setter、raise ValueError、切片、f-string

# 你的代码：


# ---------- Q5【进阶·AI场景】模型家族：继承 + 多态 ----------
# 基类 BaseModel：__init__(self, model_name)；invoke(self, prompt)
#   返回 f"{model_name} 收到：{prompt}"
# 子类 QwenModel、DeepSeekModel：构造无参数（内部固定模型名，用 super 传给父类），
#   重写 invoke：Qwen 返回 "通义千问：{prompt}"，DeepSeek 返回 "深度求索：{prompt}"
# 再写普通函数 run(model, prompt)：函数体内【不许做任何类型判断】，直接 return model.invoke(prompt)
# 验收：run(QwenModel(),"你好")、run(DeepSeekModel(),"你好") 输出不同；
#       口述：为什么 run 不需要知道传进来的是哪个类？
# 【本题用到】继承、super().__init__、方法重写、多态

# 你的代码：


# ---------- Q6【基础】三种方法同台 ----------
# 定义 Tool 类：类属性 registry = []
#   实例方法 describe(self)：返回 "工具：" + self.name（name 在 __init__ 给）
#   类方法 add(cls, name)：把 name 加进 cls.registry
#   静态方法 help_text()：无参数，返回固定字符串 "Tool 是工具基类"
# 验收：建2个实例；Tool.add("搜索")、Tool.add("计算器")；
#       打印 Tool.registry 和两个实例各自的 describe；
#       口述 classmethod 与 staticmethod 的区别（谁带 cls、谁能改类属性）。
# 【本题用到】@classmethod、@staticmethod、实例方法、类属性

# 你的代码：


# ---------- Q7【进阶】魔术方法打造对话历史容器 ----------
# 定义 History 类，内部用私有列表 self.__items 存消息（字符串或字典均可）
#   add(self, msg)：追加一条
#   __len__：len(history) 返回条数
#   __getitem__：支持 history[0]、history[-1]、history[0:2] 切片（委托给内部列表）
#   __str__：返回 "History（n 条消息）"
# 验收：add 3条后，len、正向下标、负向下标、切片、print 全部可用。
# 【本题用到】__len__、__getitem__、__str__、列表委托 self.__items[i]

# 你的代码：


# ---------- Q8【综合·AI场景】简易对话机器人（串联 D3~D5）----------
# 定义 Bot 类：
#   __init__：持有一个 LLMClient（可复用Q4，或简化成 model 名字符串）和一段历史（列表或Q7的History）
#   talk(self, user_text)：
#       把 {"role":"user","content":user_text} 加入历史
#       调 client.chat 得到回复
#       把 {"role":"assistant","content":回复} 加入历史
#       return 回复
#   __str__：返回 "Bot（已对话 n 轮）"，轮数 = 消息数 // 2
# 主程序：创建 bot；while + input 循环，输入 q 退出，每轮打印回复；
#   退出时用 json 把完整历史存到 chat_history.json
# 选做增强（强烈建议）：启动时先 load 该文件（不存在从 [] 开始），
#   实现关掉程序再打开，上一轮对话还在（复用 D4 的 Q8 姿势）。
# 验收：聊3轮后文件里有6条消息；选做：第二次运行能看到上次历史。
# 【本题用到】组合(对象里持有对象)、__init__、__str__、json.dump/load、FileNotFoundError、input循环

# 你的代码：


# ---------- Q9【选做·读代码题，口述不写实现】----------
# 读下面代码，回答3个问题（答案写在下面注释里）：
#
#   class BaseLLM:
#       def invoke(self, prompt):
#           raise NotImplementedError("子类必须实现 invoke")
#   class ChatQwen(BaseLLM):
#       def invoke(self, prompt):
#           return "千问回复：" + prompt
#   b = ChatQwen()
#   print(b.invoke("你好"))
#
# 问题①：父类 invoke 为什么不写具体逻辑、而是直接抛异常？
# 问题②：这和 Q5 的基类（父类给了默认实现）相比，是哪两种设计思路？
# 问题③：新子类忘了实现 invoke 会怎样？这种设计保护了什么？

# 你的回答：
# ①
# ②
# ③


# ---------- Q10【选做】__call__：把对象当函数调 ----------
# 给 Q4 的 LLMClient 加 __call__(self, prompt)，内部 return self.chat(prompt)，
# 使 client("你好") 与 client.chat("你好") 等价。
# 验收：两种调用输出一致；口述 LangChain 里 chain("问题") 为什么能直接跑。
# 【本题用到】__call__

# 你的代码：


# ============================================================
#  第三部分 · 联想微训练（只口述/写几句，不写完整代码，约10分钟）
# ============================================================
# 1. 以后看 LangChain 文档出现 class ChatOpenAI(BaseChatModel) 和 def _generate(self,...)：
#    用今天知识猜这是什么机制？方法名前一个下划线 _generate 暗示什么？
# 答：
#
# 2. 1000个用户共用同一个 API Key，Key 存类属性还是实例属性？各自的对话历史呢？
# 答：
#
# 3. Q8 的 Bot 是"有一个"LLMClient（组合），而不是"是一个"LLMClient（继承）。
#    一句话说清 has-a 和 is-a 怎么选。
# 答：


# ============================================================
#  提交清单（收工自查）
#  [ ] W1~W7 跟写+微调全部跑通
#  [ ] Q1~Q8 完成（Q9/Q10 选做）
#  [ ] 每题运行输出贴在题目下方
#  [ ] 联想3题写了口述答案
#  [ ] 明早 D4 四题白纸还债已记在待办
# ============================================================
#（注：内容由AI生成）
