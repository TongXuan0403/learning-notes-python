"""# 商品价格50，若余额小于50则提示“余额不足，请充值”，最后打印“欢迎下次光临”。

from random import randint

# 余额
balance = randint(0, 100)
# 价格
price = 50
# 打印余额
print(f"余额：{balance}")
# 比较余额和价格
if balance < price:
    print("余额不足，请充值")
print("欢迎下次光临")

# 简单的语句组:你也可以在同一行的位置上使用if条件判断语句，例如
var = 100
if (var == 100) : print(f"{var}" ,end = "")
print("  Good")

from random import randint

balance = randint(0, 100)
price = 50

print(f"余额{balance}")
if balance < price:
    print("余额不足，请充值")
else:
    balance -= price
    print(f"消费成功,余额:{price}")
print("欢迎下次光临")


from random import randint

print("age=", age := randint(1,100))

if age < 2 :
    print("这是婴儿")
elif age < 4:
    print("是幼儿")
elif age < 13:
    print("是儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")
"""






