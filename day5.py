# # 1.定义一个函数 add(a, b=10)，如果调用时不给第二个参数，就默认加 10。
# #
# # 2.写一个函数 calc(*args)，能计算所有参数的和。
# #
# # 3.写一个函数 person_info(**kwargs)，能接收任意个人信息（如姓名、年龄、城市），并逐条打印出来。
# #
# # 4.定义一个函数，返回两个数的和与积（两个值）。
# # 作业1
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
#
# def add(a, b=10):
#     if y is None:
#         result = add(x)  # 不输入就用默认值10
#     else:
#         result = add(x, y)
# x=simpledialog.askinteger("无名", "请输入你要计算的第一个值：")
# y=simpledialog.askinteger("无名", "请输入你要计算的第二个值：")
# # 这里不知道怎么写空值输入的情况
#
# print(f"两个数字的和是{add(x,y)}")
# # 作业2 写一个函数 calc(*args)，能计算所有参数的和。
# def calc(*args):
#    return float(sum(args))
# sum_=calc(1,2,32,87)
# print(sum_)
# # 作业3 写一个函数 person_info(**kwargs)，能接收任意个人信息（如姓名、年龄、城市），并逐条打印出来。
# def person_info(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# person_info(name="Li", age=20, city="Beijing")
# # 作业4.定义一个函数，返回两个数的和与积（两个值）。
# def sum_prod(a, b):
#     return a + b, a * b
#
# s, p = sum_prod(2, 3)
# print(s,p)
# # 今天先到这里
#
# # 作业1 修改
# # import tkinter as tk
# # from tkinter import simpledialog, messagebox
# #
# # # 初始化主窗口
# # root = tk.Tk()
# # root.withdraw()
# #
# # def add(a, b=10):
# #     return a + b
# #
# # # 获取第一个数（必填）
# # x = simpledialog.askinteger("无名", "请输入你要计算的第一个值：")
# #
# # # 获取第二个数（可选）
# # y = simpledialog.askinteger("无名", "请输入你要计算的第二个值（可留空，默认加10）：")
# #
# # # 如果用户取消或不输入第二个数，就用默认值
# # if y is None:
# #     result = add(x)
# # else:
# #     result = add(x, y)
# #
# # messagebox.showinfo("计算结果", f"两个数字的和是 {result}")
