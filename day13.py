# 1.写一个小程序，要求用户输入一个数字，如果不是整数，就提示“输入错误，请输入整数”，直到输入正确为止。
# 2.写一个程序，把几行文字写入 my_note.txt 文件，再读出来显示在控制台。
# 3.用 tkinter + filedialog 做一个简单“记事本”：
# 提供一个按钮“打开文件”，能选择并显示文件内容。
# 提供一个按钮“保存文件”，能把修改过的内容保存回去。
# 要求加入异常处理（例如用户没选文件时，程序不会崩溃）。
# 作业1 写一个小程序，要求用户输入一个数字，如果不是整数，就提示“输入错误，请输入整数”，直到输入正确为止。
while True:
    try :
        num=int(input("请输入整数："))
        print(f"你输入的整数是{num}")
        break
    except ValueError:
        print(f"你不知道什么是整数吗")
        continue
# 作业2 写一个程序，把几行文字写入 my_note.txt 文件，再读出来显示在控制台。
import tkinter as tk
from tkinter import filedialog,messagebox

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

with open("my_note.txt","w",encoding="utf-8") as f:
    f.write("你好，Python！")
    f.close()
with open("my_note.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容为",content)
# 作业3.用 tkinter + filedialog 做一个简单“记事本”：
# 提供一个按钮“打开文件”，能选择并显示文件内容。
# 提供一个按钮“保存文件”，能把修改过的内容保存回去。
# 要求加入异常处理（例如用户没选文件时，程序不会崩溃）。
import tkinter as tk
from tkinter import filedialog, messagebox

