# # 1.定义一个列表 nums = [3, 7, 1, 9, 5]，输出最大值、最小值和平均值。
# #
# # 2.定义一个列表 friends = ["小明", "小红", "小刚"]，在最后加上 "小丽"，然后删除 "小红"。
# #
# # 3.写一个程序，循环让用户输入水果名，把它们加到列表里，直到输入 "结束" 为止，最后打印整个列表。
# #
# # 4.扩展练习：写一个函数，接收一个列表，返回去掉最大值和最小值之后的平均数。
# # 作业1.定义一个列表 nums = [3, 7, 1, 9, 5]，输出最大值、最小值和平均值。
# from operator import truediv
#
# from numpy.ma.extras import average
#
# nums=[3,7,1,9,5]
# print(max(nums))
# print(min(nums))
# print(average(nums))
# # 作业2.定义一个列表 friends = ["小明", "小红", "小刚"]，在最后加上 "小丽"，然后删除 "小红"。
# friends = ["小明", "小红", "小刚"]
# friends.append("小丽")
# # 末尾添加
# print("末尾添加小丽",friends)
# friends.remove("小红")
# print("删除小红",friends)
# # 作业3 写一个程序，循环让用户输入水果名，把它们加到列表里，直到输入 "结束" 为止，最后打印整个列表。
# fruits=[]
# def add_(item):
#     global fruits
#     fruits.append(item)
#     return  fruits
# while True:
#     user_input=input("请输入水果名称(输入quit结束)：")
#     if user_input=="quit":
#         break
#     else:
#         add_(user_input)
# print("已结束，当前列表为：", fruits)
# # 作业4 扩展练习：写一个函数，接收一个列表，返回去掉最大值和最小值之后的平均数。
# lis=[1,3,5,7,9,11]
# def ca(nn):
#     global lis
#     lis.append(nn)
#     return lis
# while True:
#     nnn = int(input("请输入数字(输入0结束)："))
#     if nnn == 0:
#         break
#     else:
#         ca(nnn)
# lis.remove(max(lis))
# print("已删除最大值，当前列表为：", lis)
# lis.remove(min(lis))
# print("已删除最小值，当前列表为：", lis)
# print("列表的平均值为",average(lis))
#
#
#
# # 非常棒👏！你已经把 Day8 的核心练习都写下来了。整体逻辑是对的，但我来帮你指出几点小优化和改进的地方，保证你的代码更简洁、规范：
# #
# # ---
# #
# # ### ✅ 作业 1
# #
# # ```python
# # nums = [3, 7, 1, 9, 5]
# # print(max(nums))
# # print(min(nums))
# # print(sum(nums)/len(nums))   # 不建议用 numpy，这里直接用内置函数更简洁
# # ```
# #
# # 💡 解释：
# #
# # * 这里用 `sum(nums)/len(nums)` 直接计算平均值即可，没必要导入 `numpy`。
# # * Python 内置函数已经很强大了。
# #
# # ---
# #
# # ### ✅ 作业 2
# #
# # ```python
# # friends = ["小明", "小红", "小刚"]
# # friends.append("小丽")
# # print("末尾添加小丽:", friends)
# #
# # friends.remove("小红")
# # print("删除小红:", friends)
# # ```
# #
# # 💡 解释：
# #
# # * 这部分写得很清楚了，没问题。
# #
# # ---
# #
# # ### ✅ 作业 3
# #
# # ```python
# # fruits = []
# #
# # while True:
# #     user_input = input("请输入水果名称(输入 '结束' 结束)：")
# #     if user_input == "结束":
# #         break
# #     fruits.append(user_input)
# #
# # print("已结束，当前列表为：", fruits)
# # ```
# #
# # 💡 改进：
# #
# # * 不需要 `global`，直接在循环里 `append` 就够了。
# # * 你的原版写了 `add_()` 函数，其实没必要增加复杂度。
# # * 建议把结束标志统一为 **题目里要求的“结束”**，保持一致。
# #
# # ---
# #
# # ### ✅ 作业 4
# #
# # ```python
# # def middle_average(lst):
# #     if len(lst) <= 2:  # 特殊情况处理
# #         return None
# #     new_list = lst.copy()  # 复制，避免修改原始数据
# #     new_list.remove(max(new_list))
# #     new_list.remove(min(new_list))
# #     return sum(new_list) / len(new_list)
# #
# # lis = []
# # while True:
# #     nnn = int(input("请输入数字(输入 0 结束)："))
# #     if nnn == 0:
# #         break
# #     lis.append(nnn)
# #
# # print("原始列表:", lis)
# # print("去掉最大最小后的平均数:", middle_average(lis))
# # ```
# #
# # 💡 改进：
# #
# # 1. 建议把逻辑封装到函数里，避免全局变量 `lis`。
# # 2. 计算时用 `lst.copy()`，这样不会破坏原始数据。
# # 3. 增加特殊情况处理（如果只有 1 个或 2 个数字，无法计算去掉最大最小后的平均数）。
# #
# # ---
# #
# # ### 📌 总结
# #
# # * **作业 1** → 不要滥用库，能用内置就用内置。
# # * **作业 3** → 不要滥用 `global`，能直接操作列表就好。
# # * **作业 4** → 用函数封装，避免全局变量，同时保护原始数据。
# #
# # ---
# #
# # 要不要我帮你把这 4 个作业合并成一个更整洁的完整脚本，你直接运行就能看到效果？
#
# import math
#
# # 作业 1: 列表最大值、最小值、平均值
# print("===== 作业1 =====")
# nums = [3, 7, 1, 9, 5]
# print("列表:", nums)
# print("最大值:", max(nums))
# print("最小值:", min(nums))
# print("平均值:", sum(nums) / len(nums))
#
# # 作业 2: 操作 friends 列表
# print("\n===== 作业2 =====")
# friends = ["小明", "小红", "小刚"]
# friends.append("小丽")
# print("添加小丽:", friends)
# friends.remove("小红")
# print("删除小红:", friends)
#
# # 作业 3: 输入水果直到“结束”
# print("\n===== 作业3 =====")
# fruits = []
# while True:
#     user_input = input("请输入水果名称(输入 '结束' 结束)：")
#     if user_input == "结束":
#         break
#     fruits.append(user_input)
# print("最终水果列表:", fruits)
#
# # 作业 4: 去掉最大最小后的平均值
# print("\n===== 作业4 =====")
# def middle_average(lst):
#     if len(lst) <= 2:
#         return None
#     new_list = lst.copy()
#     new_list.remove(max(new_list))
#     new_list.remove(min(new_list))
#     return sum(new_list) / len(new_list)
#
# lis = []
# while True:
#     nnn = int(input("请输入数字(输入 0 结束)："))
#     if nnn == 0:
#         break
#     lis.append(nnn)
#
# print("原始列表:", lis)
# result = middle_average(lis)
# if result is None:
#     print("元素太少，无法计算去掉最大最小后的平均数")
# else:
#     print("去掉最大最小后的平均数:", result)
# # 确实，如果 input() 可能输入 "quit"，那就不能直接用 int(input(...))，否则一旦输入不是数字就会报错。
# #
# # 解决办法是：先用 input() 读入字符串，然后判断是不是 "quit"，如果不是再转成数字。这样就能避免报错。
# #
# # 修改后的代码示例：
# #
# # lis = []
# # while True:
# #     user_input = input("请输入数字 (输入 quit 结束)：")
# #     if user_input == "quit":   # 先判断是否退出
# #         break
# #     try:
# #         nnn = int(user_input)  # 尝试转换成整数
# #         lis.append(nnn)
# #     except ValueError:
# #         print("请输入有效的整数，或输入 quit 结束。")
# #
# # print("原始列表:", lis)
# #
# #
# # 这样做的好处：
# #
# # 允许用户输入 "quit" 正常退出；
# #
# # 如果用户误输 "abc" 这样的非法输入，不会报错，而是提示重新输入；
# #
# # 输入的数字会被转换成整数再加入列表。