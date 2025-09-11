# # 📝1.写一个函数 calc(a, b)，返回 a+b 和 a*b 两个结果。
# #
# # 📝2.写一个函数 hypotenuse(a, b)，调用 square 函数，返回直角三角形的斜边长。（勾股定理：√(a²+b²)）
# #
# # 📝3.写一个函数 counter()，每调用一次，就让一个全局变量 count 增加 1，并输出当前次数。
# #
# # 📝4.扩展练习：写一个函数，输入一个数字 n，返回 (平方, 立方, 平方根)。
# # 作业1 写一个函数 calc(a, b)，返回 a+b 和 a*b 两个结果。
# import tkinter as tk
# import math
# from tkinter import simpledialog, messagebox
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
# def calc(a, b):
#     return a+b,a*b
# x=simpledialog.askfloat("calc","请输入第一个数字：")
# y=simpledialog.askfloat("calc","请输入第二个数字：")
# s,v=calc(x,y)
# messagebox.showinfo("calc",f"数字{x}和{y}的和与积分别为{calc(x,y)}")
# # 作业2 写一个函数 hypotenuse(a, b)，调用 square 函数，返回直角三角形的斜边长。（勾股定理：√(a²+b²)）
# def square(x):
#     return x*x
# def hypotenuse(a, b):
#     return math.sqrt(square(a)+square(b))
# n=simpledialog.askfloat("勾股","请输入第一个边长：")
# m=simpledialog.askfloat("勾股","请输入第二个边长：")
# messagebox.showinfo("勾股",f"直角边长为{n}和{m}的三角形的斜边长为{hypotenuse(n, m)}")
# # 作业3.写一个函数 counter()，每调用一次，就让一个全局变量 count 增加 1，并输出当前次数。
# count=0
# def counter():
#     global count
#     count+=1
# print(count)
# # 4.扩展练习：写一个函数，输入一个数字 n，返回 (平方, 立方, 平方根)。
# def sp(n):
#     return n*n,n**3,math.sqrt(n)
# z=simpledialog.askfloat("sp","请输入数字：")
# messagebox.showinfo("sp",f"数字{z}的平方、立方、平方根为{sp(z)}")
#
#
#
# # 👍 很棒！你把 Day7 的四个作业都写出来了，而且逻辑基本正确。下面我帮你点评一下，并指出可以优化的地方：
# #
# # ---
# #
# # ### ✅ 作业 1
# #
# # ```python
# # def calc(a, b):
# #     return a+b, a*b
# # ```
# #
# # * ✅ 返回和与积写得很好。
# # * 小优化：你在 `messagebox.showinfo` 里用了 `calc(x,y)`，其实你已经在前面算过 `s, v = calc(x, y)`，可以直接用 `s` 和 `v`，避免重复计算：
# #
# # ```python
# # messagebox.showinfo("calc", f"数字{x}和{y}的和是{s}，积是{v}")
# # ```
# #
# # ---
# #
# # ### ✅ 作业 2
# #
# # ```python
# # def square(x):
# #     return x*x
# # def hypotenuse(a, b):
# #     return math.sqrt(square(a)+square(b))
# # ```
# #
# # * ✅ 先写了 `square` 再在 `hypotenuse` 中调用，非常符合题意。
# # * 输入和输出部分也做得正确。
# #
# # ---
# #
# # ### ⚠ 作业 3
# #
# # ```python
# # count = 0
# # def counter():
# #     global count
# #     count += 1
# # print(count)
# # ```
# #
# # * 这里的问题是：你定义了 `counter()` 函数，但其实没有调用它，所以最后 `print(count)` 只是输出了初始值 `0`。
# # * 正确的做法是调用函数，例如：
# #
# # ```python
# # counter()
# # counter()
# # counter()
# # print(count)   # 结果应该是 3
# # ```
# #
# # 如果想让它每次调用都能提示用户，可以写成：
# #
# # ```python
# # def counter():
# #     global count
# #     count += 1
# #     messagebox.showinfo("counter", f"这是第 {count} 次调用")
# # ```
# #
# # ---
# #
# # ### ✅ 作业 4
# #
# # ```python
# # def sp(n):
# #     return n*n, n**3, math.sqrt(n)
# # ```
# #
# # * ✅ 完全正确。平方、立方、平方根都能正确返回。
# # * 小优化：结果用元组 `(平方, 立方, 平方根)` 返回时，可以在 `messagebox` 中拆开来显示，更直观：
# #
# # ```python
# # sq, cube, root = sp(z)
# # messagebox.showinfo("sp", f"数字 {z}\n平方：{sq}\n立方：{cube}\n平方根：{root}")
# # ```
# #
# # ---
# #
# # ### 🌟 总体评价
# #
# # * 你已经能熟练写函数、调用函数，并结合 `tkinter` 与用户交互，进步很快。
# # * 唯一需要注意的是 **函数要真正调用起来**，否则就只是定义了没用。
# #
# # ---
# #
# # 要不要我帮你把 **作业3 counter()** 改成一个完整的交互式版本（点一次按钮就+1 并弹窗显示次数）？这样更直观。
#
#
#
# # 好，那我帮你把 **counter()** 写成一个完整可运行的小程序。这样你每点一次按钮，调用一次函数，计数就会加一，并在窗口里提示：
# #
# # ```python
# # import tkinter as tk
# # from tkinter import messagebox
# #
# # # 全局计数器
# # count = 0
# #
# # def counter():
# #     global count
# #     count += 1
# #     messagebox.showinfo("计数器", f"这是第 {count} 次调用")
# #
# # # 初始化主窗口
# # root = tk.Tk()
# # root.title("计数器示例")
# #
# # # 创建按钮，每点一次就调用 counter()
# # btn = tk.Button(root, text="点我计数", command=counter, width=20, height=2)
# # btn.pack(pady=20)
# #
# # # 启动事件循环
# # root.mainloop()
# # ```
# #
# # ### 📌 说明：
# #
# # 1. 定义了一个全局变量 `count`，初始为 0。
# # 2. 每次点击按钮，都会调用 `counter()`，`count` 增加 1。
# # 3. `messagebox.showinfo` 会弹窗显示当前次数。
# # 4. `tk.Button` 绑定了 `command=counter`，这就是把函数和按钮关联起来的关键。
# #
# # 这样运行后，你就能清楚地看到函数调用和全局变量变化的效果啦。
# #
# # 要不要我再给你演示一个 **不用按钮、直接循环调用 counter() 并打印结果** 的版本？
