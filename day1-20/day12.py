# 1.定义一个字典 person = {"name": "小红", "age": 16, "city": "北京"}，输出她的名字和城市。
#
# 2.新增一个键 "hobby"，值为 "画画"，然后修改 "age" 为 17。
#
# 3.删除 "city" 键，打印最终字典。
#
# 4.扩展：写一个程序，让用户输入 3 个英文单词及其中文翻译，存到字典里，然后可以输入英文单词来查询它的中文意思。
# 作业1.定义一个字典 person = {"name": "小红", "age": 16, "city": "北京"}，输出她的名字和城市。
import tkinter as tk
from tkinter import simpledialog, messagebox
# 初始化主窗口
root = tk.Tk()
root.withdraw()
person = {"name": "小红", "age": 16, "city": "北京"}
messagebox.showinfo("作业1",f"她的名字是{person['name']}，她在的城市是{person['city']}")
messagebox.showinfo("作业1",f"作业1完成")
# 作业2.新增一个键 "hobby"，值为 "画画"，然后修改 "age" 为 17。
person["hobby"]="画画"
person["age"]=17
messagebox.showinfo("作业2",f"她的年龄是{person['age']}，她在的爱好是{person['hobby']}")
messagebox.showinfo("作业2",f"作业2完成")
# 作业3.删除 "city" 键，打印最终字典。
del person["city"]
messagebox.showinfo("作业3",f"她的名字是{person['name']}，年龄是{person['age']}，她在的爱好是{person['hobby']}；当前的字典所有的键对值有{person.items()}")
messagebox.showinfo("作业3",f"作业3完成")
# 作业4.写一个程序，让用户输入 3 个英文单词及其中文翻译，存到字典里，然后可以输入英文单词来查询它的中文意思。
tran= {}
n=1
while n<=3:
    key=simpledialog.askstring("作业4",f"请输入第{n}英文单词：")
    value=simpledialog.askstring("作业4",f"请输入第{n}中文翻译：")
    tran[key]=value
    messagebox.showinfo("作业4", f"当前的字典所有的键对值有{len(tran)}个，分别为{tran.items()}")
    n+=1
else:messagebox.showinfo("作业4", f"您已经输入三个，分别为{tran.items()}输入结束")
find= simpledialog.askstring("作业4","请输入你要查询的英文单词：")
messagebox.showinfo("作业4",f"{find}的中文意思为{tran[find]}")

import tkinter as tk
from tkinter import simpledialog, messagebox

# 初始化主窗口
root = tk.Tk()
root.withdraw()

# 1~3 题你的实现可以保留；第 4 题写成函数化版本

def collect_translations(k: int = 3) -> dict[str, str]:
    """收集 k 个英文→中文的词条，统一对英文做小写与去空格，支持覆盖确认。"""
    d: dict[str, str] = {}
    n = 1
    while n <= k:
        en = simpledialog.askstring("作业4", f"请输入第 {n} 个英文单词：")
        if en is None:  # 用户取消
            break
        en = en.strip()
        if not en:
            messagebox.showinfo("提示", "英文不能为空，请重新输入。")
            continue

        zh = simpledialog.askstring("作业4", f"请输入“{en}”的中文翻译：")
        if zh is None:
            break
        zh = zh.strip()
        if not zh:
            messagebox.showinfo("提示", "中文不能为空，请重新输入。")
            continue

        key = en.lower()  # 统一小写存储，方便忽略大小写查询
        if key in d:
            # 如已存在，询问是否覆盖
            if not messagebox.askyesno("覆盖确认", f"“{en}”已存在，是否覆盖其翻译？"):
                continue

        d[key] = zh
        n += 1
    return d

def preview_dict(d: dict[str, str]) -> None:
    """美观地预览词典内容。"""
    if not d:
        messagebox.showinfo("作业4", "词典为空。")
        return
    pairs = "\n".join(f"{k} → {v}" for k, v in d.items())
    messagebox.showinfo("作业4", f"已录入：\n{pairs}")

def lookup_loop(d: dict[str, str]) -> None:
    """支持多次查询，回车空白或取消结束。查询忽略大小写。"""
    if not d:
        messagebox.showinfo("查询", "词典为空，无法查询。")
        return
    while True:
        q = simpledialog.askstring("查询", "请输入要查询的英文（取消或留空结束）：")
        if not q:  # None 或 空字符串
            break
        ans = d.get(q.strip().lower())
        if ans is None:
            messagebox.showinfo("查询结果", f"未找到 “{q}”。")
        else:
            messagebox.showinfo("查询结果", f"{q} 的中文是：{ans}")

# 运行第 4 题：先收集，再预览，最后进入查询循环
tran = collect_translations(k=3)
preview_dict(tran)
lookup_loop(tran)
