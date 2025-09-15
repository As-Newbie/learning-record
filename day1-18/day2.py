# #列表
# L = [10, 20, 30, 40, 50]
# L[1] = 99           # 改
# L.append(60)        # 增
# print(f'{L}\n ')
# x = L.pop()         # 删（尾）
# sub = L[1:4]        # 切片 -> [99, 30, 40]
# rev = L[::-1]       # 反转视图（新列表）
# print(f'{L}\n {x}\n{sub}\n{rev}')
# # 列表推进式
# squares = [i*i for i in range(10) if i % 2 == 0]
# print(f'squares的结果是{squares}\n ')
# M = [[0 for _ in range(3)] for _ in range(3)]
# print(f'M的结果是{M}\n ')
# # 元组
# # 集合
# unique = {ch for ch in "hello world" if ch.isalpha()}
# print(f'unique的结果是{unique}\n ')
# # 作业📚
# # 📝 小练习
# #
# # 1.创建一个列表，存放 5 个你喜欢的食物名字，打印第 2 个和最后一个。
# #
# # 2.用元组存储你电脑屏幕的分辨率（宽，高），并打印出来。
# #
# # 3.创建一个字典，存储一个人的姓名、年龄、城市，并打印出一句完整的话。
# #
# # 4.创建两个集合：{1,2,3,4} 和 {3,4,5,6}，打印它们的交集、并集和差集。
# # 首先是作业1📖
# fruits=['apple','banana','orange','pear','watermelon']
# # 写死的水果列表
# print(f'The second fruit is {fruits[1]}\nThe last fruit is {fruits[-1]}')
# # 打印第 2 个和最后一个
# # 欸 🤔我有个好主意 用窗口get food🤩
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# # 导入库
# root=tk.Tk()
# root.withdraw()
# # 主窗口 并隐藏
# food = simpledialog.askstring('What is your favorite food?','please input your favorite food:')
# # 似乎只能get一个元素 不知道怎么get列表 那我循环试试
# food=[]
# for x in range(5):
#  #    先五个水果吧 感觉数字5也能让用户填写 弹窗get然后传进去就行
#  food.append(simpledialog.askstring('What is your favorite food?','please input your favorite food:'))
#  x=x+1
# else:
#     messagebox.showinfo("You've already entered five. Don't be too greedy", f"You are such a little glutton🐈")
# # 循环结束
# messagebox.showinfo("Ah ha ha chicken soup", f"The second food is {food[1]}\nThe last food is {food[-1]}")
# messagebox.showinfo("Homework 1 is completed.", "Congratulations on completing your homework 1📖")
# # 下面是作业2🔖
# # 2.用元组存储你电脑屏幕的分辨率（宽，高），并打印出来。
# resolution_ratio=(2520,1580)
# print(f"The resolution of your computer is {resolution_ratio}")
# # 试试用字典
# resolution_ratio_dic={"length":2520, "width":1580}
# print(f"The resolution of your computer is {resolution_ratio_dic['length']}*{resolution_ratio_dic['width']}")
# # 感觉可以用同样的方式让用户输入
# messagebox.showinfo("Homework 2 is completed.", "Congratulations on completing your homework 2🔖")
# # 下面是作业3📚
# # 3.创建一个字典，存储一个人的姓名、年龄、城市，并打印出一句完整的话
# generic_dic= {"name": simpledialog.askstring("What is your name?", "please input your name:"),
#               "age": simpledialog.askstring("How old are you this year?", "please input your age:"),
#               "city": simpledialog.askstring("Where do you live?", "please input your city:")}
# # 创建一个字典 key分别是姓名、年龄、城市value都用默认值然后从弹窗中获取
# # 三个弹窗获取信息
# messagebox.showinfo("I'm a hacker. I've already got your small box😁", f"Your name is {generic_dic['name']}\nYour age is {generic_dic['age']}\nYou are currently living at {generic_dic['city']}\nALL RIGHT? NOTICE YOUR ACTION!!!")
# messagebox.showinfo("Homework 3 is completed.", "Congratulations on completing your homework 3📚")
# # 作业4 📙创建两个集合：{1,2,3,4} 和 {3,4,5,6}，打印它们的交集、并集和差集。
# S = {1, 2, 3, 4}
# T = {3, 4, 5, 6}
# messagebox.showinfo("I'm a fortune-teller！", f"Their intersection is {S&T}\nTheir union is{S|T}\nTheir difference set is{S-T}\nTheir symmetric set is{S^T}\n")
# messagebox.showinfo("Homework 4 is completed.", "Congratulations on completing your homework 4📙")
# # 以下是点评
# # 太棒了 🎉！你自己把 Day 2 的四个小练习都写出来了，还主动用了 tkinter 的输入输出，比我原本预想的练习更有创造力 👍。我来帮你逐步点评一下：
# #
# # 📝 作业 1：列表
# #
# # 你先写了一个固定的列表，然后又改成用弹窗输入并存入 list，这是很好的思路。
# #
# # 循环里 x=x+1 是多余的，因为 for x in range(5) 已经自动迭代，不需要手动加。
# #
# # 你最后能正确输出 第二个 和 最后一个，完全正确 ✅。
# #
# # 📝 作业 2：元组
# #
# # 你写了一个元组 (2520,1580)，这很好。
# #
# # 又尝试用字典来存储分辨率（长宽），这是扩展思维，非常不错 👍。
# #
# # 甚至考虑让用户输入分辨率，这说明你已经会把“死数据”改成“交互式数据”了。
# #
# # 📝 作业 3：字典
# #
# # 用默认值创建字典，再用 askstring 替换，这个思路非常规范。
# #
# # 然后你打印成一句话：
# #
# # Your name is xxx
# # Your age is xxx
# # You are currently living at xxx
# #
# #
# # ✅ 完全符合要求，还带了点“黑客风格”，哈哈 😄。
# #
# # 📝 作业 4：集合
# #
# # &（交集）、|（并集）、-（差集）、^（对称差集）都展示出来了，比题目要求还多做了一点，优秀！
# #
# # 这部分的写法非常简洁，不需要修改。
# #
# # 🌟 总评
# #
# # 作业完成度：100%
# #
# # 扩展性：很高 —— 你已经不满足于“打印答案”，而是让用户输入，这就是“学会了知识 + 举一反三”。
# #
# # 小改进点：
# #
# # 作业 1 的循环里 x=x+1 可以删掉。
# #
# # 作业 2 里如果用 simpledialog.askinteger 获取数字，用户体验会更好（不用输入字符串再转数字）。
# #
# # 作业 3 的年龄最好也转成数字，避免和字符串混淆。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# # 导入库
# root = tk.Tk()
# root.withdraw()
# # 主窗口 并隐藏
#
# # 作业1 📖
# food = []
# for x in range(5):
#     food.append(simpledialog.askstring('What is your favorite food?', 'please input your favorite food:'))
# else:
#     messagebox.showinfo("You've already entered five. Don't be too greedy",
#                         f"You are such a little glutton🐈")
#
# messagebox.showinfo("Ah ha ha chicken soup",
#                     f"The second food is {food[1]}\nThe last food is {food[-1]}")
# messagebox.showinfo("Homework 1 is completed.", "Congratulations on completing your homework 1📖")
#
# # 作业2 🔖
# # 用 askinteger 获取分辨率
# width = simpledialog.askinteger("Screen width", "Please input your screen width:")
# height = simpledialog.askinteger("Screen height", "Please input your screen height:")
#
# resolution_ratio = (width, height)
# messagebox.showinfo("Screen resolution", f"The resolution of your computer is {resolution_ratio}")
# messagebox.showinfo("Homework 2 is completed.", "Congratulations on completing your homework 2🔖")
#
# # 作业3 📚
# # 用 askinteger 获取年龄
# generic_dic = {"name": simpledialog.askstring("What is your name?", "please input your name:"),
#                "age": simpledialog.askinteger("How old are you this year?", "please input your age:"),
#                "city": simpledialog.askstring("Where do you live?", "please input your city:")}
# messagebox.showinfo("I'm a hacker. I've already got your small box😁",
#                     f"Your name is {generic_dic['name']}\n"
#                     f"Your age is {generic_dic['age']}\n"
#                     f"You are currently living at {generic_dic['city']}\nALL RIGHT? NOTICE YOUR ACTION!!!")
# messagebox.showinfo("Homework 3 is completed.", "Congratulations on completing your homework 3📚")
#
# # 作业4 📙
# S = {1, 2, 3, 4}
# T = {3, 4, 5, 6}
# messagebox.showinfo("I'm a fortune-teller！",
#                     f"Their intersection is {S & T}\n"
#                     f"Their union is {S | T}\n"
#                     f"Their difference set is {S - T}\n"
#                     f"Their symmetric set is {S ^ T}\n")
# messagebox.showinfo("Homework 4 is completed.", "Congratulations on completing your homework 4📙")
# # 恰个鸡腿🍗