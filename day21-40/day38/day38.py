import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)

# 练习1：绘制正弦曲线，并限制 xlim, ylim
plt.figure(figsize=(4,3),dpi=200)
# TODO: 绘制曲线
plt.plot(x,y,'b',label="sinx")
plt.title("test1")
# TODO: 设置 xlim=[0, 2*np.pi]
plt.xlim(0,2*np.pi)
# TODO: 设置 ylim=[-0.5, 0.5]
plt.ylim(-0.5,0.5)
plt.legend()
plt.show()
# 练习2：使用 plt.axis 一次性设置范围
plt.figure(figsize=(4,3),dpi=200)
# TODO: 绘制曲线
plt.plot(x,y,'r--',label="sinx")
# TODO: 使用 plt.axis([0, 2*np.pi, -1, 1])
plt.axis([0, 2*np.pi, -1, 1])
plt.title("test2")
plt.legend()
plt.show()
# 练习3：比较 axis("equal") 与 axis("tight")
plt.figure(figsize=(4,3),dpi=200)
# TODO: 绘制曲线
plt.plot(x,y,'g:',label="sinx")
# TODO: 使用 plt.axis("equal")
plt.axis("equal")
plt.title("test3.1 equal")
plt.legend()
plt.show()

plt.figure(figsize=(4,3),dpi=200)
# TODO: 绘制曲线
plt.plot(x,y,'y-.',label="sinx")
# TODO: 使用 plt.axis("tight")
plt.axis("tight")
plt.title("test3.2 tight")
plt.legend()
plt.show()


# 练习4：画一个圆，使用 set_aspect 保持比例
theta = np.linspace(0, 2*np.pi, 500)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

fig, ax = plt.subplots()
# TODO: 在 ax 上绘制圆
ax.plot(x_circle,y_circle)
# TODO: 使用 ax.set_aspect('equal')
ax.set_aspect('equal')
ax.set_title("test4 set_aspect")
plt.show()
