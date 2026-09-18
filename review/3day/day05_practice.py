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
import json


# ---------- W1 类、__init__、self、实例方法 ----------
# 跟写：照 README【最小示例1】敲 Dog 类：属性 name；bark(self) 返回 f"{self.name}: 汪汪"
#       创建 d = Dog("旺财")，打印 d.bark()
# 微调：仿写 Cat 类，meow(self) 返回 f"{self.name}: 喵"，创建对象调用。

# 你的代码：
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def bark(self):
#         return f"{self.name}"
# d = Dog("旺财")
# print(d.bark())



# ---------- W2 亲眼看 self ----------
# 跟写：在 bark 方法里加一行 print(self)；方法外 print(d)，对比两个输出的内存地址。
# 结论（一句话写这）：self 到底是谁？
# self就是实例本身
# 使用d.bark，就等于是用Dog.bark(d),d作为参数传给了self

# 你的代码：

# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def bark(self):
#         print(self,id(self))
#         return f"{self.name}"
#
# d = Dog("gou")
# print(d,id(d))
#
# print(d.bark())


# ---------- W3 类属性 vs 实例属性 ----------
# 跟写：照 README【最小示例2】敲：类属性 kind = "犬科"，实例属性 name；
#       创建 d1、d2，打印 Dog.kind / d1.kind / d2.kind
# 微调：执行 d1.kind = "柴犬" 后，再打印 d1.kind、d2.kind、Dog.kind，
#       哪些变了哪些没变？写一句解释。
# 只有d1这个实例对象变化，可能会创建或修改实例属性

# 你的代码：
# class Dog:
#     kind = "犬科"
#     def __init__(self, name):
#         self.name = name
#     def bark(self):
#         return f"{self.name}"
#
# d1 = Dog("d1")
# d2 = Dog("d2")
# d1.kind = "柴犬"
# print(Dog.kind)
# print(d1.kind)
# print(d2.kind)





# ---------- W4 三种方法同台 ----------
# 跟写：照 README【最小示例3】敲一个类，里面各放 1 个实例方法、
#       1 个 @classmethod、1 个 @staticmethod，并全部调用成功。

# 你的代码：
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def person(self):
#         return "这里是实例方法"
#     @classmethod
#     def class_method(cls):
#         return "这里是类方法"
#     @staticmethod
#     def static_method():
#         return "这里是静态方法"
# p = Person("张三")
# print(p.name)
# print(p.person())
# print(p.class_method())
# print(p.static_method())



# ---------- W5 @property 数据校验 ----------
# 跟写：照 README【最小示例4】敲 temperature 的 property + setter 校验（合法 0~1）。
# 微调：把合法范围改成 0~2，尝试赋值 3，确认抛出 ValueError 并截图/贴出报错。

# 你的代码：
# class LLM:
#     def __init__(self,temperature):
#         self.__temperature = temperature
#     @property
#     def temperature(self):
#         return self.__temperature
#     @temperature.setter
#     def temperature(self,t):
#         if not 0 <= t <= 1:
#             raise ValueError("应该在0-1之间")
#         self.__temperature = t
#
# llm = LLM(0.7)
# print(llm.temperature)
# llm.temperature = 2




# ---------- W6 继承、super、方法重写 ----------
# 跟写：照 README【最小示例5】敲 Animal/Bird，跑通 eat() 和 fly()。
# 微调：把 super().__init__(name) 这行注释掉再运行，观察报什么错、为什么。
# Bird这个类中找不到name这一属性
# 你的代码：
# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         return f"{self.name}吃"
#
#
# class Bird(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def eat(self):
#         return f"{self.name}chi,{self.age}kg"
#     def fly(self):
#         return f"{self.name}fei,{self.age}kg"
#
# b = Bird("a","b")
# print(b.eat(), b.fly())


# ---------- W7 魔术方法初体验 ----------
# 跟写：写 Box 类，__init__ 接收一个列表存为 self.items；
#       实现 __str__（返回 f"Box({len(self.items)}件)"）和 __len__（返回物品数量）。
# 验证：print(box) 和 len(box) 都能正常工作。

# 你的代码：

# class Box:
#     def __init__(self,items):
#         self.items = items
#     def __str__(self):
#         return f"Box({len(self.items)}件)"
#     def __len__(self):
#         return len(self.items)
# b = Box([1,2,3,4,5])
# print(b)
# print(len(b))



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

# class Message:
#     def __init__(self,role,content):
#         self.role = role
#         self.content = content
#     def show(self):
#         return f"{self.role}: {self.content}"
#
# u1 = Message("user","你好")
# u2 = Message("assistant","在的")
# u3 = Message("user","讲个笑话")
# print(u1.show())
# print(u2.show())
# print(u3.show())



