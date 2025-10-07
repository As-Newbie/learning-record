import numpy as np
import matplotlib.pyplot as plt

# 设置中文与负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1️⃣ 生成 1000 个符合正态分布的数据
# 平均值 0，标准差 1
data = np.random.normal(0, 1000, 1000)

# 2️⃣ 绘制直方图
plt.figure(figsize=(8, 5), dpi=100)
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('正态分布数据直方图')
plt.xlabel('数值')
plt.ylabel('频数')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 生成数据
np.random.seed(0)
x = np.linspace(0, 10, 50)
y = 2.5 * x + 5 + np.random.normal(0, 10, size=50)  # 加上噪声

# 线性回归拟合（用polyfit）
coef = np.polyfit(x, y, 1)
trend = np.poly1d(coef)

# 绘制
plt.figure(figsize=(8, 5), dpi=100)
plt.scatter(x, y, color='dodgerblue', alpha=0.6, label='原始数据')
plt.plot(x, trend(x), color='red', linewidth=2, label=f'趋势线: y={coef[0]:.2f}x+{coef[1]:.2f}')
plt.title('带噪声的线性数据与趋势线')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()