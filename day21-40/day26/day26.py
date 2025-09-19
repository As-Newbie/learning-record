# 题目1：一维聚合
# a = np.arange(1, 11)  # [1,2,...,10]
# 计算 a 的总和、均值、最大值、最小值。
# 找出最大值和最小值的索引。
# 计算 a 的标准差和方差。
# 题目2：二维数组 axis 基础
# m = np.arange(1, 13).reshape(3, 4)
# 计算整个矩阵的和与均值。
# 计算每列的和（axis=0）。
# 计算每行的均值（axis=1）。
# 找出每列的最大值。
# 题目3：高维数组
# x = np.arange(24).reshape(2, 3, 4)
# 计算整个数组的和。
# 沿 axis=0 计算和，结果形状是多少？
# 沿 axis=1 计算最大值，结果形状是多少？
# 沿 axis=2 计算均值，结果形状是多少？
# 题目4（思考题）
# 在深度学习中，输入数据常常是形状 (batch, channels, height, width) 的 4D 张量。
# 如果我们想：
# 计算每张图片的平均像素值，应该在哪个 axis 上取均值？
# 计算整个 batch 的平均像素值，应该在哪些 axis 上取均值？
# 题目1
import numpy as np
print(f"————————————————————————————题目1开始————————————————————————————")
a1=np.arange(1,11)
a1_sum=np.sum(a1)
a1_ave=np.mean(a1)
a1_max=np.max(a1)
a1_min=np.min(a1)
print(f"a1({a1})的总和为{a1_sum}、均值为{a1_ave}、最大值为{a1_max}、最小值为{a1_min}")
num_max=np.argmax(a1)
num_min=np.argmin(a1)
print(f"最大值{a1_max}的索引是{num_max}\n最小值{a1_min}的索引为{num_min}")
a1_standard_deviation=np.std(a1)
a1_variance=np.var(a1)
print(f"a1的标准差为{a1_standard_deviation}，方差为{a1_variance}")
print(f"————————————————————————————题目1结束————————————————————————————")
print(f"————————————————————————————题目2开始————————————————————————————")
a2 = np.arange(1, 13).reshape(3, 4)
a2_sum_total=np.sum(a2)
a2_ave_total=np.mean(a2)
print(f"a2\n{a2}\n总和为\n{a2_sum_total}\n均值为{a2_ave_total}")
a2_sum_columns=np.sum(a2,axis=0)
a2_sum_rows=np.sum(a2,axis=1)
print(f"a2\n{a2}\n每列的和为\n{a2_sum_columns}\n每行的和为\n{a2_sum_rows}")
a2_max_columns=np.max(a2,axis=0)
a2_max_rows=np.max(a2,axis=1)
print(f"a2\n{a2}\n每列的最大值为\n{a2_max_columns}\n每行的最大值为\n{a2_max_rows}")
a2_min_columns=np.min(a2,axis=0)
a2_min_rows=np.min(a2,axis=1)
print(f"a2\n{a2}\n每列的最小值为\n{a2_min_columns}\n每行的最小值为\n{a2_min_rows}")
print(f"————————————————————————————题目2结束————————————————————————————")
print(f"————————————————————————————题目3开始————————————————————————————")
a3 = np.arange(24).reshape(2, 3, 4)
a3_sum_total=np.sum(a3)
a3_ave_total=np.mean(a3)
print(f"a3\n{a3}\n总和为\n{a3_sum_total}\n均值为\n{a3_ave_total}")
a3_sum_axis_0=np.sum(a3,axis=0)
a3_sum_axis_1=np.sum(a3,axis=1)
a3_sum_axis_2=np.sum(a3,axis=2)
a3_max_axis_1=np.max(a3,axis=1)
a3_ave_axis_2=np.mean(a3,axis=2)
print(f"a3\n{a3}\n"
      f"沿 axis=0 计算和，结果是\n{a3_sum_axis_0}\n形状为{a3_sum_axis_0.shape}\n"
      f"沿 axis=1 计算和，结果是\n{a3_sum_axis_1}\n形状为{a3_sum_axis_1.shape}\n"
      f"沿 axis=2 计算和，结果是\n{a3_sum_axis_2}\n形状为{a3_sum_axis_2.shape}\n"
      f"沿 axis=1 计算最大值，结果是\n{a3_max_axis_1}\n形状为{a3_max_axis_1.shape}\n"
      f"沿 axis=2 计算均值，结果是\n{a3_ave_axis_2}\n形状为{a3_ave_axis_2.shape}\n")
print(f"————————————————————————————题目3结束————————————————————————————")
'''1. 计算每张图片的平均像素值
目标：为批次中的每一张独立的图片计算一个平均值。
结果形状：应该是 (batch, channels)或者 (batch,)。因为我们为每个批次、每个通道（可选）都计算了一个值。
应该在哪个 axis 上取均值？
应该在 height (axis=2) 和 width (axis=3) 这两个维度上取均值。
操作： mean(axis=(2, 3))
解释： 对于批次中的每一张图片(batch)，对于它的每一个颜色通道(channels)，我们将其所有行(height)和所有列(width)的像素值压缩（求平均），最终得到每个通道的一个代表值。'''

'''2. 计算整个 batch 的平均像素值
目标：将整个批次的所有图片视为一个整体，计算一个全局平均值。
结果形状：通常是一个单一的标量值（形状为 ()），或者按通道得到的多个值（形状为 (channels,)）。
应该在哪些 axis 上取均值？
应该在 batch (axis=0)、height (axis=2) 和 width (axis=3) 这三个维度上取均值。
操作： mean(axis=(0, 2, 3))
解释： 我们计算了所有图片(batch)、所有行(height)、所有列(width)的像素值的平均值。这个操作通常在每个通道上独立进行，所以最终会得到每个通道的全局平均值。'''


