"""
来源：Python-100-Days（骆昊）Day06
题目：猜数字游戏

要求：计算机出一个 1 到 100 之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
"""
"""
猜数字小游戏

Version: 1.0
Author: 骆昊
"""
import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')
