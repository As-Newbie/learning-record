import matplotlib.pyplot as plt
import numpy as np
from setuptools.command.rotate import rotate

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Exercise 1: Basic Scale")
# TODO: 设置 x 轴刻度为 0, π/2, π, 3π/2, 2π，并显示对应的文字标签
plt.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],[ "0", "π/2", "π", "3π/2", "2π"])
# 提示：用 np.pi 可以得到 π
# TODO: 设置 y 轴刻度为 -1, -0.5, 0, 0.5, 1
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.show()

x = np.arange(1, 8)
y = [5, 6, 7, 8, 7, 6, 5]

plt.plot(x, y, marker="o")
plt.title("Exercise 2: Custom Tags")
# TODO: 设置 x 轴刻度为 1-7，并把标签改成 ['一月','二月',...,'七月']
# TODO: 设置标签旋转 45 度
months=['January', 'February', 'March', 'April', 'May', 'June', 'July']
plt.xticks([1,2,3,4,5,6,7],months,rotation=45)
plt.show()
from matplotlib.ticker import ScalarFormatter, FuncFormatter

x = np.linspace(0, 1e6, 100)
y = x**2

plt.plot(x, y)
plt.title("Exercise 3: Scientific Notation and Formatting")
# TODO: 尝试不做任何设置，看默认的刻度显示
# TODO: 使用 ScalarFormatter() 把 y 轴改为普通数值显示
formatter = ScalarFormatter(useMathText=False)
formatter.set_scientific(False)
plt.gca().yaxis.set_major_formatter(formatter)
plt.show()
# 💡 更常见的写法是：
#
# plt.gca().yaxis.set_major_formatter(ScalarFormatter())
#
#
# 如果还要保证显示完整数值，可以加：
#
# plt.ticklabel_format(style='plain', axis='y')

x = np.linspace(0, 1e6, 100)
y = x**2

plt.plot(x, y)
plt.title("Exercise 3: Scientific Notation and Formatting")
# TODO: 使用 FuncFormatter，把 y 轴显示为 “某数值K”，例如 1000 显示为 1K
formatter1=FuncFormatter(lambda val,pos:f"{int(val/1000)}K")
plt.gca().yaxis.set_major_formatter(formatter1)
plt.yticks(rotation=45,fontsize=7)
plt.show()
# 💡 这里强制 int(val/1000) 会把小数截断，比如 1500 会显示成 1K。
# 如果希望更准确，可以用四舍五入：
# formatter1 = FuncFormatter(lambda val, pos: f"{val/1000:.1f}K")
x = np.logspace(0.1, 2, 100)  # 10^0.1 ~ 10^2
y = x**2

plt.plot(x, y)
plt.title("Exercise 4: Logarithmic Coordinates")
# TODO: 把 x 轴设置为 log 坐标
plt.xscale("log")
# TODO: 把 y 轴设置为 log 坐标
plt.yscale("log")
plt.show()

