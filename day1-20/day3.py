# # 📚1.输入一个数字，判断它是正数、负数还是零。
# #
# # 📖2.用 for 循环打印 1~10 的平方。
# #
# # 📙3.输入一个数字 n，计算 1+2+3+…+n 的和（用 while 循环）。
# # 首先是作业1📚输入一个数字，判断它是正数、负数还是零。
# # 话不多说 开导！有没有别的好玩的用户输入方式呢 这个玩的有点腻了
# import tkinter as tk
# from tkinter import simpledialog, messagebox
# # 导入库
# root=tk.Tk()
# root.withdraw()
# # 主窗口 并隐藏
# use_input= simpledialog.askstring('Let me see your ingredients！','Brother, enter the number you like！')
# if use_input is None:
#     messagebox.showinfo("I've seen through everything!",f"Why don't you type it in? Is it because you haven't grown hands?")
# elif use_input is ValueError :
#     messagebox.showinfo("I've seen through everything!",f"Don't you have a brain? Are the input numbers")
# else:
#     num=float(use_input)
# if num >0:
#     messagebox.showinfo("I've seen through everything!", f"The number you entered ({num}) is greater than 0")
# elif num == 0:
#     messagebox.showinfo("I've seen through everything!", f"If you have something wrong with your brain, what you input is 0!")
# else :
#     messagebox.showinfo("I've seen through everything!", f"The number you entered ({num}) is smaller than 0")
# # 下面是作业2📖用 for 循环打印 1~10 的平方。
# end=int(simpledialog.askstring("Square output",f"How many squares from 1 do you want to output?"))
# sum=0
# for i in range(end):
#     out=(i+1)*(i+1)
#     sum=sum+out
#     messagebox.showinfo("Square output", f"The number you entered is{num}.\nStarting from the number 1.\nThe current number to be squared is{i+1}\nTheir squares are respectively{out}.\nAt present, their sum is{sum}")
# # 作业2📖结束了
# # 作业3📙输入一个数字 n，计算 1+2+3+…+n 的和（用 while 循环）。
# n=1
# sum1=0
# end1=int(simpledialog.askstring("Sum output",f"How many sum from 1 do you want to output?"))
# while n<=end1:
#     sum1+=n
#     messagebox.showinfo("Sum output",
#                         f"The number you entered is{end1}.\nStarting from the number 1.\nTheir sum are respectively{sum1}.")
#     n+=1
# # 完成了 happy!😁
#
#
#
# # 我认真看了一下你写的代码，整体思路非常好，三道题都实现了 🎉！不过里面有几个小问题和可以优化的地方，我帮你点出来，方便你改进：
# #
# # ---
# #
# # ### 🔍 1. 作业 1：输入一个数字，判断正负零
# #
# # ```python
# # elif use_input is ValueError :
# # ```
# #
# # 这一句其实是无效的，因为 `ValueError` 是异常类型，而不是输入的值。
# # 如果要判断用户输入的不是数字，你应该用 `try...except` 来捕获错误，例如：
# #
# # ```python
# # try:
# #     num = float(use_input)
# # except ValueError:
# #     messagebox.showinfo("输入错误", "输入的不是数字，请重新运行程序！")
# #     exit()
# # ```
# #
# # 这样就能更健壮地处理“用户输错东西”的情况。
# #
# # ---
# #
# # ### 🔍 2. 作业 2：for 循环打印平方
# #
# # 现在的写法是每次循环都弹窗，用户体验有点“被轰炸” 😂。
# # 你可以把所有结果拼接成一个字符串，最后一次性弹出。例如：
# #
# # ```python
# # end = int(simpledialog.askinteger("平方输出", "请输入要输出平方的最大数字："))
# # result = ""
# # for i in range(1, end+1):
# #     result += f"{i} 的平方是 {i*i}\n"
# # messagebox.showinfo("平方结果", result)
# # ```
# #
# # 这样更直观。
# #
# # ---
# #
# # ### 🔍 3. 作业 3：while 循环求和
# #
# # ```python
# # while n<end1:
# #     sum1+=n
# #     ...
# #     n+=1
# # ```
# #
# # 这里有个小问题：循环条件用 `< end1`，所以如果用户输入 `5`，你只会加到 `4`，最后结果不完整。
# # 应该写成 `while n <= end1:`。
# #
# # 另外，这里也可以优化展示效果，把最终结果一次性输出，而不是每加一次就弹一个窗口。
# #
# # ---
# #
# # ### ✅ 总结
# #
# # 你已经基本掌握了：
# #
# # * **条件语句**（if / elif / else）
# # * **for 循环**
# # * **while 循环**
# # * **用户输入与数据处理**
# #
# # 这些都是非常重要的基础。
# # 如果改进一下异常处理和展示方式，你的程序就会更健壮、更好用了。
# #
# # ---
# #
# # 要不要我帮你把这三道题的 **改进版本（优化用户体验 + 异常处理）** 写出来给你参考？
#
#
#
# # 好的 👍 我来帮你写一个 **改进版本**，主要改进两点：
# #
# # 1. **用户输入更健壮**（用 `askinteger` / `askfloat`，并加 `try...except` 防止输错）
# # 2. **输出更友好**（减少反复弹窗，把结果汇总展示）
# #
# # ---
# #
# # ## ✨ 改进版完整代码
# #
# # ```python
# # import tkinter as tk
# # from tkinter import simpledialog, messagebox
# #
# # # 初始化窗口
# # root = tk.Tk()
# # root.withdraw()
# #
# # # ---------------- 作业1 📚 判断正负零 ----------------
# # try:
# #     num = simpledialog.askfloat("数字判断", "请输入一个数字：")
# #     if num > 0:
# #         result1 = f"你输入的数字 {num} 是正数 ✅"
# #     elif num == 0:
# #         result1 = f"你输入的数字 {num} 是零 🟡"
# #     else:
# #         result1 = f"你输入的数字 {num} 是负数 ❌"
# # except (TypeError, ValueError):
# #     result1 = "输入无效，请输入数字！"
# #
# # messagebox.showinfo("作业1结果", result1)
# #
# # # ---------------- 作业2 📖 for 循环打印平方 ----------------
# # try:
# #     end = simpledialog.askinteger("平方输出", "请输入要输出平方的最大数字 n：")
# #     if end is None:
# #         result2 = "你没有输入任何数字。"
# #     else:
# #         result2 = "平方结果如下：\n"
# #         for i in range(1, end+1):
# #             result2 += f"{i} 的平方是 {i*i}\n"
# # except (TypeError, ValueError):
# #     result2 = "输入无效，请输入整数！"
# #
# # messagebox.showinfo("作业2结果", result2)
# #
# # # ---------------- 作业3 📙 while 循环求和 ----------------
# # try:
# #     end1 = simpledialog.askinteger("求和", "请输入要求和的最大数字 n：")
# #     if end1 is None:
# #         result3 = "你没有输入任何数字。"
# #     else:
# #         n = 1
# #         total = 0
# #         while n <= end1:
# #             total += n
# #             n += 1
# #         result3 = f"从 1 加到 {end1} 的和是 {total} 🎉"
# # except (TypeError, ValueError):
# #     result3 = "输入无效，请输入整数！"
# #
# # messagebox.showinfo("作业3结果", result3)
# # ```
# #
# # ---
# #
# # ## 🔑 改进点说明
# #
# # 1. **异常处理**：
# #
# #    * 如果用户点“取消”或者输入错误，不会报错，而是友好提示。
# #    * 使用 `askfloat` / `askinteger` 直接获取数字，避免手动 `float()` 转换出错。
# #
# # 2. **输出优化**：
# #
# #    * for 循环和 while 循环的结果都汇总成字符串，一次性展示，避免弹窗轰炸。
# #
# # 3. **逻辑修正**：
# #
# #    * while 循环条件改为 `<=`，保证包含最后一个数。
# #
# # ---
# #
# # 要不要我再帮你把 **每道题的流程图** 画出来（判断、循环的逻辑），这样你理解起来会更直观？
