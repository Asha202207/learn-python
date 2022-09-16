"""
演示tuple元组的定义和操作
"""

# 定义元组
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元组
t4 = ("Hello",) # 定义单个元素的元组后面必须有空的,
print(f"t4的类型是：{type(t4)},内容是：{t4}")
# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")
# 下标索引去取出内容
num1 = t5[1][2]
num2 = t5[-1][-1]
print(f"从嵌套元组中取出的元素是：{num1}{num2}")
# 元组的操作：index查找方法
t6 = ("张瀚", "许雯霏", "python")
index = t6.index("张瀚")
print(f"在元组t6中查找张瀚，的下标是：{index}")
# 元组的操作：count统计方法
t7 = ("张瀚", "许雯霏", "许雯霏", "许雯霏", "python")
num = t7.count("许雯霏")
print(f"在元组t7中，许雯霏的数量是：{num}")
# 元组的操作：len函数统计元组元素数量
num = len(t7)
print(f"t7元组中元素的数量有：{num}个")
# 元组的遍历：while
index = 0
while index < len(t7):
    print(f"元组的元素有：{t7[index]}")
    # 至关重要
    index += 1
# 元组的遍历：for
for element in t7:
    print(f"元组的元素有：{element}")

# 修改元组内容
# t8[0] = "zhanghan" 元组内容不可以修改
# 定义一个元组
t9 = (1, 2, ["zhanghan", "xuwenfei"])
print(f"t9的内容是：{t9}")
t9[2][0] = "张瀚"
t9[2][1] = "许雯霏"
print(f"t9的内容是：{t9}")


"""
演示以数据容器的角色，学习字符串的相关操作
"""
my_str = "zhanghan and xuwenfei"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串m{my_str}取下标为2的元素值是：{value}，取下标为-16的元素值是：{value2}")
# my_str[2] = "H"  字符串不允许修改
# 字符串.index方法查找字符串
value = my_str.index("and")
print(f"在字符串{my_str}中查找and,其起始下标是：{value}")
# 字符串.repalce方法替换字符串
new_str = my_str.replace("zhanghan", "张瀚")
print(f"将字符串{my_str},进行替换后得到：{new_str}")
# 字符串.split分割字符串(字符串本身不变，得到列表)
my_str = "hello python zhanghan xuwenfei"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行切分后得到：{my_str_list},类型是：{type(my_str_list)}")
# 字符串.strip() 字符串规整操作(去前后空格)
my_str = "  hello python zhanghan xuwenfei  "
print(my_str.strip())
# 字符串.strip(字符串) 字符串规整操作(去前后指定字符串)
my_str = "12hello python zhanghan xuwenfei21"
print(my_str.strip("12"))
# 统计字符串中某字符串的出现次数，count
my_str = "hello python zhanghan xuwenfei"
count = my_str.count("n")
print(f"字符串{my_str}中，n出现的次数是{count}次")
# 统计字符串的长度，len()
num = len(my_str)
print(f"字符串{my_str}的长度是{num}")

"""
练习案例：分割字符串
"""
my_str = "itheima itcast boxuegu"
i = my_str.count("it")
print(f"字符串{my_str}中有：{i}个it字符")
m = my_str.replace(" ", "|")
print(f"字符串{my_str},被替换空格后，结果：{m}")
n = m.split("|")
print(f"字符串{my_str},按照|分割后，得到：{n}")