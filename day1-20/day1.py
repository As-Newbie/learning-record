# # print("ceshiwenben")
# # print('文本1', '文本2',sep='🤣')
# # 新的任务
#
# # import tkinter as tk
# # from tkinter import simpledialog, messagebox
# #
# # root=tk.Tk()
# # root.withdraw()
# # name = simpledialog.askstring("赶紧输入你的名字", "能给我你的名字吗？🥵🥵🥵🥵")
# # age = simpledialog.askinteger("快点你的年龄", "你多大了😊😊")
# # messagebox.showinfo("结果", f"姓名为🤣🛬 {name} 现在已经是 {age} 的老东西了")
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# # 导入库
# root=tk.Tk()
# root.withdraw()
# # 主窗口 并隐藏
# name= simpledialog.askstring('what is your name?','please input your name:')
# # 这是个名字获取
# birth=int(simpledialog.askstring('Please tell me your date of birth?','please input date of birth:'))
# age=2025-birth
# # 获取出生日期并计算年龄
# messagebox.showinfo("结果", f"Your name is🤣 {name} 现在已经是 {age} 的老东西了")
# messagebox.showinfo("任务一已结束", f"任务一结束咯🥵")
# # 上面是任务一
# # 接着是任务二
# a=float(simpledialog.askstring('what is your first number?',f'Please {age}-year-old {name} input first number:'))
# b=float(simpledialog.askstring('what is your second number?',f'Please {age}-year-old {name} input second number:'))
# # 分别获取两个数值
# messagebox.showinfo("calculation result ", f"\n它们的和是\t{a+b}\n它们的差是\t{a-b}\n它们的积是\t{a*b}\n他们的商是\t{a/b}")
# messagebox.showinfo("任务二已结束", f"任务二结束咯👏")
# # 结果输出
# # 上面是任务二
# # 下面是任务三
# c=float(simpledialog.askstring('what is your first number?',f'Please {age}-year-old {name} input first number:'))
# d=float(simpledialog.askstring('what is your second number?',f'Please {age}-year-old {name} input second number:'))
# if c>d :
#     messagebox.showinfo("让我看看谁更大", f"你们两个还是c{c}更大一些啊😁")
#     # c大输出c
# elif  c<d:
#     messagebox.showinfo("让我看看谁更大", f"你们两个还是d{d}更大一些啊🥰")
# else :
#     messagebox.showinfo("让我看看谁更大", f"你们两个竟然是一样大啊😒")
# messagebox.showinfo("任务三已结束", f"任务三结束咯👏下班咯")
#     # 否则输出d
#     # 没了吧