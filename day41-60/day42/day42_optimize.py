# 非常好 👍！你今天（Day 42）的三道练习都完成得不错，整体思路清晰、代码可运行、图表标签完整。我来给你做一个逐题点评与优化建议，帮你把代码提升到“更工程化”的水平：
#
# ---
import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题

### 🟩 练习1：柱状图

# ✅ **优点：**
#
# * 能正确绘制出彩色柱状图；
# * 用 `plt.text()` 显示数值，逻辑清晰；
# * 中英文标签都设置得很好。
#
# ⚙️ **优化建议：**
#
# 1. 你用数字 `[1,2,3,4,5]` 作为横轴坐标没问题，但更简洁的写法是直接用城市名作 `x`；
# 2. `plt.text()` 的写法重复度较高，可以循环自动标注；
# 3. 建议将字体颜色与柱子区分开，或使用统一黑色，更清晰。
#
# **优化写法：**


cities = ['北京', '上海', '广州', '深圳', '杭州']
values = [90, 85, 88, 92, 80]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

plt.bar(cities, values, color=colors)
for i, v in enumerate(values):
    plt.text(cities[i], v + 1, str(v), ha='center', va='bottom', fontsize=11)

plt.title("练习1：绘制柱状图")
plt.xlabel("城市")
plt.ylabel("数值")
plt.show()
# 👉 更简洁、可扩展性强。
### 🟩 练习2：饼图
#
# ✅ **优点：**
#
# * 参数设置完整；
# * 饼图比例、阴影、突出效果都有体现；
# * 标签显示正确。
#
# ⚙️ **优化建议：**
#
# * 若希望更专业的排版，可以加上 `plt.axis('equal')` 让饼图为**正圆形**；
# * 若想增加细节感，可加入“阴影深度”和“颜色映射”。
#
# **推荐写法：**


fruits = ['苹果', '橙子', '香蕉', '葡萄']
ratios = [30, 25, 25, 20]
colors = plt.cm.Set2(np.linspace(0, 1, len(fruits)))  # 使用 colormap 自动生成颜色

explode = [0.1, 0, 0, 0]
plt.pie(ratios, labels=fruits, autopct="%1.1f%%", explode=explode,
        shadow=True, startangle=90, colors=colors)
plt.axis('equal')  # 保证饼图是正圆
plt.title("练习2：绘制饼图")
plt.show()



### 🟩 练习3：直方图
#
# ✅ **优点：**
#
# * 数据生成正确；
# * 使用 `bins`、`color`、`edgecolor` 参数；
# * 标签、标题都齐全。
#
# ⚙️ **优化建议：**
#
# * 建议使用 **正态分布生成数据**，更接近真实成绩分布；
# * 可以加上网格线或透明度，使视觉更柔和；
# * 若想让分布更清晰，可以叠加平均线。
#
# **改进版：**


np.random.seed(42)
scores = np.clip(np.random.normal(70, 15, 1000), 0, 100)  # 更接近真实分布

plt.hist(scores, bins=10, color='lightcoral', edgecolor='black', alpha=0.8)
plt.axvline(scores.mean(), color='blue', linestyle='--', linewidth=2, label=f"平均分: {scores.mean():.1f}")
plt.title("成绩分布图")
plt.xlabel("分数区间")
plt.ylabel("人数")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


# ✅ **总结：**
#
# * 你的绘图逻辑掌握得很好，说明你已经熟悉 Matplotlib 的基本语法；

