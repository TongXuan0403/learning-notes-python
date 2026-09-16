知识点	                        讲义小节	                        你要交的笔记要点
函数的定义与调用	                函数的概念 / 定义 / 抽取调用	        def 语法、函数名规则、先定义后调用
形参 vs 实参、参数传递	            参数的抽取 / 形参实参 / 传递	        值传递 vs 引用传递的区别
参数的五种形式	                    函数可使用的参数形式	            见下方
解包传参 / 强制位置・关键字参数	    解包传参 / 强制...	               *list、**dict 解包；/ 和 * 的位置
返回值	                        返回值 / 函数说明文档               无 return 返回 None；多值返回是元组；docstring
变量作用域	                    全局 / 局部 /global/nonlocal	    局部优先、global 改全局、nonlocal 改外层
递归	                            概念 / 本质 / 阶乘 / 执行流程	    递归三要素：出口 + 递推式 + 规模缩小
匿名函数 lambda	                匿名函数	                        语法、作为内置函数参数（sorted/max）
map()                           函数对序列中元素逐一处理。
filter()                        函数对序列中元素过滤
reduce()                        函数对序列中元素进行累积。


定义和调用
想干什么	             写法	                    最小示例	                            易混点
定义函数	             def 名(参数):体	            def add(a,b): return a+b	        函数体必须缩进；先定义再调用
返回结果	             return 值	                return a+b	                        不写 return 返回 None
返回多个	             return a, b	            return a+b, a-b	                    本质返回元组，用 x, y = f() 解包
写说明	             """docstring"""	        函数体第一行	                        用 help(函数名) 查看


参数五种形式
形式	            语法	                   什么时候用	                   最小示例
位置参数	        def f(a, b)	           参数少、顺序固定	               f(1, 2)
默认参数	        def f(a, b=10)	       某些参数大多数时候固定	       f(1) → b=10
关键字参数	    f(b=2, a=1)	           调用时不怕顺序乱	               f(a=1, b=2) 与 f(b=2, a=1) 等价
可变位置参数	    def f(*args)	       任意个位置参数，打包成元组	       f(1,2,3) → args=(1,2,3)
可变关键字参数	    def f(**kwargs)	       任意个 "名字 = 值"，打包成字典   f(name='A', age=9) → kwargs={'name':'A',...}


作用域
想干什么	                关键字	            示例
修改全局变量	            global	            def f(): global x; x = 10
修改外层 (非全局) 变量	    nonlocal	        嵌套函数里改外层函数局部变量




文件操作 + 异常 + JSON

①知识速整清单
知识点	            讲义位置	                    笔记要点
文件概念与路径	        文件基本概念	                文本 / 二进制；绝对路径 vs 相对路径
打开与关闭	        打开与关闭	                open 三参数、mode 表、为什么要 close
with 关键字（重点）	异常章・with	                自动关闭、异常也关，以后一律用 with
读写	                文件读写	                    write/writelines、read/readline/readlines
异常体系	            异常介绍	                    语法错误 vs 运行时异常；常见异常类型
捕获结构	            try except/else/finally	    四段各自什么时候执行
抛出与断言	        raise/assert	            主动抛、调试断言
异常传递	            异常的传递	                函数内不捕获会一层层往上抛
json 模块	        补充                         dump/dumps/load/loads 四兄弟



② 方法地图
文件操作
想干什么	        写法	                        最小示例	                         易混点
打开文件	        open(路径, mode,             open('a.txt','r'                 不写 encoding 在 Windows 上可能乱码
                encoding='utf-8')	       ,encoding='utf-8')

安全打开（首选）	with open(...) as f:	缩进内操作，出缩进自动关	                不用手写 close
模式 r/w/a	    'r'读 'w'覆盖写 'a'追加 'b'二进制		                  'w' 一打开就清空原文件！文件不存在时 r 报错、w/a 会新建
写字符串	        f.write(s)	                f.write('hello\n')	        返回字符数；不会自动换行，自己加 \n
写多行	        f.writelines(列表)		同样不自动加换行，先把每行拼好 \n
全读	            f.read()	                一个大字符串	                    小文件用
读一行	        f.readline()	              含行尾 \n
读所有行	        f.readlines()	          得到 ['行1\n','行2\n']	                一次性进内存
逐行读（首选）	    for line in f:	            大文件 / 日志不爆内存	                line 带 \n，用 .strip() 去

选型对比 —— 怎么读？
小文件随便；大文件（日志、训练数据）只用 `for line in f`，因为 `read()/readlines()` 会把整个文件载入内存。



异常处理
想干什么	                写法	                                         易混点
试一段可能出错的代码	    try: ... except 类型: ...	    别写裸 except:，会连 Ctrl+C 都吞掉，至少 except Exception
一次捕多种	            except (ValueError, KeyError) as e:	         as e 拿到错误描述，可 print(e)
没出错才执行	            else:	                                     只有 try 成功才走
无论如何都执行	            finally:	                                 常用于兜底关资源
主动抛错	                raise ValueError("消息")
调试断言	                assert 条件, "不满足时提示"	                 条件为 False 抛 AssertionError

必认的 6 个异常：
`FileNotFoundError` 文件不存在
`KeyError` 字典没这个键
`IndexError` 列表越界
`ValueError` 值非法（如 `int('abc')`）
`TypeError` 类型不对
`ZeroDivisionError` 除以 0。




json

想干什么	                写法	                                            记忆 / 易混
字典 → JSON 字符串	json.dumps(obj, ensure_ascii=False, indent=2)	    s = string；ensure_ascii=False
                                                                        让中文不变成 \uXXXX；indent 缩进美化
JSON 字符串 → 字典	json.loads(s)	                                    s = string，输入是字符串
字典 → 写进文件	    json.dump(obj, f, ensure_ascii=False, indent=2)	    没 s，参数里给文件对象
文件 → 字典	        json.load(f)	                                    没 s，从文件对象读
类型对应	            dict↔object、list↔array、True↔true、None↔null	    JSON 里的 true/null 是小写，别和 Python 混

函数	                        作用
json.dumps(obj)	            Python 对象 → json 字符串（dump string）
json.loads(s)	            json 字符串 → Python 对象（load string）
json.dump(obj, fp)	        Python 对象 → 写入json 文件
json.load(fp)	            读取 json 文件 → Python 对象

json_str = json.dumps(data, indent=2, ensure_ascii=False)   indent=2表示缩进2格，ensure_ascii=False中文显示







