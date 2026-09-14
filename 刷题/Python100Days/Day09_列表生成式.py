"""
来源：Python-100-Days（骆昊）
示例：列表生成式（comprehension）与传统 for 循环对比，用一行代码生成满足条件的列表。
"""
# ---- 代码块6 ----
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

# ---- 代码块7 ----
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

# ---- 代码块8 ----
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)

# ---- 代码块9 ----
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)
