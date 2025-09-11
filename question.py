# nums = []
# while True:
#     val = input("请输入一个数字（输入 q 退出）：")
#     if val == "q":
#         break
#     nums.append(int(val))
#
# print("你输入的数字有：", nums)
#
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# # 初始化
# root = tk.Tk()
# root.withdraw()
#
# # 定义函数
# def add(a, b=10):
#     return a + b
#
# # 获取第一个数字
# a = simpledialog.askinteger("加法计算器", "请输入第一个数字：")
# if a is None:
#     messagebox.showinfo("结果", "你没有输入任何数字，程序结束。")
# else:
#     # 获取第二个数字（可选）
#     b = simpledialog.askinteger("加法计算器", "请输入第二个数字（可选，取消则默认10）：")
#
#     if b is None:  # 用户取消或空输入
#         result = add(a)       # 使用默认值 b=10
#         messagebox.showinfo("结果", f"你只输入了一个数字 {a}\n结果是：{result}")
#     else:
#         result = add(a, b)    # 使用输入的 b
#         messagebox.showinfo("结果", f"你输入了 {a} 和 {b}\n结果是：{result}")
#
#
#
#
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# root = tk.Tk()
# root.withdraw()
#
# def add_all(a_list, b=10):
#     return sum(a_list) + b
#
# a_list = []  # 用来存放多个 a 的值
#
# while True:
#     a = simpledialog.askinteger("加法计算器", "请输入一个 a（取消表示结束输入）：")
#     if a is None:  # 结束输入
#         break
#     a_list.append(a)
#
# b = simpledialog.askinteger("加法计算器", "请输入 b（取消则默认 10）：")
# if b is None:
#     result = add_all(a_list)
# else:
#     result = add_all(a_list, b)
#
# messagebox.showinfo("结果", f"你输入的 a 值有：{a_list}\n b = {b if b is not None else 10}\n最终结果是：{result}")
