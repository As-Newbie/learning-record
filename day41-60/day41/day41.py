import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(2*x)

# 练习1：绘制 y1, y2 曲线，要求：
# (1) y1 使用自定义虚线样式 (0, (5, 2, 1, 2))
# (2) y2 使用 marker='^'，颜色 #FF7F0E，标记边框黑色
plt.figure(figsize=(6,4))
# TODO
plt.plot(x,y1,label="sinx",linestyle=(0, (5, 2, 1, 2)))
plt.plot(x, y2, color='#FF7F0E', marker='^',
         markeredgecolor='black', label='sin(2x)')

plt.title("Exercise 1: Lines and Marking Styles")
plt.legend()
plt.show()


# 练习2：绘制散点图
# 数据：x, y = np.random.rand(100), np.random.rand(100)
# 使用 cmap='plasma'，点透明度 0.6，并添加颜色条
# TODO
np.random.seed(2568)
x2,y3= np.random.rand(100), np.random.rand(100)
colors=x2+y3
# 数值映射颜色
plt.scatter(x2, y3, c=colors, cmap='plasma', alpha=0.6, edgecolor='black', linewidths=0.3)

plt.title("Color mapping example:plasma")
plt.colorbar(label="value")
plt.show()


# 练习3：绘制多条曲线，使用 alpha 渐变（从 0.2 到 1.0）
# 提示：可用循环绘制多条正弦曲线 y = sin(kx)，k=1~5
# TODO
# 生成 x 数据
x = np.linspace(0, 2*np.pi, 100)
# 创建图形
plt.figure(figsize=(8, 6))
alphas = np.linspace(0.2, 1.0, 5)  # 生成5个alpha值：0.2, 0.4, 0.6, 0.8, 1.0
colors = plt.cm.viridis(np.linspace(0, 1, 5))  # 使用viridis色彩映射生成5种颜色

for k in range(1, 6):  # k = 1, 2, 3, 4, 5
    y = np.sin(k * x)  # 计算 y = sin(kx)
    alpha_value = alphas[k-1]  # 对应的透明度
    color = colors[k-1]  # 对应的颜色
    plt.plot(x, y,
             alpha=alpha_value,  # 设置透明度
             color=color,  # 设置颜色
             linewidth=2,  # 线条宽度
             label=f'y = sin({k}x)')  # 图例标签
# 你可以考虑让颜色与透明度同步控制，例如使用 zip()：
#
# for k, (alpha_value, color) in enumerate(zip(alphas, colors), start=1):
#     y = np.sin(k * x)
#     plt.plot(x, y, color=color, alpha=alpha_value, linewidth=2, label=f'y = sin({k}x)')
#
#
# 更 Pythonic，一行处理对应参数。
plt.title("练习3：多条正弦曲线的Alpha渐变效果")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)  # 添加网格线，透明度0.3
plt.show()

