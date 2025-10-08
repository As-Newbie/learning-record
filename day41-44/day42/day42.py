import matplotlib.pyplot as plt
import numpy as np
# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
# 练习1：绘制柱状图
# 数据：城市 = ['北京', '上海', '广州', '深圳', '杭州']
# 数值 = [90, 85, 88, 92, 80]
# 要求：设置不同颜色，并在每个柱顶显示具体数值（可用 plt.text）
# TODO
city=[1, 2, 3, 4, 5]
city_values=[90, 85, 88, 92, 80]
colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
plt.bar(city,city_values,color=colors)
plt.text(1,92,"北京",fontsize=12,color="#1f77b4",ha="center",va="center")
plt.text(2,87,"上海",fontsize=12,color="#ff7f0e",ha="center",va="center")
plt.text(3,90,"广州",fontsize=12,color="#2ca02c",ha="center",va="center")
plt.text(4,94,"深圳",fontsize=12,color="#d62728",ha="center",va="center")
plt.text(5,82,"杭州",fontsize=12,color="#9467bd",ha="center",va="center")
plt.title("练习1：绘制柱状图")
plt.xticks([1, 2, 3, 4, 5],['北京', '上海', '广州', '深圳', '杭州'])
plt.xlabel("city")
plt.ylabel("values")
plt.show()
# 练习2：绘制饼图
# 数据：水果 = ['苹果', '橙子', '香蕉', '葡萄']
# 比例 = [30, 25, 25, 20]
# 要求：显示百分比（保留1位小数），并突出“苹果”部分
# TODO
fruits=['苹果', '橙子', '香蕉', '葡萄']
fruits_ratio=[30, 25, 25, 20]
colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
explode=[0.1,0,0,0]# 突出第1块
plt.pie(fruits_ratio,labels=fruits,autopct="%1.1f%%",explode=explode, shadow=True, startangle=90)
# autopct="%1.1f%%"
# 控制饼图各部分百分比的显示格式：%1.1f%%表示保留 1 位小数（如 30.0%）。
# xplode=explode控制某部分是否"突出"显示（远离中心）。 explode是一个列表，例如 [0, 0.1, 0]表示第二块（香蕉）突出 0.1 个单位距离。
# shadow=True为饼图添加阴影效果，使图表更具立体感。
# startangle=90设置饼图的起始角度（默认 0°，即从右侧开始）。startangle=90表示从顶部（12 点钟方向）开始绘制。
plt.title("练习2：绘制饼图")
plt.show()


# 练习3：绘制直方图
# 数据：随机生成 1000 个 0~100 的成绩
# 要求：分为 10 个区间，设置颜色、边框，并显示标题“成绩分布图”
# TODO
grade=np.random.randint(0,101,1000)
# # 生成 1000 个 0~100 的浮点数（保留 2 位小数）
# grade = np.round(np.random.uniform(0, 100, 1000), 2)

# print(grade[:5])  # 示例输出: [84.37, 12.95, 56.28, 99.99, 3.14]
# scores = np.clip(np.random.normal(loc=70, scale=15, size=1000), 0, 100).astype(int)
# np.random.normal(loc=70, scale=15, size=1000)
# 生成 1000 个 符合正态分布的随机数。
# loc=70：均值（μ）为 70，表示成绩集中在 70 分附近。
# scale=15：标准差（σ）为 15，表示成绩的离散程度较大（约 68% 数据在 55~85 之间）。
# size=1000：生成 1000 个数据点。
# np.clip(..., 0, 100)
# 将数据 限制在 [0, 100] 范围内，超出部分会被截断：
# 例如，生成的值是 105→ 强制改为 100；-5→ 改为 0。
# .astype(int)将浮点数转换为 整数（成绩通常为整数）。
plt.hist(grade, bins=10, color='lightcoral', edgecolor='black')
# bins=20将数据分成20 个等宽区间（柱子的数量）。
# color='lightcoral'设置柱子的填充颜色为浅珊瑚色（lightcoral）。支持颜色名称（如 'skyblue'）、十六进制值（如 '#FF5733'）或 RGB 元组。
# edgecolor='black'设置柱子边缘颜色为黑色，使柱子之间界限更清晰。
plt.title("成绩分布图")
plt.xlabel("数值区间")
plt.ylabel("频数")
plt.show()