# ---------- Q2【基础】让 print 直接好看 ----------
# 给 Q1 的 Message 加 __str__，使 print(m) 输出 [user] 你好 格式。
# 对比实验：先故意不加 __str__ 打印一次对象，把 <__main__.Message object at 0x...> 也贴上来。
# 边界：__str__ 里用 return，不能用 print。
# 【本题用到】__str__、f-string
# user: 你好,assistant: 在的,user: 讲个笑话

# 你的代码：

# class Message:
#     def __init__(self,role,content):
#         self.role = role
#         self.content = content
#     def __str__(self):
#         return f'[{self.role}]: {self.content}'
#     def show(self):
#         return f"{self.role}: {self.content}"
#
# u1 = Message("user","你好")
# u2 = Message("assistant","在的")
# u3 = Message("user","讲个笑话")
# print(f"{u1.show()},{u2.show()},{u3.show()}")
# print(u1,u2,u3)

# <__main__.Message object at 0x00000201049F96A0> <__main__.Message object at 0x0000020104AD4B90>
# <__main__.Message object at 0x0000020104AD4F50>



# ---------- Q3【基础】类属性计数器（含坑实验）----------
# 定义 ChatSession 类：类属性 count = 0，每创建一个实例计数 +1。
# 实验①：__init__ 里写 self.count += 1，创建3个实例后分别打印 ChatSession.count
#        和某个实例的 count，观察结果。
#
# 实验②：改成 ChatSession.count += 1（或 type(self).count += 1），再观察。
# 输出：两组实验结果 + 一句话解释①为什么不对。
# 1     1 和 0
#   类名.类属性名  返回的是类属性
#   实例名.类属性名    会进到__init__中，返回实例属性,也只是当前对象的实例属性
# 2     3 和 3
#   类属性就类似公共数据库，不同实例实例都可以去访问，修改

# 【本题用到】类属性、实例属性、__init__、type(self)
# 你的代码：

# class ChatSession:
#     count = 0
#     def __init__(self, number):
#         self.count += 1
#         self.number = number
#
# d1 = ChatSession(1)
# d2 = ChatSession(2)
# d3 = ChatSession(3)
# print(d1.count)
# print(ChatSession.count)

# class ChatSession:
#     count = 0
#     def __init__(self, number):
#         ChatSession.count += 1
#         self.number = number
#
# d1 = ChatSession(1)
# d2 = ChatSession(2)
# d3 = ChatSession(3)
# print(d1.count)
# print(ChatSession.count)



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
# class LLMClient:
#     def __init__(self,api_key,model="qwen",t=0.7):
#         self.__api_key = api_key
#         self.model = model
#         self.__temperature = t
#
#     def show_key(self):
#         last4 = self.__api_key[-4:]  #对短 key 不会报错，只会取整段
#         return f"sk-***{last4}"
#     @property
#     def temperature(self):
#         return self.__temperature
#     @temperature.setter
#     def temperature(self, value):
#         if not 0 <= value <= 1:
#             raise ValueError("temperature must be between 0 and 1")
#         self.__temperature = value
#     def chat(self,prompt):
#         return f"[{self.model}] 对「{prompt}」的回复（temperature={self.temperature}）"
#
# client = LLMClient("sk-8a3b2f1e9d0c7b6a")
# print(client.show_key())
# print(client.temperature)
# print(client.chat("你好"))
#
# print(client.__api_key)
#
# client.temperature = 2
# print(client.temperature)



# ---------- Q5【进阶·AI场景】模型家族：继承 + 多态 ----------
# 基类 BaseModel：__init__(self, model_name)；invoke(self, prompt)
#   返回 f"{model_name} 收到：{prompt}"
# 子类 QwenModel、DeepSeekModel：构造无参数（内部固定模型名，用 super 传给父类），
#   重写 invoke：Qwen 返回 "通义千问：{prompt}"，DeepSeek 返回 "深度求索：{prompt}"
# 再写普通函数 run(model, prompt)：函数体内【不许做任何类型判断】，直接 return model.invoke(prompt)
# 验收：run(QwenModel(),"你好")、run(DeepSeekModel(),"你好") 输出不同；
#       口述：为什么 run 不需要知道传进来的是哪个类？run 只要求对象 "有 invoke 方法"（鸭子类型），不检查它是哪个类
# 【本题用到】继承、super().__init__、方法重写、多态

