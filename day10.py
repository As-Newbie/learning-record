# # 1.定义一个字符串 "hello world"，输出它的长度、第一个字符、最后一个字符。
# #
# # 2.定义一个字符串 "Python Programming"，把它变成全大写，再输出它的前 6 个字母。
# #
# # 3.写一个程序，循环让用户输入一句话，直到输入 "quit" 结束，并统计输入过的所有句子数量。
# #
# # 4.扩展练习：写一个函数，接收一句话，返回其中的单词数量（提示：可以用 split() 方法）。
# # 作业1 定义一个字符串 "hello world"，输出它的长度、第一个字符、最后一个字符。
# import tkinter as tk
# from tkinter import simpledialog, messagebox
#
# from PIL.ImImagePlugin import number
#
# # 初始化主窗口
# root = tk.Tk()
# root.withdraw()
# work1="hello world"
# messagebox.showinfo("作业1",f"字符串的长度为{len(work1)}、第一个字母为{work1[0]}、最后一个字母为{work1[-1]}")
# messagebox.showinfo("作业1",f"作业1完成")
# # 作业2 定义一个字符串 "Python Programming"，把它变成全大写，再输出它的前 6 个字母。
# work2="Python Programming"
# word_raw=work2
# word_result=word_raw.upper()
# messagebox.showinfo("作业2",f"字符串的大写{word_result}、前六字母为{word_result[0:6]}。")
# messagebox.showinfo("作业2",f"作业2完成")
# # 作业3 写一个程序，循环让用户输入一句话，直到输入 "quit" 结束，并统计输入过的所有句子数量。
# n=-1
# me=[]
# while True:
#     n += 1
#     work3=simpledialog.askstring("作业3",f"请输入你要说的话（输入quit取消）：")
#     me.append(work3)
#     if work3=="quit":
#         me.remove("quit")
#         break
# messagebox.showinfo("作业3",f"输入的句子的数量为{n}，句子为{me}")
# messagebox.showinfo("作业3",f"作业3完成")
# # 这个题没理解怎么写对 现在结果虽然对了但是在凑答案
# # me = []
# # while True:
# #     work3 = simpledialog.askstring("作业3", "请输入你要说的话（输入 quit 结束）：")
# #     if work3 == "quit":
# #         break
# #     me.append(work3)
# #
# # messagebox.showinfo("作业3", f"输入的句子数量为{len(me)}，句子为{me}")
#
# # 作业4 扩展练习：写一个函数，接收一句话，返回其中的单词数量（提示：可以用 split() 方法）。
# def count_words(sentence):
#    words=sentence.split()
#    return len(words)
# sentence1=simpledialog.askstring("作业4",f"请输入你要说的话：")
# messagebox.showinfo("作业4",f"句子的单词个数为{count_words(sentence1)}。")
# messagebox.showinfo("作业4",f"作业4完成")
# # 好像理解了一些函数的用法 但还是不够
