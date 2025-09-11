# 作业1：继承
# 写一个 Shape 类，有一个方法 area()，输出 "这是一个形状".
# 然后写一个子类 Circle，继承 Shape，不用写新代码，直接调用 Circle().area()。
# 作业2：方法重写
# 在 Circle 里重写 area() 方法，计算圆的面积：
# 公式：面积 = 3.14 × 半径²
# 提示：在 __init__() 方法里定义 radius（半径）。
# 作业3：多态
# 再写一个 Square 类，计算正方形面积（边长 × 边长）。
# 把 Circle、Square 都放进列表里，依次调用 area()，看看效果。
# 作业1
class Shape:
    def area(self):
        print(f"这是一个形状")
class Circle(Shape):
    pass
Circle().area()
# 作业2
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area_value=3.14*self.radius**2
        print(f"圆的面积是{area_value}")
s1=Circle(1)
s1.area()
# 作业3
class Square(Shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        area_value=self.a*self.b
        print(f"矩形的面积是{area_value}")
shape=[Shape(),Circle(1),Square(2,3)]
for s in shape:
    s.area()