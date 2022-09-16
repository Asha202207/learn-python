"""
演示Python判断语句：if语句的基本格式应用
"""

age = 18

print(f"我今年已经{age}岁了")
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过的真快")

"""
练习案例：成年人判断
"""
print("欢迎来到黑马游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄："))

if age >= 18:
    print("您已成年，游玩需要补票10元")
    print("祝您游玩愉快")

else:
     print("儿童免费，祝您游玩愉快")

"""
练习案例：成年人判断
"""
print("欢迎来到黑马动物园")
height = int(input("请输入你的身高(cm)："))

if height >= 120:
    print("您的身高超出120cm，游玩需要购票10元")

else:
    print("您的身高未超出120cm，可以免费游玩")

print("祝您游玩愉快")

"""
if_elif_else组合使用
"""
print("欢迎来到黑马动物园")
# height = int(input("请输入你的身高(cm)："))
# vip_level = int(input("请输入你的vip等级（1~5）："))
# day = int(input("请告诉我今天是几号："))

if int(input("请输入你的身高(cm)：")) < 120:
    print("您的身高不超出120cm，可以免费游玩")

elif int(input("请输入你的vip等级（1~5）：")) > 3:
    print("您的vip等级大于3，可以免费游玩")

elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1号免费日，可以免费游玩")

else:
     print("不好意思，条件都不满足，需要买票10元")

"""
练习案例：猜错心里数字
"""
# 定义一个变量数字
num = 5
# 通过键盘输入获得猜想的数字，通过多次if 和 elif的组合进行猜想比较
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("很遗憾，全部猜错了，我想要的数字是：5")

"""
判断语句的嵌套
"""
# print("欢迎来到黑马动物园")
# if int(input("请输入你的身高(cm)：")) > 120:
#     print("你的身高大于120cm，不可以免费")
#     print("不过，如果你的vip等级高于3，可以免费游玩")
#     if int(input("请告诉我你的vip级别：")) > 3:
#         print("恭喜你，你可以免费游玩")
#     else:
#         print("Sorry,你需要补票，10元")
# else:
#     print("欢迎小朋友，可以免费游玩")
# age = int(input("请输入你的年龄"))
# year = int(input("请输入你的工龄"))
# level = int(input("请输入你的级别"))
if int(input("请输入你的年龄")) >=18:
    print("你是成年人")
    if int(input("请输入你的年龄")) < 30:
        print("你的年龄达标了")
        if int(input("请输入你的工龄")) >2:
            print("恭喜你，你的年龄和入职时间都达标，可以领取礼物")
        elif int(input("请输入你的级别")) >3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了")
else:
    print("不好意思，年龄太小了")

"""
演示判断语句的实战案例：终极猜数字
"""
# 1、构建一个随机的数字变量
import random
num = random.randint(1,10)
print(num)

guess_num = int(input("输入你想要的数字："))
# 2、通过if语句进行数字的猜错
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("再一次输入你想要的数字："))
    if guess_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("第三次输入你想要的数字："))
        if guess_num == num:
            print("恭喜，第三次就猜中了")
        else:
            print("三次机会用完了，没有猜中")