import numpy as np
import matplotlib.pyplot as plt
# 设置中文与负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置
np.random.seed(42)
days = np.arange(1, 101)  # 100 天
price = np.zeros(100)
price[0] = 100  # 初始价格

# 模拟每日涨跌：平均涨幅 0.1，波动标准差 2
for i in range(1, 100):
    change = np.random.normal(-0.2, 1)
    price[i] = price[i-1] + change

# 绘图
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(days, price, color='teal', linewidth=2, label='股票价格走势')
plt.scatter(days, price, s=15, color='orange', alpha=0.6)

# 标注最高/最低价
max_idx = np.argmax(price)
min_idx = np.argmin(price)
plt.text(days[max_idx], price[max_idx]+1, f'最高: {price[max_idx]:.2f}', color='red', ha='center')
plt.text(days[min_idx], price[min_idx]-2, f'最低: {price[min_idx]:.2f}', color='blue', ha='center')

plt.title('模拟股票价格波动曲线')
plt.xlabel('天数')
plt.ylabel('价格（元）')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
