# ✏️ 今日练习题
# 题目1：基本随机数
# 用 rand 生成一个 3×3 矩阵。
# 用 randn 生成一个 3×3 矩阵。
# 用 randint 生成 10 个 [1,100) 的随机整数。
# 题目2：抽样
# 创建数组 arr = np.array([10,20,30,40,50])，
# 用 choice 随机抽取 3 个数（可重复）。
# 再随机抽取 3 个数（不可重复）。
# 题目3：洗牌
# 创建数组 arr = np.arange(10)。
# 用 shuffle 打乱它，并观察原数组是否变化。
# 用 permutation 打乱它，并观察原数组是否变化。
# 题目4（进阶）：模拟掷骰子
# 用 randint 模拟掷一个骰子 10 次，输出结果。
# 用 randint 模拟同时掷两个骰子 1000 次，统计点数和为 7 的次数。
# （提示：统计时可以用 np.sum 和布尔索引）
import numpy as np
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
a1=np.random.rand(3,3)
print(f"用 rand 生成一个 3×3 矩阵(均匀分布随机数)\n{a1}")
b1=np.random.randn(3,3)
print(f"用 randn 生成一个 3×3 矩阵(标准正态分布随机数 均值为0 标准差为1)\n{b1}")
c1=np.random.randint(1,100,10)
print(f"用 randint 生成 10 个 [1,100) 的随机整数\n{c1}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
arr_2 = np.array([10,20,30,40,50])
a2=np.random.choice(arr_2, 3, True)
print(f"可重复随机抽取的3个数:\n{a2}")
b2=np.random.choice(arr_2,3,False)
print(f"不可重复随机抽取的3个数:\n{b2}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
arr_3 = np.arange(10)
a3=np.copy(arr_3)
np.random.shuffle(a3)
print(f"原数组为\n{arr_3}\n打乱后为\n{a3}")
b3=np.random.permutation(arr_3)
print(f"原数组为\n{arr_3}\n打乱后为\n{b3}")
# shuffle：原地操作，直接修改原数组,无返回，无法直接赋值给变量
# permutation：非原地操作，返回新数组而不修改原数组
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
a4=np.random.randint(1,7,10)
print(f"投掷骰子10的结果为\n{a4}")
np.random.seed(42)
dice1 = np.random.randint(1, 7, size=1000)
dice2 = np.random.randint(1, 7, size=1000)
sums = dice1 + dice2
count_7 = np.sum(sums == 7)
unique, counts = np.unique(sums, return_counts=True)
count = counts[unique == 7][0]
# unique == 7 → [False, False, False, True]  # 创建布尔掩码
# counts[mask] → [3]                         # 用掩码提取值
# [0] → 3                                    # 从数组中取出标量
print(f"\n掷两个骰子1000次的结果:\n{sums}")
print("点数和为7的次数:", count_7)
print(f"求和去重的数组为\n{unique}\n各个点数和的次数:\n{counts}\n其中和为7的次数为：{count}" )
unique_1, counts_1 = np.unique(sums, return_counts=True)
print("\n所有点数和及其出现次数:")
for val, cnt in zip(unique_1, counts_1):
    print(f"和={val}: {cnt}次 ({cnt/1000:.3f})")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目4结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")

