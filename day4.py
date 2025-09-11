# #作业1📖定义一个函数 square(n)，返回数字的平方，并调用它。
# #
# #作业2📚定义一个函数 max_of_two(a, b)，返回两个数中较大的一个。
# #
# #作业3📙定义一个函数 is_even(n)，判断一个数是否为偶数，返回 True/False。
# #
# #作业4🎒写一个函数 bmi(height, weight)，计算并返回 BMI 指数 = 体重 / (身高²)，然后根据数值判断体型（过轻、正常、超重、肥胖）。
# #作业1📖定义一个函数 square(n)，返回数字的平方，并调用它。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# # 导入库
# root=tk.Tk()
# root.withdraw()
# # 隐藏主窗口
# def square(n):
#     # 定义函数square计算平方
#     return n*n
# # 返回计算的平方值
# nn=simpledialog.askinteger("Square calculation is a piece of cake!", "Please enter the number whose square you want to calculate n：")
# # 获取需要计算的变量的值
# messagebox.showinfo("Square calculation is a piece of cake!", f"The square of the number you entered  ({nn}) is {square(nn)}")
# # 调用square函数计算并输出结果
# # 作业1📖结束
# # 作业2📚定义一个函数 max_of_two(a, b)，返回两个数中较大的一个。
# def max_of_two(a, b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else :
#         return f"The number ({a}) you entered is as large as the number ({b})"
# x=simpledialog.askinteger("Let's compare the sizes together!", "Please enter the first number whose square you want to calculate ：")
# y=simpledialog.askinteger("Let's compare the sizes together!", "Please enter the second number whose square you want to calculate ：")
# messagebox.showinfo("Let's compare the sizes together!", f"The larger number among the numbers you entered ({x} {y})is\n{max_of_two(x,y)}")
# #作业3📙定义一个函数 is_even(n)，判断一个数是否为偶数，返回 True/False。
# def  is_even(m):
#     if m%2==0:
#      return True
#     else:
#      return False
# #作业4🎒写一个函数 bmi(height, weight)，计算并返回 BMI 指数 = 体重 / (身高²)，然后根据数值判断体型（过轻、正常、超重、肥胖）。
# def bmi(height, weight):
#     ww=height*height
#     bmi_=float(ww/weight)
#     return bmi_
# e=simpledialog.askfloat("BMI计算器!", "请输入你的身高（m）：")
# f=simpledialog.askfloat("BMI计算器!", "请输入你的体重(kg)：")
# if bmi(e, f)>=30.0:
#     messagebox.showinfo("BMI计算器!",f"你的BMI值为{bmi(e, f):.2f}\n你的体型为 肥胖！\n你需要减肥！行动起来！🏊‍♀️")
# elif bmi(e, f)>=25.0:
#     messagebox.showinfo("BMI计算器!", f"你的BMI值为{bmi(e, f):.2f}\n你的体型为 超重！\n你需要适当锻炼！🏃")
# elif bmi(e, f)>=18.5:
#     messagebox.showinfo("BMI计算器!",  f"你的BMI值为{bmi(e, f):.2f}\n你的体型为 正常！\n你很健康！继续保持！💪")
# else:
#     messagebox.showinfo("BMI计算器!",  f"你的BMI值为{bmi(e, f):.2f}\n你的体型为 偏瘦！\n有些瘦了，多吃点好的🍗！")
# # 作业4🎒完成
#
#
#
# # 非常好👏 你已经把 Day4 的四个练习都实现了，而且还结合了 `tkinter` 的输入弹窗，交互体验更强。整体思路完全正确，不过我帮你指出几个可以优化的小地方：
# #
# # ---
# #
# # ### 🔍 代码细节建议
# #
# # 1. **作业2**
# #
# #    * 你的 `max_of_two(a, b)` 写得没问题，但可以用 Python 的内置函数 `max(a, b)` 简化。
# #    * 另外，在 `messagebox.showinfo` 中输出时，格式稍微改下更美观。
# #
# # 2. **作业3**
# #
# #    * 你写的 `is_even(m)` 逻辑正确，其实可以更简洁：
# #
# #      ```python
# #      def is_even(m):
# #          return m % 2 == 0
# #      ```
# #
# # 3. **作业4（BMI计算）**
# #
# #    * 你的公式写反了，应该是 **体重 ÷ (身高²)**，你写成了 `height / (weight²)`。
# #    * 改正后应该是：
# #
# #      ```python
# #      def bmi(height, weight):
# #          return weight / (height * height)
# #      ```
# #    * 另外，最好把 BMI 值格式化一下，避免弹窗里出现太多小数位：
# #
# #      ```python
# #      f"{bmi(e, f):.2f}"
# #      ```
# #
# # ---
# #
# # ### ✅ 优化后 BMI 部分示例
# #
# # ```python
# # def bmi(height, weight):
# #     return weight / (height * height)
# #
# # e = simpledialog.askfloat("BMI计算器!", "请输入你的身高（m）：")
# # f = simpledialog.askfloat("BMI计算器!", "请输入你的体重(kg)：")
# #
# # bmi_value = bmi(e, f)
# #
# # if bmi_value >= 30.0:
# #     body_type = "肥胖！你需要减肥！行动起来！🏊‍♀️"
# # elif bmi_value >= 25.0:
# #     body_type = "超重！你需要适当锻炼！🏃"
# # elif bmi_value >= 18.5:
# #     body_type = "正常！你很健康！继续保持！💪"
# # else:
# #     body_type = "偏瘦！有些瘦了，多吃点好的🍗！"
# #
# # messagebox.showinfo("BMI计算器!", f"你的BMI值为 {bmi_value:.2f}\n你的体型为 {body_type}")
# # ```
# #
# # ---
# #
# # 你要不要我帮你把四个作业全部整理成一个 **更精简、更规范的版本**（但保留你喜欢的弹窗交互风格）？
# # 好的 👍，我帮你把 Day4 的四个作业整理成一个整洁、规范、交互友好的版本，保留弹窗交互，同时优化一些小细节。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
#
# # ---------- 作业1：平方函数 ----------
# def square(n):
#     """返回数字的平方"""
#     return n * n
#
# num = simpledialog.askinteger("平方计算器", "请输入一个数字计算平方：")
# messagebox.showinfo("平方计算器", f"你输入的数字 {num} 的平方是 {square(num)}")
#
# # ---------- 作业2：比较两个数 ----------
# def max_of_two(a, b):
#     """返回两个数字中较大的一个"""
#     return max(a, b)
#
# x = simpledialog.askinteger("比较大小", "请输入第一个数字：")
# y = simpledialog.askinteger("比较大小", "请输入第二个数字：")
# messagebox.showinfo("比较大小", f"你输入的数字分别是 {x} 和 {y}。\n较大的数字是 {max_of_two(x, y)}")
#
# # ---------- 作业3：判断偶数 ----------
# def is_even(n):
#     """判断是否为偶数"""
#     return n % 2 == 0
#
# m = simpledialog.askinteger("偶数判断", "请输入一个数字判断是否为偶数：")
# result = "是偶数" if is_even(m) else "是奇数"
# messagebox.showinfo("偶数判断", f"你输入的数字 {m} {result}")
#
# # ---------- 作业4：BMI计算 ----------
# def bmi(height, weight):
#     """根据身高（米）和体重（kg）计算BMI"""
#     return weight / (height * height)
#
# def bmi_category(bmi_value):
#     """根据中国标准返回体型"""
#     if bmi_value < 18.5:
#         return "偏瘦！有些瘦了，多吃点好的🍗！"
#     elif bmi_value < 24:
#         return "正常！你很健康！继续保持！💪"
#     elif bmi_value < 28:
#         return "超重！你需要适当锻炼！🏃"
#     else:
#         return "肥胖！你需要减肥！行动起来！🏊‍♀️"
#
# height = simpledialog.askfloat("BMI计算器", "请输入你的身高（米）：")
# weight = simpledialog.askfloat("BMI计算器", "请输入你的体重（公斤）：")
# bmi_value = bmi(height, weight)
# category = bmi_category(bmi_value)
#
# messagebox.showinfo("BMI计算器", f"你的BMI值为 {bmi_value:.2f}\n你的体型为 {category}")
#
#
