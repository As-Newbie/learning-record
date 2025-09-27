import numpy as np
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目1：npy 文件读写
# (a) 创建一个 3x3 数组 arr = np.arange(9).reshape(3,3)，保存为 "test.npy"
# (b) 重新读取文件并打印数组
arr1=np.arange(9).reshape(3,3)
np.save("day34_test_1.npy",arr1)
arr2=np.load("day34_test_1.npy")
print(f"arr2为\n{arr2}")
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目2：txt 文件读写
# (a) 创建一个 1D 数组 arr = np.linspace(0,1,5)，保存为 "test.csv"，逗号分隔
# (b) 重新读取并打印数组
arr3=np.linspace(0,1,5)
np.savetxt("day34_test_2.csv",arr3,delimiter=",")
arr4=np.loadtxt("day34_test_2.csv",delimiter=",")
print(f"arr4为\n{arr4}")
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目3：npz 多数组保存
# (a) 创建两个数组 a = np.array([1,2,3])，b = np.array([4,5,6])
# (b) 保存到同一个 "multi.npz" 文件
# (c) 重新读取，并分别打印 a 和 b
a = np.array([1,2,3])
b = np.array([4,5,6])
np.savez("day34_multi.npz",a=a,b=b)
arr5=np.load("day34_multi.npz")
arr5_a=arr5["a"]
arr5_b=arr5["b"]
print(f"a为\n{arr5_a}")
print(f"b为\n{arr5_b}")
# 小优化建议：
#
# 1. **存储路径灵活化**
#    你现在的 `"day34_test_1.npy"` 会存到脚本运行目录下，如果想放到指定文件夹，可以这样：
#    ```python
#    import os
#    os.makedirs("output", exist_ok=True)  # 确保目录存在
#    np.save("output/day34_test_1.npy", arr1)
#    ```
# 2. **读取时的 with 语句（推荐写法）**
#    读取 `.npz` 时，最好加 `with`，这样用完会自动关闭文件句柄：
#    ```python
#    with np.load("day34_multi.npz") as data:
#        print("a:", data["a"])
#        print("b:", data["b"])
#    ```
# 3. **保存 CSV 时控制小数格式**
#    默认 `np.savetxt` 会保存很多小数位，可以加 `fmt` 参数：
#    ```python
#    np.savetxt("day34_test_2.csv", arr3, delimiter=",", fmt="%.3f")
#    ```
#    👉 就会只保留 3 位小数，更整齐。