# 定义一个名为SimpleNotepad的类，用于创建记事本应用
class SimpleNotepad:
    # __init__方法是类的构造函数，在创建对象时自动调用
    # self代表类的实例本身，root是Tkinter的主窗口对象[1,2,3](@ref)
    def __init__(self, root):
        # 保存主窗口引用，以便后续使用
        self.root = root
        # 设置窗口标题，初始显示"未命名"[9](@ref)
        self.root.title("简单记事本 - 未命名")
        # 文件路径，初始为None表示未保存过的新文件
        self.file_path = None
        # 修改标志，False表示文件未被修改
        self.modified = False

        # 创建按钮栏框架容器
        btn_frame = tk.Frame(root)
        # 将按钮栏填充到窗口顶部（x方向）
        btn_frame.pack(fill='x')
        # 创建新建按钮，点击时调用new_file方法
        tk.Button(btn_frame, text="新建", command=self.new_file).pack(side='left')
        # 创建打开按钮，点击时调用open_file方法
        tk.Button(btn_frame, text="打开", command=self.open_file).pack(side='left')
        # 创建保存按钮，点击时调用save_file方法
        tk.Button(btn_frame, text="保存", command=self.save_file).pack(side='left')
        # 创建另存为按钮，点击时调用save_as方法
        tk.Button(btn_frame, text="另存为", command=self.save_as).pack(side='left')

        # 创建文本区域框架容器
        text_frame = tk.Frame(root)
        # 将文本区域填充整个窗口并允许扩展
        text_frame.pack(fill='both', expand=True)
        # 创建文本编辑区域，设置自动换行[9](@ref)
        self.text = tk.Text(text_frame, wrap='word')
        # 将文本区域放置在左侧并填充整个空间
        self.text.pack(side='left', fill='both', expand=True)
        # 创建滚动条，与文本区域的y视图关联
        scroll = tk.Scrollbar(text_frame, command=self.text.yview)
        scroll.pack(side='right', fill='y')
        # 设置文本区域的滚动条控制
        self.text.config(yscrollcommand=scroll.set)

        # 绑定文本修改事件，当内容改变时触发on_modified方法
        self.text.bind('<<Modified>>', self.on_modified)

    # 当文本内容被修改时调用的方法
    def on_modified(self, event=None):
        # 重置修改标志，否则事件会持续触发
        self.text.edit_modified(False)
        # 如果之前未被标记为已修改
        if not self.modified:
            # 设置修改标志为True
            self.modified = True
            # 更新窗口标题显示未保存标识
            self.update_title()

    # 更新窗口标题的方法
    def update_title(self):
        # 获取文件名，如果有文件路径则使用路径，否则显示"未命名"
        name = self.file_path if self.file_path else "未命名"
        # 如果文件已被修改但未保存，添加星号标记
        mark = "*" if self.modified else ""
        # 设置窗口标题
        self.root.title(f"简单记事本 - {name}{mark}")

    # 创建新文件的方法
    def new_file(self):
        # 如果当前文件已被修改，询问是否保存
        if self.modified:
            if not self.ask_save_changes():
                return  # 用户取消操作
        # 重置文件路径
        self.file_path = None
        # 清空文本区域内容（从第1行第0字符到末尾）
        self.text.delete('1.0', 'end')
        # 重置修改标志
        self.modified = False
        # 更新窗口标题
        self.update_title()

    # 询问是否保存更改的方法
    def ask_save_changes(self):
        # 显示是/否/取消对话框
        ans = messagebox.askyesnocancel("未保存", "当前文件有未保存的更改，要保存吗？")
        if ans is None:
            return False  # 用户点击取消，不继续操作
        if ans:
            return self.save_file()  # 用户点击是，尝试保存文件
        return True  # 用户点击否，不保存但继续操作

    # 打开文件的方法
    def open_file(self):
        # 如果当前文件已被修改，询问是否保存
        if self.modified:
            if not self.ask_save_changes():
                return  # 用户取消操作
        # 显示文件打开对话框，过滤文本文件[9](@ref)
        path = filedialog.askopenfilename(title="打开文件", filetypes=[("文本文件","*.txt"),("所有文件","*.*")])
        if not path:
            return  # 用户取消选择
        try:
            # 尝试以UTF-8编码读取文件
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                # 如果UTF-8解码失败，尝试GBK编码（常见于中文系统）
                with open(path, 'r', encoding='gbk') as f:
                    content = f.read()
            # 清空当前文本区域
            self.text.delete('1.0', 'end')
            # 插入文件内容（从第1行第0字符开始）
            self.text.insert('1.0', content)
            # 更新文件路径
            self.file_path = path
            # 重置修改标志
            self.modified = False
            # 更新窗口标题
            self.update_title()
        except FileNotFoundError:
            messagebox.showerror("错误", "文件未找到。")
        except Exception as e:
            messagebox.showerror("错误", f"读取文件时发生错误：{e}")

    # 保存文件的方法
    def save_file(self):
        # 如果没有文件路径（新文件），调用另存为方法
        if not self.file_path:
            return self.save_as()
        try:
            # 获取文本内容（从第1行第0字符到倒数第1个字符，避免多余换行）
            text = self.text.get('1.0', 'end-1c')
            # 以UTF-8编码写入文件
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            # 重置修改标志
            self.modified = False
            # 更新窗口标题
            self.update_title()
            return True  # 保存成功
        except Exception as e:
            messagebox.showerror("错误", f"保存文件失败：{e}")
            return False  # 保存失败

    # 另存为文件的方法
    def save_as(self):
        # 显示文件保存对话框，默认扩展名为.txt
        path = filedialog.asksaveasfilename(title="另存为", defaultextension=".txt",
                                            filetypes=[("文本文件","*.txt"),("所有文件","*.*")])
        if not path:
            return False  # 用户取消操作
        try:
            # 获取文本内容
            text = self.text.get('1.0', 'end-1c')
            # 以UTF-8编码写入文件
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
            # 更新文件路径
            self.file_path = path
            # 重置修改标志
            self.modified = False
            # 更新窗口标题
            self.update_title()
            return True  # 保存成功
        except Exception as e:
            messagebox.showerror("错误", f"另存为失败：{e}")
            return False  # 保存失败

# Python程序入口标准写法
if __name__ == "__main__":
    # 创建Tkinter主窗口
    root = tk.Tk()
    # 设置窗口大小（宽800像素，高600像素）
    root.geometry("800x600")
    # 创建SimpleNotepad应用实例
    app = SimpleNotepad(root)
    # 启动Tkinter事件循环，等待用户交互
    root.mainloop()
