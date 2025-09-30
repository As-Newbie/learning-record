import matplotlib.pyplot as plt
import numpy as np

# 练习1：绘制正弦曲线，并尝试不同 figsize
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)

# TODO: 尝试 figsize=(4,3)
plt.figure(figsize=(4, 3))
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题
plt.title("sinx figsize=(4,3)")
plt.show()

# TODO: 尝试 figsize=(8,6)
plt.figure(figsize=(8, 6))
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题
plt.title("sinx figsize=(8,6)")
plt.show()


# 练习2：尝试不同 dpi 并保存图像
# TODO: figsize=(6,4), dpi=72
plt.figure(figsize=(6,4), dpi=72)
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题
plt.title("sinx figsize=(6,4), dpi=72")
# 保存图片，例如 "sine_dpi72.png"
plt.savefig("sine_dpi72.png")
plt.show()

# TODO: figsize=(6,4), dpi=100
plt.figure(figsize=(6,4), dpi=100)
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题
plt.title("sinx figsize=(6,4), dpi=100")
# 保存图片，例如 "sine_dpi100.png"
plt.savefig("sine_dpi100.png")
plt.show()

# TODO: figsize=(6,4), dpi=300
plt.figure(figsize=(6,4), dpi=300)
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题
plt.title("sinx figsize=(6,4), dpi=300")
# 保存图片，例如 "sine_dpi300.png"
plt.savefig("sine_dpi300.png")
plt.show()


# 练习3：使用 bbox_inches="tight" 保存图像
plt.figure(figsize=(6,4), dpi=100)
# 绘制曲线
plt.plot(x,y,'r',label="sin(x)")
# 添加标题、x/y 标签
plt.title("bbox_inches='tight' ")
plt.xlabel("x axis")
plt.ylabel("y axis")
# 保存图片，例如 "sine_tight.png"，使用 bbox_inches="tight"
plt.savefig("sine_tight.png", bbox_inches="tight")
plt.show()
