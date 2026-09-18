================================================================
 D5 知识卡 · 面向对象（配套 day05_practice.py）
 2026-09-16 | 对应讲义第8章《类和对象》、第9章《三大特性》、第10章案例
 用法：热身时照「最小示例」亲手敲到 practice.py 里；做题时回查方法地图。
================================================================


────────────────────────────────────────────────
 ① 知识速整清单（先逐条用自己的话写笔记，每点配最小示例）
────────────────────────────────────────────────
 1. 类与对象：类是模具，对象是用模具压出来的月饼。class 定义类，类名() 创建对象。
 类是宏观的，抽象的。多数对象都存在的。对象，把类具体化

 2. __init__：创建对象时自动调用的初始化方法；self 不用手动传。
__init__，是初始化方法，使用时，底层启动一个构造函数

 3. self：调用  对象.方法() 时，Python 自动把这个对象传进 self（相当于 Java 的 this）。
 self，相当类的实例对象，在方法内部，通过 self 可以访问和修改对象的属性

 4. 类属性 vs 实例属性：类属性全类共享一份；实例属性每个对象各一份。
类属性：
1）通过 类名.属性名 或 实例名.属性名 访问
2）通过 类名.属性名 添加与修改类属性
3）所有该类的实例
实例属性：
1）通过 实例名.属性名 访问
2）通过 实例名.属性名 添加与修改实例属性
3）每个实例独有一份实例属性
 5. 三种方法：实例方法(带self)、类方法(@classmethod 带cls)、静态方法(@staticmethod 都不带)。
 实例方法：
     实例方法只能被实例对象调用
     可以访问实例属性、类属性、类方法。
     实例方法在类中定义，第一个参数为self，代表实例本身。
 类方法：
     在类中通过 @classmethod 定义，第一个参数为cls，代表类本身。
     类方法可以被类和实例对象调用。
     不需要实例化，就可以同过 类名.方法名 访问
静态方法：
    在类中通过 @staticmethod 定义
    不访问实例属性或类属性，只依赖于传入的参数
    通过类名或实例调用，但它不会访问类或实例的内部信息，更像是一个工具函数
    不需要实例化，就可以同过 类名.方法名 访问


 6. 封装：私有 __x（改名重整，约定别碰）、单下划线 _x（内部约定）、@property 控制读写。
 私有属性：
    通过双下划线定义私有属性
    self.__name = name
 私有方法
    通过双下划线定义私有方法。
    def __fun():
 可以通 _类名.__方法名做访问

本质是 Python 自动做了**名称改写（Name Mangling）**：把 `__方法名` 自动改成了 `_类名__方法名`

property
1）方法转换为属性
    @property
    def eat(self):
p.est

2）只读属性
@property
    def name(self):
        return self.__name
print(p.name)  # 张三
p.name = "李四"  # 报错
只能读取无法修改

3）读写属性
@property的基础上还有@name.setter 就有了修改的能力
一个是或取，一个修改。这俩为一体
 @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name




 7. 继承：class 子类(父类)；super() 调父类方法；同名方法 = 重写(override)。
单继承:
class 类名(父类):
    类体
在类名后括号内指定要继承的父类。

多继承:
class 类名(父类1, 父类2, ...):
    类体
调用方法时先在子类中查找，若不存在则从左到右依次查找父类中是否包含方法。

复用父类方法:
子类可以在类中使用 super().方法名() 或 父类名.方法名() 来调用父类的方法
1）super().方法名()
super().eat()

2）父类名.方法名()
 Person.eat(self)

方法重写:
在子类中定义与父类方法重名的方法，调用时会调用子类中重写的方法。

子类重写 __init__() 并调用时，不会执行父类的 __init__() 方法。如有必要，
需在子类 __init__() 中使用 super().__init__() 来调用父类的 __init__() 方法。

def __init__(self, name):
        self.name = name

def __init__(self, name, area):
        super().__init__(name)  # 调用父类的__init__()
        self.area = area


 8. 多态与鸭子类型：不看对象是什么类型，只看它有没有那个方法（"走起来像鸭子就是鸭子"）。
 同一事物在不同场景下呈现不同状态。

 9. 魔术方法(双下划线 dunder)：__str__/__len__/__getitem__/__call__，让自定义对象像内置类型一样好用。
 了解即可：多继承与 MRO、动态给对象加属性、__slots__ 限制属性。
