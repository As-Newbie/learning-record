# 题目1：排序与索引
# 创建 a = np.array([7, 2, 5, 2, 9, 1])
# 1. 对 a 排序并输出结果。
# 2. 输出排序后的索引。
# 3. 使用排序后的索引重建排序结果（手动用索引取值）。
# 题目2：唯一值
# 创建 b = np.array([1,2,2,3,4,4,4,5])
# 1. 输出唯一值。
# 2. 输出每个值的出现次数。
# 题目3：拼接与拆分
# 创建 m1 = np.arange(1,7).reshape(2,3)，m2 = np.arange(7,13).reshape(2,3)
# 1. 行拼接 m1 和 m2。
# 2. 列拼接 m1 和 m2。
# 3. 将行拼接的结果，按行拆分成两个矩阵。
# 4. 将列拼接的结果，按列拆分成三个矩阵。
# 题目4（加分）：综合应用
# 创建 x = np.array([10, 20, 20, 30, 10, 40, 30])
# 1. 找出 x 的唯一值和对应的次数。
# 2. 对唯一值进行排序。
# 3. 拼接唯一值和次数，形成一个二维数组 [[值, 次数], ...]。
import numpy as np
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
a1=np.array([7, 2, 5, 2, 9, 1])
b1=a1.copy()
# 先创建副本然后排序
c1=np.sort(a1)
# 直接用给新的变量赋值
print(f"对 a1 排序并输出结果\n{np.sort(b1)}\n{c1}")
# 两种方式输出一样
d1=c1.argsort()
print(f"对 a1 排序后的索引为\n{b1.argsort()}\n{d1}")
# 这时候副本的索引值并非预期
e1=a1[a1.argsort()]
print(f"使用索引重建的排序结果\n{e1}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
a2=np.array([1,2,2,3,4,4,4,5])
a2_vals, a2_counts = np.unique(a2, return_counts=True)
# a2_vals返回去除重复值后的数组并排序 a2_counts返回每个唯一值出现的次数
vals, indices = np.unique(a2, return_index=True)
print(vals, indices)  # indices 是第一次出现的位置
print(f"对 a2 去重并排序后为\n{a2_vals}\n每个唯一值出现的次数为\n{a2_counts}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
m1 = np.arange(1,7).reshape(2,3)
m2 = np.arange(7,13).reshape(2,3)
m1_m2_rows=np.concatenate([m1,m2],axis=0)
# 行拼接
m1_m2_columns=np.concatenate([m1,m2],axis=1)
# 列拼接
print(f"m1\n{m1}\n和m2\n{m2}\n行拼接后的结果为\n{m1_m2_rows}\n列拼接的结果为\n{m1_m2_columns}")
m1_m2_vstack=np.vstack([m1,m2])
# 垂直拼接
m1_m2_hstack=np.hstack([m1,m2])
# 水平拼接
print(f"垂直拼接后的结果为\n{m1_m2_vstack}\n水平拼接的结果为\n{m1_m2_hstack}")
# 注意 vstack 等价于 axis=0，hstack 等价于 axis=1。
# np.vsplit 和 np.hsplit 返回的是列表（list），所以打印出来有方括号。
# 如果要单独拿第一个，可以用 split_rows[0]。
split_rows=np.vsplit(m1_m2_rows,2)
# 将行拼接的结果，按行拆分成两个矩阵
split_columns=np.hsplit(m1_m2_columns,3)
# 将列拼接的结果，按列拆分成三个矩阵
print(f"将行拼接的结果，按行拆分成两个矩阵的结果为\n{split_rows}\n"
      f"将列拼接的结果，按列拆分成三个矩阵的结果为\n{split_columns}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目4开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 创建数组
x = np.array([10, 20, 20, 30, 10, 40, 30])
print("原始数组:", x)
# 1. 找出x的唯一值和对应的次数
unique_values, counts = np.unique(x, return_counts=True)
print("唯一值:", unique_values)
print("对应次数:", counts)
# 2. 对唯一值进行排序
sorted_unique = np.sort(unique_values)
print("排序后的唯一值:", sorted_unique)
# 3. 拼接唯一值和次数，形成一个二维数组
result = np.column_stack((sorted_unique, counts))
print("二维数组:")
print(result)
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目4结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")

# 如果以后遇到“统计唯一值和次数”的需求，可以封装成一个小函数：

def unique_with_counts(arr):
    vals, counts = np.unique(arr, return_counts=True)
    return np.column_stack((vals, counts))
# 调用
print(unique_with_counts([10,20,20,30,10,40,30]))

print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷补充∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 使用不同方法拼接数组：np.column_stack、np.hstack 和 np.concatenate
import numpy as np

# 创建数组
x = np.array([10, 20, 20, 30, 10, 40, 30])
unique_values, counts = np.unique(x, return_counts=True)

print("唯一值:", unique_values)
print("对应次数:", counts)

# 方法1: 使用 np.column_stack (原始方法)
result1 = np.column_stack((unique_values, counts))
print("\n使用 np.column_stack:")
print(result1)

# 方法2: 使用 np.hstack (需要先调整数组形状)
# 需要先将一维数组转换为列向量
unique_col = unique_values.reshape(-1, 1)
counts_col = counts.reshape(-1, 1)
result2 = np.hstack((unique_col, counts_col))
print("\n使用 np.hstack:")
print(result2)

# 方法3: 使用 np.concatenate (需要先调整数组形状)
result3 = np.concatenate((unique_col, counts_col), axis=1)
print("\n使用 np.concatenate:")
print(result3)




