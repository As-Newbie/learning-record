# 作业1
# 写一个 Employee 类，有 work() 方法，输出 "员工在工作".
# 再写一个 Programmer 类，继承 Employee，重写 work() 方法，输出 "程序员在写代码"。
# 作业2
# 再写一个 Teacher 类，也继承 Employee，work() 方法输出 "老师在讲课"。
# 把 Programmer 和 Teacher 放到一个列表里，用循环依次调用 work()。
# 作业3 （选做，稍微有点进阶）
# 给 Employee 增加一个 __init__() 方法，传入名字（name）。
# 调用 work() 的时候，输出时带上名字，比如：
# "小王正在写代码"
# "李老师正在讲课"
# class Employee:
#     def work(self):
#         print(f"员工在工作")
# class Programmer(Employee):
#     def work(self):
#         print(f"程序员在写代码")
# Programmer().work()
# class Teacher(Employee):
#     def work(self):
#         print(f"老师在讲课")
# occupation=[Programmer(),Teacher()]
# for o in occupation:
#     o.work()
# 作业3
class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(f"{self.name}在工作")
class Programmer(Employee):
    def work(self):
        print(f"{self.name}在写代码")
class Teacher(Employee):
    def work(self):
        print(f"{self.name}在讲课")
occupation=[Programmer("小王"),Teacher("小张")]
for o in occupation:
    o.work()
