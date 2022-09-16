"""
演示捕获异常
"""

# 基本捕获语法
# try:
#     f = open("D:/abc.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在，我将open模式，改为w模式去打开")
#     f = open("D:/abc.txt", "w", encoding="UTF-8")

# 捕获指定异常
# try:
#     # print(name)
#     1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)
# # 捕获多个异常
# try:
#     # 1 / 0
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除以0的异常错误")
# 未正确设置捕获异常类型，将无法捕获异常

# 捕获所有异常
# try:
#     f = open("D:/123.txt", "r")
# except Exception as e:
#     print("文件出现异常")
# else:
#     print("好高兴，没有出现异常")
# finally:
#     print("我是finally,有没有异常我都要执行")
#     f.close()

"""
演示异常的传递性
"""


# 定义一个出现异常的方法
def func1():
    print("func1 开始执行")
    num = 1 / 0  # 肯定有异常，除以0的异常
    print("func1 结束执行")


# 定义一个无异常的方法，调用上面的方法
def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")


# 定义一个方法，调用上面的方法

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常信息是：{e}")


main()

"""
演示python的模块导入
"""

# 使用import导入time模块使用sleep功能（函数）
# import time # 导入python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)  # 通过，就可以使用模块内部的全部功能（类、函数、变量）
# print("我好")
# 使用from导入time的sleep功能（函数）
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")
# 使用 * 导入time模块的全部功能
# from time import *  # *表示全部的意思
# print("你好")
# sleep(5)
# print("我好")
# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

print("你好")
# sl(5)
print("我好")

"""
演示自定义模块
"""

# 导入自定义模块使用
# import my_module1
# my_module1.test(1, 2)
# from my_module1 import test
# test(1, 2)
# 导入不同模块的同名功能    只能使用导入的最后一个模块
# from my_module1 import test
# from my_module2 import test
# test(1, 2)
# __main__变量
# from my_module1 import test

# __all__变量
from my_package.my_module1 import *
# test_a(1, 2)
# test_b(2, 1)


"""
演示python的包
"""

# 创建一个包
# 导入自定义的包中国的模块，并使用
# import my_package.my_module1
# import  my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
from my_package import *
my_module1.info_print1()
# my_module2.info_print2() all变量控制 * 只能导入my_module1模块

"""

"""
