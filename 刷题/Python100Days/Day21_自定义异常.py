"""
来源：Python-100-Days（骆昊）
示例：自定义异常类型——InputError 继承 ValueError，配合递归求阶乘触发并捕获。
"""
# ---- 代码块6 ----
class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

# ---- 代码块7 ----
flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)
