"""
来源：Python-100-Days（骆昊）Day15
题目：数据统计

假设样本数据保存一个列表中，设计计算样本数据描述性统计信息的函数。描述性统计信息通常包括：
- 算术平均值（均值）：所有数据之和 / 数据个数
- 中位数：排序后取中间位置的值（偶数个取中间两个的平均）
- 极差：最大值 - 最小值
- 方差：各数据与均值之差的平方和 / (n-1)
- 标准差：方差的算术平方根
- 变异系数：标准差 / 均值
"""
def ptp(data):
    """极差（全距）"""
    return max(data) - min(data)


def mean(data):
    """算术平均"""
    return sum(data) / len(data)


def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])


def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)


def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5


def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)


def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')
