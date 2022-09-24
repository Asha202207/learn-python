"""
演示面向对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法
# class Phone:
#
#     __current_voltage = 0.5   # 当前手机运行电压
#
#     def __keep_single_core(self):
#         print("让CPU以单核模式运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("5G通话已开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足，无法使用5G通话，并已设置单核模式运行进行省电")
#
#
# phone = Phone()
# phone.call_by_5g()
# phone.__keep_single_core()
# print(phone.__current_voltage)

"""
讲解面向对象—封装特性课后练习题
设计带有私有成员的手机
"""


# 设计一个类，用来描述手机
class Phone:
    # 提供私有成员变量： __is_5g_enable
    __is_5g_enable = True  # 5g状态

    # 提供私有成员方法：__check_5g()
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    # 提供公开成员方法：call_by_5g()
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