# 你的代码：
# class BaseModel:
#     def __init__(self,model_name):
#         self.model_name = model_name
#     def invoke(self,prompt):
#         return f"{self.model_name} 收到：{prompt}"
#
# class QwenModel(BaseModel):
#     def __init__(self):
#         super().__init__("通义千问")
#     def invoke(self,prompt):
#         return f"通义千问：{prompt}"
#
# class DeepSeekModel(BaseModel):
#     def __init__(self):
#         super().__init__("深度求索")
#     def invoke(self,prompt):
#         return f"深度求索：{prompt}"
#
# def run(model,prompt):
#     return model.invoke(prompt)
#
# if __name__ == "__main__":
#     base_model = BaseModel("通用模型")
#     print(run(base_model, "测试请求"))
#     qwen = QwenModel()
#     print(run(QwenModel(), "你好"))
#     print(run(=DeepseekModel(), "你好"))

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

# class Tool:
#     registry =[]
#     def __init__(self,name):
#         self.name = name
#     def describe(self):
#         return f"工具：" + self.name
#     @classmethod
#     def add(cls,name):
#         cls.registry.append(name)
#     @staticmethod
#     def help():
#         return "Tool 是工具基类"
#
# Tool.add("搜索")
# Tool.add("计算器")
# t1= Tool("锤子")
# t2= Tool("榔头")
# print(Tool.registry)
# print(t1.describe())
# print(t2.describe())

# ---------- Q7【进阶】魔术方法打造对话历史容器 ----------
# 定义 History 类，内部用私有列表 self.__items 存消息（字符串或字典均可）
#   add(self, msg)：追加一条
#   __len__：len(history) 返回条数
#   __getitem__：支持 history[0]、history[-1]、history[0:2] 切片（委托给内部列表）
#   __str__：返回 "History（n 条消息）"
# 验收：add 3条后，len、正向下标、负向下标、切片、print 全部可用。
# 【本题用到】__len__、__getitem__、__str__、列表委托 self.__items[i]

# 你的代码：

# class History:
#     def __init__(self):
#         self.__items = []
#     def add(self,msg):
#         self.__items.append(msg)
#     def __len__(self):
#         return len(self.__items)
#     def __getitem__(self,idx):
#         return self.__items[idx]
#     def __str__(self):
#         return f"History（{len(self)} 条消息）"


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

# 你的代码：q4的实现加历史纪录保存，聊天记录是循环的

class LLMClient:
    def __init__(self,api_key,model="qwen",temperature=0.7):
        self.__api_key = api_key
        self.model = model
        self.__temperature = temperature
    def chat(self, prompt):
        return f"[{self.model}] 对「{prompt}」的回复（temperature={self.temperature}）"
    def show_key(self):
        last4 = self.__api_key[-4:]
        return f"sk-***{last4}"
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, value):
        if not 0 <= value <= 1:
            raise ValueError("temperature must be between 0 and 1")
        self.__temperature = value
# LLMClient 只管 "生成回复"，Bot 才管 "记历史 + 调度"
class Bot:
    def __init__(self,api_key):
        self.client = LLMClient(api_key)
        self.history = []
    def talk(self,user_text):
        self.history.append({"role":"user","content":user_text})
        reply = self.client.chat(user_text)
        self.history.append({"role":"assistant","content":reply})
        return reply
    def __str__(self):
        return f"Bot（已对话 {len(self.history) // 2} 轮）"

if __name__ == "__main__":
    bot = Bot(api_key="")
    while True:
        text = input()
        if text == "q":
            break
        reply = bot.talk(text)
    with open("chat_history.json","w",encoding="utf-8") as f:
        json.dump(bot.history,f,ensure_ascii=False)



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
# 父类把 invoke 定义成 "必须实现的接口"，直接 raise 是强制子类兑现
# ②
# Q5 是 "父类给默认实现、子类可直接用或重写"，Q9 是 "父类不给实现、不重写就报错"
# ③
#忘了实现，一调用就抛 `NotImplementedError`，让错误立刻暴露而不是静默跑出错误结果。

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
# 什么机制：q5的使用某个模型，然后返回对于内容
#下划线 _generate 暗示这是一个私有方法，简单警告，允许访问
# 2. 1000个用户共用同一个 API Key，Key 存类属性还是实例属性？各自的对话历史呢？
# 答：
#key存类属性,这样各实例对象都能去访问这个api key,各自对话历史存在对于对话对象中，防止内容混乱
#
# 3. Q8 的 Bot 是"有一个"LLMClient（组合），而不是"是一个"LLMClient（继承）。
#    一句话说清 has-a 和 is-a 怎么选。
# 答：
# 做一个完整的bot用组合，多功能，连发。继承，拓展功能延展用


# ============================================================
#  提交清单（收工自查）
#  [ ] W1~W7 跟写+微调全部跑通
#  [ ] Q1~Q8 完成（Q9/Q10 选做）
#  [ ] 每题运行输出贴在题目下方
#  [ ] 联想3题写了口述答案
#  [ ] 明早 D4 四题白纸还债已记在待办
# ============================================================
#（注：内容由AI生成）
