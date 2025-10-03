import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体和解决负号显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
x = np.linspace(-5, 5, 200)
y = x**2
plt.plot(x, y)
plt.title("练习1：文本标记")
# TODO: 在 (0,0) 添加文本 "原点"
plt.text(0,0,"原点",fontsize=12,color='red',ha='center',va='center')
plt.show()
# 你用了 ha='center', va='center'，很好地让文字和点对齐，这样不会出现偏移。
# 小优化：如果希望和点稍微错开一点，可以加上 xytext + annotate，避免文字和曲线重叠。
x = np.linspace(0, 2*np.pi, 200)
y = np.cos(x)

plt.plot(x, y,"b-")
plt.title("练习2：箭头注释")
# TODO: 在 cos(x) 最小值点添加注释
plt.annotate("最小值点",color="red",xy=(np.pi,-1),xytext=(np.pi+1,-1+0.3),arrowprops=dict(arrowstyle="->",color="red"))
plt.show()
# 小优化：箭头的样式 arrowstyle 可以换成 "fancy" 或 "simple"，视觉效果会更明显。
# arrowprops=dict(arrowstyle="fancy", color="red")
x = np.linspace(0, 5, 200)
y = np.exp(-x)

plt.plot(x, y)
plt.title("练习3：文本框样式")
# TODO: 在 (2, exp(-2)) 添加带背景框的文本
plt.text(2,np.exp(-2),"衰减点",fontsize=15,color='red',bbox=dict(facecolor="green",alpha=0.5,boxstyle="square",))
plt.show()
# 小优化：boxstyle 除了 "square"，还可以试 "round" 或 "round,pad=0.5"，让边框更美观。
# bbox=dict(facecolor="green", alpha=0.5, boxstyle="round,pad=0.5")


