# 定义函数
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
# str1 = "zhanghan"
# str2 = "xuwenfei"
# my_len(str1)
# my_len(str2)

"""
函数定义语法
"""
# def say_hi():
#     print("Hi,我是张瀚，我是许雯霏老公")
# 调用函数
# say_hi()

"""
练习案例——自动查核酸
"""
# 定义函数
# def check():
#     print("欢迎来到北京！\n请出示您的健康吗及72小时核酸")
# 调用函数
# check()

"""
演示函数的传入参数
"""

# 定义2数相加的函数，通过参数接收被计算的2个数字
# def add(x, y, z):
#     result = x + y + z
#     print(f"{x}+{y}+{z}的计算结果是：{result}")


# 调用函数，传入被计算的2个数字
# add(5, 6, 7)

"""
练习案例——升级版自动查核酸
"""
# 定义函数，接收1个形式参数，数字类型，表示体温
# def check(num):
#     # 在函数体内进行判断体温
#     print("欢迎来到北京！请出示您的健康吗及72小时核酸证明，并配合测量体温")
#     if num <=37.5:
#         print(f"体温测量中，您的体温是：{num}度，体温正常请进！")
#     else:
#         print(f"体温测量中，您的体温是：{num}度，需要隔离！")
# # 调用函数，输入实际参数
# check(37.8)

"""
演示：定义函数返回值的语法形式
"""

# 定义一个函数，完成两数相加的功能
# def add(a, b):
#     result = a + b
# 通过返回值，将相加的结果返回给调用值
# return result
# 返回结果后，还想输出一句话
# print("我完事了") return后面不执行


# 函数返回值，可以通过变量去接收
# r = add(5, 6)
# print(r)

"""
演示特殊字变量:Bone
"""

# 无return语句的函数返回值
# def say_hi():
#     print("你好呀")
#
# result = say_hi()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# 主动返回None的函数
# def say_hi2():
#     print("你好呀")
#     return None
#
# result = say_hi2()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# None用于if判断
# def check_age(age):
#     if age > 18:
#         return "SUCCESS"
#     else:
#         return None
#
#
# result = check_age(16)
# if not result:
#     # 进入if表示result是None值 也就是False
#     print("未成年，不可进入")
# # def check_age(age):
# #     if age > 18:
# #         return "SUCCESS"
# #     else:
# #         print("未成年，不可进入")
# # a = input()
# # result = check_age(int(a))
#
# # None用于声明无初始内容的变量
# name = None

"""
演示嵌套调用函数
"""

# # 定义函数func_b
# def func_b():
#     print("----2----")
#
#
# # 定义函数fun_a,并在内部调用func_b
# def func_a():
#     print("----1----")
#
#     # 嵌套调用func_b
#     func_b()
#
#     print("----3----")
#
#
# # 调用func_a
# func_a()

"""
演示在函数使用的时候，定义的变量作用域
"""

# # 演示局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()
# # 出了函数，局部变量就无法使用
# # print(num)
#
# # 演示全局变量
# num = 200
#
#
# def test_a():
#     print(f"test_a:{num}")
#
#
# def test_b():
#     # global关键字，在函数内声明变量为全局变量
#     global num
#     num = 500
#     print(f"test_b:{num}")
#
#
# test_a()
# test_b()
# print(num)

"""
综合案例：瀚瀚ATM
"""

# # 定义全局变量money name
# money = 5000000
# name = None
# # 要求客户输入姓名
# name = input("请输入您的姓名：")
#
#
# # 定义查询函数
# def query(show_header):
#     if show_header:
#         print("------查询余额------")
#     print(f"{name},您好，您的余额剩余：{money}元")
#
#
# # 定义存款函数
# def saving(num):
#     global money  # money在函数内部定义为全局变量
#     money += num
#     print("------存款------")
#     print(f"{name},您好，您存款{num}元成功。")
#
#     # 调用query函数查询余额
#     query(False)
#
# #定义取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("------存款------")
#     print(f"{name},您好，您取款{num}元成功。")
#
#     # 调用query函数查询余额
#     query(False)
# # 定义主菜单函数
# def main():
#     print("------主菜单------")
#     print(f"{name}您好，欢迎来到瀚瀚银行ATM，请选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入您的选择：")
#
# # 设置诬陷循环，确保程序不退出
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue
#     elif keyboard_input == "2":
#         num = input("您想要存多少钱？请输入：")
#         saving(int(num))
#         continue
#     elif keyboard_input == "3":
#         num = input("您想要取多少钱？请输入：")
#         get_money(int(num))
#         continue
#     else:
#         print("程序退出")
#         break


money = 500000
name = None
name = input("请输入您的姓名：")


def query(show_header):
    if show_header:
        print("------查询余额------")
    print(f"{name},您好，您的余额为{money}")


def saving(num):
    global money
    money += num
    print("------存款------")
    print(f"{name},您好，您存款{money}元成功。")
    query(False)


def get_money(num):
    global money
    money -= num
    print("------取款------")
    print(f"{name},您好，您取款{money}元成功。")
    query(False)


def main():
    print("------主菜单------")
    print(f"{name},您好，请选择您的操作：")
    print("查询余额\t[请输入1]")
    print("存款\t\t[请输入2]")
    print("取款\t\t[请输入3]")
    print("退出\t\t[请输入4]")
    return input("请输入您的选择：")


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = input("您想要存多少钱，请输入：")
        saving(int(num))
        continue
    elif keyboard_input == "3":
        a = input("您想要取多少钱，请输入：")
        get_money(int(a))
        continue
    else:
        print("程序退出")
        break
