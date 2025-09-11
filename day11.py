# # 1.让用户输入一句话，去掉首尾空格，并把其中的 "Python" 替换成 "Java" 后输出。
# #
# # 2.定义一个列表 [5, 8, 2, 7]，尝试用 append、insert、remove、pop 等操作，最后输出处理结果。
# #
# # 3.让用户输入 5 个单词，存入列表，然后：
# # 输出第一个和最后一个单词
# # 判断 "hello" 是否在其中
# # 如果有 "hello"，打印它的索引
# # 4.扩展：写一个函数，接收一个列表，返回所有偶数的平方（用列表推导式）。
# # 作业1 让用户输入一句话，去掉首尾空格，并把其中的 "Python" 替换成 "Java" 后输出。
# import tkinter as tk
# from dataclasses import replace
# from tkinter import simpledialog, messagebox
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
# text=simpledialog.askstring("捣蛋鬼","请输入一句含有Python的语句 嘿嘿~")
# text_new=text.replace("Python","Java")
# messagebox.showinfo("捣蛋鬼",f"哈哈，Java天下第一！{text_new.strip()}")
# messagebox.showinfo("作业1",f"作业1完成")
# # 作业2 定义一个列表 [5, 8, 2, 7]，尝试用 append、insert、remove、pop 等操作，最后输出处理结果。
# list_r=[5, 8, 2, 7]
# list_r.append(15)
# messagebox.showinfo("作业2",f"作业2当前列表为{list_r}")
# list_r.insert(1,100)
# messagebox.showinfo("作业2",f"作业2当前列表为{list_r}")
# list_r.remove(5)
# messagebox.showinfo("作业2",f"作业2当前列表为{list_r}")
# list_r.pop(1)
# messagebox.showinfo("作业2",f"作业2当前列表为{list_r}")
# messagebox.showinfo("作业2",f"作业2完成")
# # 作业3 让用户输入 5 个单词，存入列表，然后：
# # # 输出第一个和最后一个单词
# # # 判断 "hello" 是否在其中
# # 如果有 "hello"，打印它的索引
# a=1
# list3=[]
# while a<=5:
#     list3.append(simpledialog.askstring("作业3", f"请输入第[{a}]个单词：(当前单词有{list3})"))
#     a+=1
# messagebox.showinfo("作业3",f"当前单词有{list3}")
# messagebox.showinfo("作业3",f"第一个单词为{list3[0]},最后一个单词为{list3[-1]}")
#
# if "hello" in list3:
#     messagebox.showinfo("作业3", f'单词hello在列表中,其索引为{list3.index("hello")}')
# #     如果用户输入 "Hello"（首字母大写），就不会被识别为 "hello"，可以考虑统一转小写：
# #
# # if "hello" in [w.lower() for w in list3]:
# #     ...
# else:
#     messagebox.showinfo("作业3", f"单词hello不在列表中")
# messagebox.showinfo("作业3",f"作业3完成")
# #作业4.扩展：写一个函数，接收一个列表，返回所有偶数的平方（用列表推导式）。
# c=simpledialog.askinteger("作业4", f"请输入你想输入几个数字")
# b=1
# list4=[]
# while b<=c:
#     list4.append(simpledialog.askinteger("作业4", f"请输入第[{b}]个数字：(当前数字有{list4})"))
#     b+=1
# squares = [x**2 for x in list4 if x % 2 == 0]
# messagebox.showinfo("作业4",f"您输入的数字{list4}中，所有偶数的平方为{squares}")
# # 作业3修改 让用户输入 5 个单词，把它们存到一个列表中，然后：
# # 输出第一个和最后一个单词
# # 判断 "hello" 是否在其中（忽略大小写）
# # 如果有 "hello"，打印它的索引
#
# a=1
# list3=[]
# while a<=5:
#     word = simpledialog.askstring("作业3", f"请输入第[{a}]个单词：(当前单词有{list3})")
#     list3.append(word)
#     a+=1
#
# messagebox.showinfo("作业3", f"当前单词有{list3}")
# messagebox.showinfo("作业3", f"第一个单词为{list3[0]}, 最后一个单词为{list3[-1]}")
#
# # 统一转小写进行判断
# lower_list = [w.lower() for w in list3]
#
# if "hello" in lower_list:
#     index = lower_list.index("hello")  # 找到小写版的索引
#     messagebox.showinfo("作业3", f'单词 "hello" 在列表中, 其索引为 {index}')
# else:
#     messagebox.showinfo("作业3", f'单词 "hello" 不在列表中')
