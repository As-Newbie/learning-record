from cProfile import label

import matplotlib.pyplot as plt
import numpy as np
# 1. 用 numpy 生成从 0 到 2π 的 100 个点，绘制 sin(x) 的曲线。
#    要求：加上 x 轴、y 轴标签，并设置标题为 "Sine Function"。
a1=np.linspace(0,2*np.pi,100)
y1=np.sin(a1)
plt.plot(a1,y1,'g-',label="sin(x)",linewidth=2)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Sine Function")
plt.legend(loc="upper right")
plt.show()

# 2. 在同一张图里绘制 sin(x) 和 cos(x) 两条曲线，并添加图例区分。
y2=np.cos(a1)
plt.plot(a1, y1,'g-', label="sin(x)")   # 给第一条曲线起名
plt.plot(a1, y2,'r-', label="cos(x)")   # 给第二条曲线起名
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Sine and Cosine")
plt.legend(loc="upper right")
plt.show()
# 3. 随机生成 50 个点 (x,y)，x 和 y 都在 [0,10] 范围内，用散点图画出来。
x3=np.random.uniform(0,10,50)
y3=np.random.uniform(0,10,50)
plt.scatter(x3,y3,c='steelblue',    # 点颜色
    alpha=0.7,        # 透明度
    s=80,             # 点大小
    edgecolor='white', # 点边缘颜色
    linewidth=1 )      # 边缘线宽
# 唯一的小问题：在某些环境（比如 Jupyter 或新版 Matplotlib）里，edgecolor='white' 和 alpha<1 组合可能会有一个小警告（因为 scatter 默认 marker='o' 是填充形状）。
# 如果想避免，可以改成：
# plt.scatter(x3, y3, c='steelblue', alpha=0.7, s=80, edgecolors='white', linewidth=1)
# 注意这里是 edgecolors，不是 edgecolor）
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("random 50 point1")
plt.show()
# 4. 额外挑战：把第 3 题的散点点颜色设置为红色，点的大小设置为 50。
plt.scatter(x3,y3,c='red',    # 点颜色
    alpha=0.7,        # 透明度
    s=50,             # 点大小
    edgecolor='white', # 点边缘颜色
    linewidth=1 )      # 边缘线宽
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("random 50 point2")
plt.show()
