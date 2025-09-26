import numpy as np
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目1：tile 与 repeat
# (a) 用 np.tile 生成数组 [1,2,3,1,2,3,1,2,3]
# (b) 用 np.repeat 生成数组 [1,1,1,2,2,2,3,3,3]
a1=np.tile([1,2,3],3)
b1=np.repeat([1,2,3],3)
print(f"两个数组分别为:\n{a1}\n{b1}")
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目2：where 条件选择
# 给定数组 a = np.array([10, 15, 20, 25, 30])
# (a) 把大于20的元素替换成1，否则替换成0
# (b) 把小于等于15的元素替换成-1，其余保持原值
a2=np.array([10, 15, 20, 25, 30])
b2=np.copy(a2)
a2_a=np.where(b2>20,1,0)
print(f"a2把大于20的元素替换成1，否则替换成0:\n{a2_a}")
b2_b=np.where(a2<=15,-1,a2)
print(f"a2把小于等于15的元素替换成-1，其余保持原值:\n{b2_b}")
# 题目3：nonzero
# 给定数组 b = np.array([0,3,0,4,5,0])
# 找出所有非零元素的索引，并提取这些元素
a3=np.array([0,3,0,4,5,0])
nonzero_indices = np.nonzero(a3)
nonzero_elements = a3[np.nonzero(a3)]
print(f"所有非零元素的索引，并提取这些元素:索引为：\n{nonzero_indices}\n提取的元素为：\n{nonzero_elements}")
# 题目4：集合类操作
# (a) 找出数组 [1,2,2,3,4,4,5] 的唯一值
a = np.array([1, 2, 2, 3, 4, 4, 5])
unique_a = np.unique(a)
print("(a) 唯一值:", unique_a)
# (b) 判断 [2,6,7] 是否在 [1,2,3,4,5] 中
arr1 = np.array([2, 6, 7])
arr2 = np.array([1, 2, 3, 4, 5])
result = np.isin(arr1, arr2)
print("（b）判断结果:", result)
# (c) 求 [1,2,3,4] 和 [3,4,5,6] 的交集
c1 = np.array([1, 2, 3, 4])
c2 = np.array([3, 4, 5, 6])
intersection = np.intersect1d(c1, c2)
print("(c) 交集:", intersection)
