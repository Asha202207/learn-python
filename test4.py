"""
演示for循环的基础语法
"""
# name = "zhanghan"
#
# for x in name:
#     # 将name的内容，挨个取出来赋予x临时变量
#     # 就可以在循环体内对x进行处理
#     print(x)

"""
练习案例：数一数有几个a
"""
# 统计如下字符串，有多少个字母a
# name = "itheima is a brand of itcast"
# 定义一个变量，用来统计有多少个a
# count = 0
# for循环统计
# for临时变量 in 被统计的数据：
# for x in name:
#     if x == "a":
#         count += 1
# print(f"被统计的字符串中有{count}个a")

"""
演示Python中的range()语句的基本使用
"""
# range语法1 rang(num)
# for x in range(10):
#     print(x)
# range 语法2 range(num1,num2)
# for x in range(5, 10):
#     print(x)
# range 语法3 range(num1,num2,step)
# for x in range(5, 10, 2):
#     print(x)
# for x in range(10):
#     print("送玫瑰花")

"""
练习案例：有几个偶数
"""
# num = 100
# count = 0
# for x in range(1, 100):
#     if x % 2 == 0:
#         count += 1
# print(f"有{count}个偶数")

"""
演示python for循环临时变量的左右域
"""
# i = 0
# for i in range(5):
#     print(i)
# print(i)

"""
演示嵌套应用for循环
"""
# 坚持表白100天，每天都送10朵花
# range
# i = 1
# for i in range(1, 101):
#     print(f"今天是向霏霏表白的第{i}天,加油坚持")
#
#     # 写内层循环了
#     for j in range(1, 11):
#         print(f"给霏霏送的第{j}朵玫瑰花")
#     print("霏霏，我喜欢你")
# print(f"第{i}天，表白成功")

"""
练习案例——for循环打印九九乘法表
"""
# i = 1
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j}*{i}={i*j}\t", end='')
#     print("\n")

"""
演示循环语句的中断控制，break和continue
"""
# 演示循环中的continue
# for i in range(1, 6):
#     print("语句1")
#     continue
#     print("语句2")
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
# 演示循环中断语句 break
# for i in range(1 ,6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")

"""
练习案例：发工资
"""
# 定义账户余额变量
money = 10000
# for循环对员工发放工资
for i in range(1, 21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效分{score},不满足，不发工资，下一位")
        # continue
        continue
    # 要判断余额足不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i},满足条件发放工资1000，公司账户余额：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月再来")
        # break结束发放
        break