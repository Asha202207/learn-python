"""
演示类和对象的关系，即面向对象的编程套路（思想）
"""

# 设计一个闹钟类
# class Clock:
#     id = None  # 序列化
#     price = None  # 价格
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)


# 构建2个闹钟对象并让其工作
# clock1 = Clock()
# clock1.id = "003032"
# clock1.price = 19.99
# print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock1.ring()
#
# clock2 = Clock()
# clock2.id = "003033"
# clock2.price = 21.99
# print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock2.ring()

"""
演示类的构造方法
"""


# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__

class Student:
    name = None
    age = None
    tell = None

    def __init__(self, name, age, tell):
        self.name = name
        self.age = age
        self.tell = tell
        print(f"Student类创建了一个类对象")


stu = Student("周杰伦", 31, "18500006666")
print(stu.name, stu.age, stu.tell)

"""
魔术方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name  # 学生姓名
        self.age = age  # 学生年龄

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象：name:{self.name}, age:{self.age}"

    # # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周杰伦", 31)
stu2 = Student("林俊杰", 36)
print(stu1 == stu2)
print(stu1 >= stu2)
