import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1=np.sin(x)
y2=np.cos(x)
y3=np.sin(2*x)
y4=np.cos(2*x)
# 题目1：
# 使用 plt.subplot 生成 2 行 1 列的子图
# 在第一个子图画 sin(x)，在第二个子图画 cos(x)
plt.subplot(2,1,1)
plt.plot(x,y1,'r',label="sin(x)")
plt.legend(loc="lower left")
plt.subplot(2,1,2)
plt.plot(x,y2,'b',label="cos(x)")
plt.legend(loc="lower left")
plt.show()
# 题目2：
# 使用 plt.subplots 生成 1 行 2 列的子图
# 左边画 y = sin(x)，右边画 y = sin(2x)
fig2,axes2=plt.subplots(1,2)
axes2[0].plot(x,y1,'r--',label="sin(x)")
axes2[0].set_title("sin(x)")
axes2[0].legend(loc="lower left")
axes2[1].plot(x,y3,'c-.',label="sin(2x)")
axes2[1].set_title("sin(2x)")
axes2[1].legend(loc="lower left")
plt.tight_layout()  # 自动调整子图间距
plt.show()
# 题目3（挑战）：
# 使用 plt.subplots 生成 2 行 2 列的子图
# 分别画出 y=sin(x), y=cos(x), y=sin(2x), y=cos(2x)
# 并给每个子图加上标题
fig3,axes3=plt.subplots(2,2,figsize=(10, 10))
axes3[0,0].plot(x,y1,'r--',label="function sin(x)")
axes3[0,0].set_title("fig sin(x) ")
axes3[0,0].legend(loc="lower left", fontsize=5, frameon=False)
# 左上图
axes3[0,1].plot(x,y2,'c-.',label="function cos(x)")
axes3[0,1].set_title("fig cos(x)")
axes3[0,1].legend(loc="lower left", fontsize=5, frameon=False)
# 右上图
axes3[1,0].plot(x,y3,'b-',label="function sin(2x)")
axes3[1,0].set_title("fig sin(2x) ")
axes3[1,0].legend(loc="lower left", fontsize=5, frameon=False)
# 左下图
axes3[1,1].plot(x,y4,'r:',label="function cos(2x)")
axes3[1,1].set_title("fig cos(2x) ")
axes3[1,1].legend(loc="lower left", fontsize=5, frameon=False)
plt.tight_layout()  # 自动调整子图间距
plt.show()
