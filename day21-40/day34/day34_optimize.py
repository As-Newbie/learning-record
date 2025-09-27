import numpy as np
import os

# 创建输出目录
os.makedirs("output_day34", exist_ok=True)

print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目1：npy 文件读写
# (a) 创建一个 3x3 数组 arr = np.arange(9).reshape(3,3)，保存为 "test.npy"
# (b) 重新读取文件并打印数组
arr1 = np.arange(9).reshape(3, 3)
np.save("output_day34/test.npy", arr1)

arr2 = np.load("output_day34/test.npy")
print(f"arr2 为：\n{arr2}")

print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目2：txt 文件读写
# (a) 创建一个 1D 数组 arr = np.linspace(0,1,5)，保存为 "test.csv"，逗号分隔
# (b) 重新读取并打印数组
arr3 = np.linspace(0, 1, 5)
np.savetxt("output_day34/test.csv", arr3, delimiter=",", fmt="%.3f")

arr4 = np.loadtxt("output_day34/test.csv", delimiter=",")
print(f"arr4 为：\n{arr4}")

print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目3：npz 多数组保存
# (a) 创建两个数组 a = np.array([1,2,3])，b = np.array([4,5,6])
# (b) 保存到同一个 "multi.npz" 文件
# (c) 重新读取，并分别打印 a 和 b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.savez("output_day34/multi.npz", a=a, b=b)

with np.load("output_day34/multi.npz") as data:
    print("a 为：", data["a"])
    print("b 为：", data["b"])
