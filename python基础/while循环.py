"""
演示while循环的基础应用
"""
# i = 0
# while i < 100:
#     print("许雯霏，我喜欢你")
#     i += 1

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1-100累加的和是：{sum}")

"""
演示while循环的基础案例 - 猜数字
"""
# # 获取范围在1-100的随机数字
# import random
# num = random.randint(1, 100)
# # 定义一个变量，记录总共猜测了多少次
# count = 0
# # 通过一个布尔类型的变量，做循环是否继续的标记
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜测的数字："))
#     count += 1
#     if guess_num == num:
#         print("猜中了")
#         # 设置为False就是终止循环的条件
#         flag = False
#     else:
#         if guess_num > num:
#             print("你猜的大了")
#         else:
#             print("你猜的小了")
#
# print(f"你总共猜测了{count}次")

"""
演示while循环的嵌套使用
"""

# 外层：表白100天的控制
# 内层：每天的表白都送10只玫瑰花的控制
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天，准备表白.....")
#     #内层循环的控制变量
#     j = 1
#     while j <= 10:
#         print(f"送给小美第{j}只玫瑰花")
#         j += 1
#     print("许雯霏，我喜欢你")
#     i += 1
#
# print(f"坚持第{i}天，表白成功")

"""
while嵌套循环案例
"""
# 使用print语句输出不换行
# print("hello", end='')
# print("world", end='')
# print("Hello\tWorld")
# print("zhanghan\tbest")
# 练习案例-打印九九乘法表
# 定义外层循环的控制变量
# i = 1
# while i <= 9:  # 定义内层循环的控制变量
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}\t", end='')
#         j += 1
#     i += 1
#     print()  # print空内容就是输出一个换行