前后双下划线
这类方法不许要手动调用，当执行某个特定操作时，这类方法会被自动调用
__new__\__init__:创建对象的时候会被自动调用

__del__



────────────────────────────────────────────────
 ② 方法地图（按"想干什么"查）
────────────────────────────────────────────────

【类的骨架】
  想干什么            写法
  ------------------  ------------------------------------------------
  定义类              class 类名:
  初始化属性          def __init__(self, 参数):  self.属性 = 参数
  普通实例方法        def 方法名(self, ...):   # 第一个参数永远是 self
  创建对象            obj = 类名(实参)          # 自动调 __init__
  访问属性/方法       obj.属性 / obj.方法()

  易混点：__init__ 里给 self.xxx 赋值才是"创建实例属性"；
          方法第一参数 self 只是约定名（但永远别改它）。

【类属性 vs 实例属性 —— 今天最大的坑】
                      类属性                      实例属性
  ------------------  --------------------------  --------------------------
  写在哪              类里、方法外                __init__ 里 self.x=...
  归属                所有对象共享一份            每个对象各一份
  典型用途            计数器、注册表、共享常量    对象各自的数据
  访问方式            类名.x 或 self.x            self.x

  ⚠ 坑：方法里 self.count += 1 不会改类属性！
     它会偷偷新建一个同名【实例属性】。改类属性要用 类名.count += 1
     （或 type(self).count += 1）。

【三种方法对比】
  类型        装饰器          第一参数   能访问什么          什么时候用
  ----------  --------------  ---------  ------------------  ----------------------------
  实例方法    无              self       实例属性 + 类属性   90% 的普通方法
  类方法      @classmethod    cls        类属性              计数器/注册表/备选构造
  静态方法    @staticmethod   无         都不能直接访问      逻辑属于类但不依赖状态

【封装】
  想干什么              写法/说明
  --------------------  ----------------------------------------------------
  私有属性              self.__api_key = k   外部 obj.__api_key 取不到，
                        会被改名成 _类名__api_key（君子协定，不是真锁）
  内部约定              self._cache          单下划线：告诉别人"别从外面碰"
  方法伪装成属性(读)    @property 修饰方法   访问时 obj.temperature 不加括号
  赋值时校验(写)        @属性名.setter       obj.temperature = 2 时自动执行，可 raise

【继承与多态】
  想干什么              写法/说明
  --------------------  ----------------------------------------------------
  继承                  class Qwen(BaseModel):
  调父类初始化          super().__init__(参数)
                        子类写了 __init__ 就必须显式调，否则父类属性建不出来
  重写方法              子类里定义同名方法（可选择 super().方法() 复用再追加）
  多态                  不同子类都有同名 invoke，函数里直接调，不写 if 判断类型
  判断类型              isinstance(obj, 类)：子类实例对父类也返回 True
                        type(obj) 要求类型严格相等；判断"是不是某家族"用 isinstance

【常用魔术方法（让对象支持内置函数/语法）】
  魔术方法        什么时候自动被调用          你要做的
  --------------  --------------------------  ----------------------------
  __init__        类名() 创建对象时           初始化属性，不要 return
  __str__         print(obj)、str(obj)        return 一个给人看的字符串（不是print!）
  __repr__        调试、放进容器里显示        return 给开发者看的字符串
  __len__         len(obj)                    return 整数
  __getitem__     obj[i]、obj[a:b] 切片       return 对应位置元素
  __call__        obj(...) 把对象当函数调     写调用逻辑
  实现了 __len__ + __getitem__，你的对象就能像列表一样被 len()、下标、切片、遍历 —— 这就是鸭子类型。


────────────────────────────────────────────────
 ③ 最小示例（热身 W1~W7 就照这些敲，必须亲手敲）
────────────────────────────────────────────────

# ---------- 最小示例1：类的骨架（对应 W1）----------
class Dog:
    def __init__(self, name):      # 创建对象时自动调用
        self.name = name          # 实例属性
    def bark(self):               # 实例方法，self 自动传入
        return f"{self.name}: 汪汪"

