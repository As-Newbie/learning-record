# #1 写一个函数 circle_area(radius)，返回圆的面积（公式 πr²）。
# #
# #2 写一个函数 greet(name="陌生人")，带有默认参数，返回“你好，xxx”。
# #
# #3 写一个函数 stats(a, b, c)，返回这三个数的最大值、最小值和平均值。
# # 作业1 写一个函数 circle_area(radius)，返回圆的面积（公式 πr²）。
# import tkinter as tk
# from math import pi
# from tkinter import simpledialog, messagebox
#
# from numpy.ma.extras import average
#
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
# def circle_area(radius):
#     return float(pi * radius * radius)
# r=simpledialog.askfloat("圆面积计算器","请输入圆的半径：")
# messagebox.showinfo("圆面积计算器",f"你输入的圆的半径是{r}，其面积为{circle_area(r)}")
# # 作业2 写一个函数 greet(name="陌生人")，带有默认参数，返回“你好，xxx”
# def greet(name="陌生人"):
#     return name
# n=simpledialog.askstring("用户名输入",f"请告诉我你的名字：")
# gender=simpledialog.askstring("用户性别输入",f"请告诉我你的性别：")
# if gender=="男":
#     g="先生"
# elif gender=="女":
#     g="女士"
# else:
#     g="先生/女士"
# messagebox.showinfo("欢迎系统",f"您好\n{greet(n)}{g}\n欢迎光临！")
# # 作业3 写一个函数 stats(a, b, c)，返回这三个数的最大值、最小值和平均值。
# a1=simpledialog.askinteger("计算器","请输入第一个数字：")
# b1=simpledialog.askinteger("计算器","请输入第二个数字：")
# c1=simpledialog.askinteger("计算器","请输入第三个数字：")
# def stats_max(a,b,c):
#     return max(a,b,c)
# _max=stats_max(a1,b1,c1)
# def stats_min(a,b,c):
#     return min(a,b,c)
# _min=stats_min(a1,b1,c1)
# def stats_ave(a,b,c):
#     return a+b+c
# _ave=stats_ave(a1,b1,c1)/3
# messagebox.showinfo("计算器",f"你输入的三个数字是{a1}、{b1}、{c1}，\n他们的\t最大值、\t最小值、\t均值\t\n分别为：\t{_max}、\t{_min}、\t{_ave}。\t")
#
#
# # 很好，你已经完整地实现了三个小练习，并且成功把 **用户输入 + 函数 + 返回值 + messagebox 输出** 结合起来了 👍。下面我帮你逐条点评和优化建议：
# #
# # ---
# #
# # ### **作业 1：circle\_area**
# #
# # ```python
# # def circle_area(radius):
# #     return float(pi * radius * radius)
# # ```
# #
# # ✅ 正确无误，计算圆面积的公式也正确。
# # 💡 优化建议：`float()` 可以去掉，因为 `pi * radius ** 2` 本身就是浮点数。也可以写成更 Pythonic 的形式：
# #
# # ```python
# # def circle_area(radius):
# #     return pi * radius ** 2
# # ```
# #
# # ---
# #
# # ### **作业 2：greet**
# #
# # ```python
# # def greet(name="陌生人"):
# #     return name
# # ```
# #
# # * 功能上可以工作，但严格来说你函数只是返回了名字，没有完成“返回‘你好，xxx’”。
# # * 改进示例：
# #
# # ```python
# # def greet(name="陌生人"):
# #     return f"你好，{name}"
# # ```
# #
# # 然后在 `messagebox.showinfo` 里直接用：
# #
# # ```python
# # messagebox.showinfo("欢迎系统", f"{greet(n)} {g}")
# # ```
# #
# # 这样函数本身就封装了问候语，更符合函数的设计理念。
# #
# # ---
# #
# # ### **作业 3：stats**
# #
# # 你写了三个函数分别计算最大值、最小值、平均值：
# #
# # ```python
# # def stats_max(a,b,c):
# #     return max(a,b,c)
# #
# # def stats_min(a,b,c):
# #     return min(a,b,c)
# #
# # def stats_ave(a,b,c):
# #     return a+b+c
# # ```
# #
# # ✅ 功能正确，结果也对。
# #
# # 💡 优化建议：可以把它们合并成一个函数，一次返回三个值，更符合“返回多个值”的练习：
# #
# # ```python
# # def stats(a, b, c):
# #     maximum = max(a, b, c)
# #     minimum = min(a, b, c)
# #     average = (a + b + c) / 3
# #     return maximum, minimum, average
# #
# # _max, _min, _ave = stats(a1, b1, c1)
# # ```
# #
# # 这样代码更简洁，调用也更方便。
# #
# # ---
# #
# # ### **整体代码小优化**
# #
# # 1. 避免重复导入模块，例如 `from numpy.ma.extras import average` 没有用到，可以去掉。
# # 2. 输出里可以多用 `\n` 或 `\t` 美化显示，但注意 `\t` 对齐效果不总是完美，尤其在 messagebox 里。
# # 3. `g` 的性别判断逻辑可以简化：
# #
# # ```python
# # g = "先生" if gender=="男" else "女士" if gender=="女" else "先生/女士"
# # ```
# #
# # ---
# #
# # ### ✅ 总结
# #
# # * 功能完成度高，用户输入、函数计算、输出都实现了。
# # * 函数的封装可以再进一步，把逻辑尽量放在函数内部，调用时只传参数，输出由函数返回值决定，这样代码更清晰、可复用。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# from math import pi
#
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
#
# # =============================
# # 作业 1：计算圆的面积
# # =============================
# def circle_area(radius):
#     """计算圆的面积"""
#     return pi * radius ** 2
#
# r = simpledialog.askfloat("圆面积计算器", "请输入圆的半径：")
# if r is not None:
#     area = circle_area(r)
#     messagebox.showinfo("圆面积计算器", f"你输入的圆的半径是 {r}\n面积为 {area:.2f}")
# else:
#     messagebox.showinfo("圆面积计算器", "你没有输入半径，跳过计算。")
#
# # =============================
# # 作业 2：带默认参数的问候函数
# # =============================
# def greet(name="陌生人"):
#     """返回问候语"""
#     return f"你好，{name}"
#
# name_input = simpledialog.askstring("用户名输入", "请告诉我你的名字：")
# gender_input = simpledialog.askstring("用户性别输入", "请告诉我你的性别：")
#
# g = "先生" if gender_input=="男" else "女士" if gender_input=="女" else "先生/女士"
# messagebox.showinfo("欢迎系统", f"{greet(name_input)} {g}\n欢迎光临！")
#
# # =============================
# # 作业 3：返回最大值、最小值、平均值
# # =============================
# def stats(a, b, c):
#     """返回三个数的最大值、最小值和平均值"""
#     maximum = max(a, b, c)
#     minimum = min(a, b, c)
#     average = (a + b + c) / 3
#     return maximum, minimum, average
#
# a1 = simpledialog.askinteger("计算器", "请输入第一个数字：")
# b1 = simpledialog.askinteger("计算器", "请输入第二个数字：")
# c1 = simpledialog.askinteger("计算器", "请输入第三个数字：")
#
# if None not in (a1, b1, c1):
#     _max, _min, _ave = stats(a1, b1, c1)
#     messagebox.showinfo("计算器", f"你输入的三个数字是：{a1}, {b1}, {c1}\n"
#                                   f"最大值: {_max}\n最小值: {_min}\n平均值: {_ave:.2f}")
# else:
#     messagebox.showinfo("计算器", "输入不完整，无法计算最大值、最小值和平均值。")
# # 明白，你希望把 **固定三个数** 改成 **用户自由输入任意数量的数字**，然后计算最大值、最小值和平均值。
# #
# # 这里有几种实现思路，我帮你整理一下：
# #
# # ---
# #
# # ### 1️⃣ 用循环让用户输入任意个数
# #
# # ```python
# # import tkinter as tk
# # from tkinter import simpledialog, messagebox
# #
# # root = tk.Tk()
# # root.withdraw()
# #
# # numbers = []
# #
# # while True:
# #     n = simpledialog.askfloat("计算器", "请输入一个数字（取消结束输入）：")
# #     if n is None:  # 用户取消输入，结束循环
# #         break
# #     numbers.append(n)
# #
# # if numbers:  # 确保列表非空
# #     maximum = max(numbers)
# #     minimum = min(numbers)
# #     average = sum(numbers) / len(numbers)
# #     messagebox.showinfo("计算结果",
# #                         f"你输入的数字有：{numbers}\n最大值: {maximum}\n最小值: {minimum}\n平均值: {average:.2f}")
# # else:
# #     messagebox.showinfo("计算结果", "你没有输入任何数字！")
# # ```
# #
# # ✅ 说明：
# #
# # * `while True` 无限循环，用户输入 `None`（点击取消）就结束输入。
# # * 所有数字存入 `numbers` 列表。
# # * 最后用 `max()`, `min()`, `sum()/len()` 计算结果。
# #
# # ---
# #
# # ### 2️⃣ 封装成函数
# #
# # 为了复用，你可以把逻辑封装成一个函数：
# #
# # ```python
# # def stats_dynamic():
# #     nums = []
# #     while True:
# #         n = simpledialog.askfloat("计算器", "请输入一个数字（取消结束输入）：")
# #         if n is None:
# #             break
# #         nums.append(n)
# #     if nums:
# #         return max(nums), min(nums), sum(nums)/len(nums)
# #     else:
# #         return None, None, None
# #
# # _max, _min, _ave = stats_dynamic()
# # if _max is not None:
# #     messagebox.showinfo("计算结果", f"最大值: {_max}\n最小值: {_min}\n平均值: {_ave:.2f}")
# # else:
# #     messagebox.showinfo("计算结果", "你没有输入任何数字！")
# # ```
# #
# # ---
# #
# # 这样，你就不再受固定数字个数的限制，用户可以自由输入任意数量的数字，然后得到最大值、最小值和平均值。
#
#
#
