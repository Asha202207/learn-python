"""

演示数据容器之：list列表
语法：[元素，元素，....]
"""
# 定义一个列表 list
my_list = ["zhanghan", "xuwenfei", "python"]
print(my_list)
print(type(my_list))

my_list = ["zhanghan", 666, True]
print(my_list)
print(type(my_list))

# 通过下标索引去除对应位置的数据
my_list = ["Tom", "Lily", "Rose"]
# 列表[下标索引]，从前向后从0开始，每次+1    从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 通过下标索引取出数据
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
# 取出嵌套列表的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[1][1])

"""
演示数据容器之：List列表的常用操作
"""
mylist = ["zhanghan", "xuwenfei", "python"]
# 1.1 查找某元素在列表内的下标元素
index = mylist.index("xuwenfei")
print(f"xuwenfei在列表中的下标索引值是：{index}")
# 1.2 如果被查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"xuwenfei在列表中的下标索引值是：{index}")

# 2. 修改特定下标索引的值
mylist[0] = "传授教育"
print(f"列表被修改元素值后，结果是：{mylist}")

# 3. .insert(下标，元素)在指定下标位置插入新元素
mylist.insert(1, "best")
print(f"列表插入元素后，结果是：{mylist}")

# 4. .append(元素)在列表的尾部追加'''单个'''新元素
mylist.append("黑马程序员")
print(f"列表在追加了元素后，结果是：{mylist}")

# 5. .extend(其他数据容器)在列表尾部追加'''一批'''新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"列表在追加了一个新的列表后，结果是：{mylist}")

# 6. del列表[下标]/列表.pop(下标)删除指定下标索引的元素(2种方式)
mylist = ["zhanghan", "xuwenfei", "python"]
# 6.1 方式1：del 列表[下标]
del mylist[2]
print(f"列表删除元素后结果是：{mylist}")
# 6.2 方式2：列表pop(下标)
mylist = ["zhanghan", "xuwenfei", "python"]
element = mylist.pop(2)
print(f"通过pop方法移除/取出元素后，列表内容{mylist}，取出的元素是{element}")

# 7. 列表.remove(元素)删除某元素在列表中的第一个匹配项
mylist = ["zhanghan", "zhanghan", "xuwenfei", "xuwenfei", "python"]
mylist.remove("zhanghan")
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 8. 列表.clear()清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 9. 列表.count(元素)统计列表内某元素的数量
mylist = ["zhanghan", "zhanghan", "xuwenfei", "xuwenfei", "python"]
count = mylist.count("zhanghan")
print(f"列表中zhanghan的数量是：{count}")

# 10. len(列表)统计列表中全部的元素数量
mylist = ["zhanghan", "zhanghan", "xuwenfei", "xuwenfei", "python"]
count = len(mylist)
print(f"列表的元素数量总共有：{count}")

"""
练习案例:常用功能练习
"""
# 1. 定义这个列表，并用变量接收它，内容是：[21,25,21,23,22,20]
mylist = [21, 25, 21, 23, 22, 20]
# 2. 追加一个数字31，到列表的尾部
mylist.append(31)
print(mylist)
# 3. 追加一个薪列表[29, 33, 30],到列表的尾部
mylist2 = [29, 33, 30]
mylist.extend(mylist2)
print(mylist)
# 4. 取出第一个元素(应是：21)
element = mylist.pop(0)
print(f"取出的第一个元素是：{element}")
# 5. 取出最后一个元素(应是：30)
element2 = mylist.pop(-1)
print(f"取出的最后一个元素是：{element2}")
# 6. 查找元素31，在列表中的下标位置
index = mylist.index(31)
print(f"31在列表下标的索引值是：{index}")
index = mylist.index(25)
print(f"25在列表下标的索引值是：{index}")


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ["张瀚", "许雯霏", "python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量

    # 定义一个变量用来标记列表的下标
    index = 0  # 初始值为0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        # 至关重要 将循环变量（index）每一次循环都+1
        index += 1


list_while_func()


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    # for 临时变量 in 数据容器：
    for element in my_list:
        print(f"类别的元素：{element}")


list_for_func()

"""
练习案例：取出列表内的偶数
"""
my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list4 = []
start = my_list3.index(3)
end = my_list3.index(9)
for i in my_list3[start:end]:
       my_list4.append(i)
print(f"通过for循环，从列表：{my_list3}中取出偶数，组成新的列表：{my_list4}")
for i in my_list3:
    if i%2 == 0:
       my_list4.append(i)
print(f"通过for循环，从列表：{my_list3}中取出偶数，组成新的列表：{my_list4}")
# i = 0
# while i < len(my_list3):
#     element = my_list3[i]
#     i += 1
#     if element%2 == 0:
#         print(element)

