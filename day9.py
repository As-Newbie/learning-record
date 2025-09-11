# # 1.定义一个列表 nums = [2, 4, 6, 8, 10]，用 for 循环打印出它的每个元素。
# #
# # 2.定义一个列表 scores = [88, 92, 79, 93, 85]，输出它的总分、最高分、最低分和平均分。
# #
# # 3.让用户循环输入 5 个名字，把它们存到一个列表中，然后逐个打印出来。
# #
# # 4.扩展练习：写一个函数，接收一个列表，返回其中每个数的平方，要求用 列表推导式 实现。
# # 作业1 定义一个列表 nums = [2, 4, 6, 8, 10]，用 for 循环打印出它的每个元素。
# # 这个看起来很简单
# nums = [2, 4, 6, 8, 10]
# for nums_ in nums:
#     print(nums_)
#     # 这是直接遍历元素
# for i in range(len(nums)):
#     print(f"索引为{i}对应的值为{nums[i]}")
#     # 这是索引的方法 for循环列表的长度（元素个数）逐个打印对应的元素
# for a, value in enumerate(nums):
#     print(f"第{a+1}个值为 {value}")
# print("========================= 分隔符1 =========================")
# # 这是使用enumerate的方法 但我不很懂 详细讲讲
# # 作业2 定义一个列表 scores = [88, 92, 79, 93, 85]，输出它的总分、最高分、最低分和平均分。
# scores = [88, 92, 79, 93, 85]
# print(f"最高分为{max(scores)}")
# print(f"最低分为{min(scores)}")
# print(f"总分为{sum(scores)}")
# print(f"平均分为{sum(scores)/len(scores)}")
# print(f"分数从低到高为{sorted(scores)}")
# new_nums=scores
# # new_nums = scores 并不是拷贝，而是两个变量指向同一个列表。所以当你 reverse() 时，scores 本身也被修改了。
# # new_nums = scores[:]   # 或 new_nums = scores.copy()
# # new_nums.reverse()
# # print(f"分数从高到低为{new_nums}")
#
# new_nums.reverse()
# print(f"分数从高到低为{new_nums}")
# print(f"分数从高到低为{sorted(scores, reverse=True)}")
# print("========================= 分隔符2 =========================")
# # 作业3 让用户循环输入 5 个名字，把它们存到一个列表中，然后逐个打印出来。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
# end=int(simpledialog.askinteger("逐个打印",f"你想输出多少个名字?"))
# end_re=end
# name=[]
# for n in range(end_re):
#     name_input=simpledialog.askstring('逐个打印','Brother, enter the name you like！')
#     name.append(name_input)
#     if name_input=="quit":
#         break
# print(f"你输入的名字个数为{len(name)}，名字分别为{name}")
# print("========================= 分隔符3 =========================")
# # 作业4 扩展练习：写一个函数，接收一个列表，返回其中每个数的平方，要求用 列表推导式 实现。
# cala=[]
# end1=int(simpledialog.askstring("计算",f"你想计算多少个数字?"))
# end1_re=end1
# for y in range(end1_re):
#     cala_input=simpledialog.askfloat('计算','Brother, enter the number you like！(enter 0 to end)')
#     cala.append(cala_input)
#     if cala_input==0:
#         break
# def square_(lst):
#     return [m**2 for m in lst]
# square_result=square_(cala)
# print(square_result)
# messagebox.showinfo("计算",f"数字的平方分别为{square_result}")