d = Dog("旺财")
print(d.bark())                   # 旺财: 汪汪


# ---------- 最小示例2：类属性 vs 实例属性（对应 W3）----------
class Dog:
    kind = "犬科"                 # 类属性，共享
    def __init__(self, name):
        self.name = name          # 实例属性，各一份

d1 = Dog("旺财")
d2 = Dog("来福")
print(Dog.kind, d1.kind, d2.kind) # 犬科 犬科 犬科
d1.kind = "柴犬"                  # 只给 d1 新建了实例属性，不影响 d2 和类
print(d1.kind, d2.kind, Dog.kind) # 柴犬 犬科 犬科


# ---------- 最小示例3：三种方法（对应 W4）----------
class Tool:
    registry = []                          # 类属性
    def __init__(self, name):
        self.name = name
    def describe(self):                    # 实例方法
        return "工具：" + self.name
    @classmethod
    def add(cls, name):                    # 类方法，cls 就是 Tool
        cls.registry.append(name)
    @staticmethod
    def help_text():                       # 静态方法，没有 self/cls
        return "Tool 是工具基类"

Tool.add("搜索")
print(Tool.registry, Tool.help_text())     # ['搜索'] Tool 是工具基类


# ---------- 最小示例4：property 校验（对应 W5）----------
class LLM:
    def __init__(self, t):
        self.temperature = t               # 注意：这行会走 setter
    @property
    def temperature(self):                 # 读：obj.temperature
        return self.__temperature
    @temperature.setter
    def temperature(self, v):              # 写：obj.temperature = v
        if not 0 <= v <= 1:
            raise ValueError("temperature 必须在 0~1 之间")
        self.__temperature = v

m = LLM(0.7)
print(m.temperature)                       # 0.7（不加括号）
# m.temperature = 2                        # 抛 ValueError


# ---------- 最小示例5：继承 + super + 重写（对应 W6）----------
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name}在吃东西"

class Bird(Animal):
    def __init__(self, name, wing):
        super().__init__(name)             # 先让父类建好 name
        self.wing = wing                   # 子类再加自己的属性
    def fly(self):
        return f"{self.name}用{self.wing}飞"
    def eat(self):                         # 重写父类方法
        return f"{self.name}啄米"

b = Bird("鹦鹉", "翅膀")
print(b.eat(), b.fly())                    # 鹦鹉啄米 鹦鹉用翅膀飞


# ---------- 最小示例6：魔术方法（对应 W7）----------
class Box:
    def __init__(self, items):
        self.items = items
    def __str__(self):
        return f"Box({len(self.items)}件)"
    def __len__(self):
        return len(self.items)

box = Box(["书", "笔", "杯子"])
print(box)                                 # Box(3件)
print(len(box))                            # 3


────────────────────────────────────────────────
 ④ 今日易错点（写代码前先扫一眼）
────────────────────────────────────────────────
 1. __str__ 必须 return 字符串；在里面 print 会得到 None。
 2. 子类写了 __init__ 却忘了 super().__init__()，父类属性全部不存在。
 3. self.count += 1 改不到类属性（见方法地图的坑）。
 4. 私有属性 __x 不是访问不到，是被改名成 _类名__x，目的是"别手滑改到"。
 5. 静态方法/类方法上面的 @ 装饰器一行都不能漏。
 6. 方法第一个参数 self 只在【定义】时写，调用 obj.f() 时不用传。
 7. 先判断"该用继承(is-a)还是组合(has-a)"：Bot 有一个 LLMClient，就持有它，别去继承它。

────────────────────────────────────────────────
 ⑤ AI 开发视角（今天学的东西以后在哪见）
────────────────────────────────────────────────
 - LangChain 里 ChatOpenAI(BaseChatModel)：继承；你要重写的方法常在子类里。
 - chain = build_chain() 后 chain("问题")：__call__。
 - 消息列表支持 len(msgs)、msgs[-1]：__len__ / __getitem__。
 - @property：SDK 里把复杂配置伪装成简单属性；@classmethod：常见于各种 from_xxx 构造。
 - 方法名前一个下划线 _generate：约定的"内部方法，外部别直接调"。
================================================================
