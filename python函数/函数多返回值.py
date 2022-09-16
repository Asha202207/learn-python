"""
演示函数的多返回值示例
"""


# 演示使用多个变量，接收多个返回值
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)

"""
演示多种传参的形式
"""


def user_info(name, age, gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


# 位置参数 - 默认使用形式   顺序不能乱
user_info(20, "小明", "男")
# 关键字参数  顺序可以打乱
user_info(name='小王', age=11, gender='女')
user_info(age=10, gender='女', name='霏霏')
user_info('霏霏', gender='女', age=23)


# 缺省参数（默认值）
def user_info(name, age, gender='男'):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")


user_info('小天', 13)
user_info('小天', 13, '女')


# 不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是：{args}")


user_info(1, 2, 3, '小明', '男孩')


# 不定长 - 关键字不定长，**号
# 不定长定义的形式参数会作为字典存在，接收不定长数量的参数传入
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")


user_info(name='小王', age=11, gender='男孩', addr='北京')

"""
演示函数作为参数传递
"""


# 定义一个函数，接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2)  # 确定compute是函数
    print(type(compute))
    print(f"计算结果：{result}")


# 定义一个函数，准备作为参数传入另一个函数
def compute(x, y):
    return x + y


# 调用，并传入函数
test_func(compute)

"""
演示lambda匿名函数
"""


# 定义一个函数，接收其他函数输入
def test_func(compute):
    result = compute(1, 2)  # 确定compute是函数
    print(f"结果：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test_func(lambda x, y: x + y)
test_func(lambda x, y: x + y)
