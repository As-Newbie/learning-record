import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
# 1️⃣ 数据准备
days = np.arange(1, 8)  # 星期 1~7
temps = np.array([33,34,32,29,30,31,35])  # 请填入或生成一周平均气温
# 区分工作日和周末
workday_indices = [0, 1, 2, 3, 4]  # 周一到周五
weekend_indices = [5, 6]           # 周六、周日
# 2️⃣ 绘制折线图 + 散点图
plt.figure(figsize=(8, 5), dpi=100)

# 绘制工作日数据
plt.plot(days[workday_indices], temps[workday_indices],
         marker='o', color='orange', linewidth=2, label='工作日气温')

# 绘制周末数据
plt.plot(days[weekend_indices], temps[weekend_indices],
         marker='o', color='green', linewidth=2, label='周末气温')
# 散点标记也按颜色区分
plt.scatter(days[workday_indices], temps[workday_indices], color='red', s=50, zorder=5)
plt.scatter(days[weekend_indices], temps[weekend_indices], color='darkgreen', s=50, zorder=5)
# 3️⃣ 添加标题与标签
plt.title('一周气温变化趋势')
plt.xlabel('星期')
plt.ylabel('气温 (℃)')

# 4️⃣ 标注最高温和最低温
max_temp = np.max(temps)
min_temp = np.min(temps)
max_day = days[np.argmax(temps)]
min_day = days[np.argmin(temps)]
# 标记最高温度
plt.text(max_day, max_temp+0.5, f'最高: {max_temp}℃',
         color='red', ha='center', fontsize=10,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# 标记最低温度
plt.text(min_day, min_temp-0.5, f'最低: {min_temp}℃',
         color='blue', ha='center', fontsize=10,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# 5️⃣ 美化与保存
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(days, ['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
plt.ylim(25, 40)  # 设置y轴范围
# 添加填充区域
plt.fill_between(days, 28, 33, color='orange', alpha=0.1, label='舒适区间')

plt.fill_between(days, temps, min_temp-2, color='skyblue', alpha=0.2)
plt.suptitle('城市气温监测报告', fontsize=14, fontweight='bold')
plt.title('一周气温变化趋势（单位：℃）', fontsize=12)
plt.text(1, 26, '数据来源：模拟生成', fontsize=8, alpha=0.7)

plt.legend(loc='upper right')
plt.tight_layout()  # 自动调整布局
plt.savefig('weekly_temperature.png', dpi=200, bbox_inches='tight')
plt.show()
