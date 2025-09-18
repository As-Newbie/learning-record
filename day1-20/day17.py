class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} 在工作")

class Programmer(Employee):
    def work(self):
        print(f"{self.name} 正在写代码")

class Teacher(Employee):
    def work(self):
        print(f"{self.name} 正在讲课")

class Manager(Employee):
    def work(self):
        print(f"{self.name} 正在开会")
class Designer(Employee):
    def work(self):
        print(f"{self.name} 正在画图")
# # 创建不同员工
# employees = [
#     Programmer("小王"),
#     Teacher("李老师"),
#     Manager("张经理"),
#     Designer("星老师")
# ]
#
# # 统一管理：遍历调用 work()
# for e in employees:
#     e.work()

# 作业2
# 写一个循环菜单，用户输入数字选择角色类型（程序员/老师/经理/设计师），再输入名字，最后加入到员工列表中。
# 输入 0 时退出，并打印所有员工的工作内容。
# 👉 提示：用 while True + input() 实现。
# 员工列表
employees = []

while True:
    print("\n请选择要添加的员工类型：")
    print("1. 程序员")
    print("2. 老师")
    print("3. 经理")
    print("4. 设计师")
    print("0. 退出并显示所有员工")

    choice = input("请输入编号：")

    if choice == "0":
        break  # 退出循环

    name = input("请输入员工名字：")

    if choice == "1":
        employees.append(Programmer(name))
    elif choice == "2":
        employees.append(Teacher(name))
    elif choice == "3":
        employees.append(Manager(name))
    elif choice == "4":
        employees.append(Designer(name))
    else:
        print("输入有误，请重新选择。")

print("\n所有员工的工作内容：")
for e in employees:
    e.work()