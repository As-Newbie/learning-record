# 作业1：继承
# 定义一个 Animal 类，有一个方法 speak()，输出 "动物在叫".
# 然后写一个子类 Dog，继承 Animal，不用写新代码，直接调用 Dog().speak() 看看效果。
# 作业2：方法重写
# 在上面 Dog 类里，重写 speak() 方法，让它输出 "汪汪！".
# 然后再写一个 Cat 类，让它输出 "喵喵！".
# 作业3：多态
# 把 Animal、Dog、Cat 都放进一个列表里，遍历列表，依次调用它们的 speak() 方法。
# 作业1：定义一个 Animal 类，有一个方法 speak()，输出 "动物在叫".
#  然后写一个子类 Dog，继承 Animal，不用写新代码，直接调用 Dog().speak() 看看效果。
class Animal:
    def speak(self):
        print("动物在叫")
class Dog(Animal):
    pass
Dog().speak()
# 作业2：方法重写
# 在上面 Dog 类里，重写 speak() 方法，让它输出 "汪汪！".
# 然后再写一个 Cat 类，让它输出 "喵喵！".
class Animal:
    def speak(self):
        print("动物在叫")
class Dog(Animal):
    def speak(self):
        print("汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵")
Dog().speak()
Cat().speak()
# 作业3：多态
# 把 Animal、Dog、Cat 都放进一个列表里，遍历列表，依次调用它们的 speak() 方法。
class Animal:
    def speak(self):
        print("动物在叫")
class Dog(Animal):
    def speak(self):
        print(f"汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵")
end=[Animal(),Dog(),Cat()]
for e in end:
    e.speak()