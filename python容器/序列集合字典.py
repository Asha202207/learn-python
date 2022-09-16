"""
演示对序列进行切片操作
"""

# 对list进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]    # 步长默认是1，所以可以不写
print(f"结果1：{result1}")
# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # 起始和结束不写表示从头到尾，步长为1可以省略
print(f"结果2：{result2}")
# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果2：{result3}")
# 对str进行切片，从头开始，到最后结束，步长-1
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果2：{result4}")   # 等同于将序列反转了
# 对列表进行切片，从3开始，到1结束，步长-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"结果5：{result5}")
# 对元组进行切片，从头开始，到尾结束，步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果6：{result6}")


"""
练习案例：序列的切片实践
"""
str1 = "万过薪月，员序程马黑来，nohtyP学"
# 方式1
result1 = str1[9:4:-1]
print(result1)
# 方式2  倒叙字符，切片取出
result2 = str1[::-1][9:14]
print(result2)
# 方式3  split分割“，” replace替换来为空，倒叙字符
result3 = str1.split("，")[1].replace("来", "")[::-1]
print(result3)


"""
演示数据容器字典的定义
"""

# 定义字典
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# 定义空字典
my_dict2 = {}   # set()
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1},类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2},类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型：{type(my_dict3)}")
# 定义重复Key的字典
my_dict1 = {"王力宏": 99, "王力宏": 88, "林俊杰": 77}
print(f"重复key的字典内容是：{my_dict1}")
# 从字典中基于key获取Value
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
score = my_dict1["王力宏"]
print(f"王力宏的考试分数是：{score}")
score = my_dict1["周杰伦"]
print(f"周杰伦的考试分数是：{score}")
# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "周杰伦": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息：{stu_score_dict}")
# 从嵌套字典中获取数据
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文成绩是：{score}")
score = stu_score_dict["林俊杰"]["英语"]
print(f"林俊杰的英语成绩是：{score}")

"""
演示字典的常用操作
"""

# 新增元素
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")
# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新元素后，结果：{my_dict}")
# 删除元素 字典.pop(key)
score = my_dict.pop("周杰伦")
print(f"字典中被移除一个元素，结果：{my_dict},周杰伦的考试分数是：{score}")
# 清空元素  clear
my_dict.clear()
print(f"字典被清空了，内容是{my_dict}")
# 获取全部的key  字典.keys()
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")
# 遍历字典
# 方式1 通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")
# 字典不支持下标索引，不支持while循环
# 统计字典内的元素数量 len()函数
num = len(my_dict)
print(f"字典的元素数量有：{num}个")

"""
练习：升职加薪
"""
my_dict = {"王力宏": {
    "部门": "科技部",
    "工资": 3000,
    "级别": 1
}, "周杰伦": {
    "部门": "市场部",
    "工资": 5000,
    "级别": 2
}, "林俊杰": {
    "部门": "市场部",
    "工资": 7000,
    "级别": 3
}, "张学友": {
    "部门": "科技部",
    "工资": 4000,
    "级别": 1
}, "刘德华": {
    "部门": "市场部",
    "工资": 6000,
    "级别": 2
}, }
print(f"全体员工当前信息如下：{my_dict}")
for name in my_dict:
    # if条件判断符号条件员工
    if my_dict[name]["级别"] == 1:
        # 升职加薪操作
        # 获取到员工的信息
        employee_my_dict = my_dict[name]
        # 修改员工的信息字典
        employee_my_dict["级别"] = 2  # 级别+1
        employee_my_dict["工资"] += 1000  # 工资+1000
        # 将员工的信息更新回my_dict
        my_dict[name] = employee_my_dict

print(f"员工在升职加薪后的信息如下：{my_dict}")


"""
演示数据容器集合的使用
"""

# 定义集合
my_set = {"张瀚", "许雯霏", "python", "张瀚", "许雯霏", "python", "张瀚", "许雯霏", "python"}
my_set_empty = set()
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")  # 集合的特点是不允许重复，顺序不能保证
# 添加新元素 集合.add(元素)
my_set.add("C++")
print(f"my_set添加元素后，结果是：{my_set}")
# 移除元素  集合.renmve()
my_set.remove("python")
print(f"my_set移除python后，结果是：{my_set}")
# 随机取出一个元素   集合.pop()
my_set = {"张瀚", "许雯霏", "python"}
element = my_set.pop()  # 随机取，取哪个不能决定
print(f"集合被取出元素是：{element}，取出元素后：{my_set}")
# 清空集合 集合.clear()
my_set.clear()
print(f"集合被清空了，结果是：{my_set}")
# 去2个集合的差集
# 语法1：集合1.difference(集合2)  取集合1中集合2没有的元素
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是:{set3}")
print(f"取出差集后,原有set1的内容是:{set1}")
print(f"取出差集后,原有set2的内容是:{set2}")
# 语法2：集合1.difference_update(集合2)  对比集合1和集合2，在集合1内，删除和集合2相同的元素
set4 = set1.difference_update(set2)
print(f"消除差集后,原有set1的内容是:{set1}")
print(f"消除差集后,原有set2的内容是:{set2}")
# 2个集合合并成1个  集合1.union(集合2)  将集合1和集合2组成新集合
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set5 = set1.union(set2)
print(f"2集合合并结果：{set5}")
print(f"2集合合并后，集合1结果：{set1}")
print(f"2集合合并后，集合2结果：{set2}")
# 统计集合元素数量  len()
set1 = {1, 2, 3, 4, 5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")
# 集合的遍历
# 集合不支持下标索引，索引不能用while循环，但是可以用for循环
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合内的元素有：{element}")

"""
练习：信息去重
"""
my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]
my_set = set()
# 通过for循环遍历列表
for element in my_list:
    # 在for循环中将列表的元素添加至集合
    my_set.add(element)

# 最终得到元素去重后的集合对象，并打印输出
print(f"列表的内容是：{my_list}")
print(f"通过for循环后，得到的集合对象是：{my_set}")

"""
五类数据容器的总结
"""
"""
是否支持下标索引
   支持：列表、元组、字符串 - 序列类型
   不支持：集合、字典 - 非序列类型
是否支持重复元素
   支持：列表、元组、字符串 - 序列类型
   不支持：集合、字典 - 非序列类型
是否可以修改
   支持：列表、集合、字典
   不支持：元组、字符串
"""
"""
               列表          元组          字符串          集合          字典
元素数量      支持多个       支持多个       支持多个       支持多个       支持多个 
元素类型        任意          任意          仅字符          任意        key:value
                                                                    key:除字典外任意类型
                                                                    value:任意类型
下标索引        支持          支持          支持          不支持         不支持
重复元素        支持          支持          支持          不支持         不支持
可修改性        支持          不支持        不支持          支持          支持
数据有序         是            是            是             否            否
使用场景     可修改、可重    不可修改、可重   一串字符的   不可重复的数据   以key检索value
            复的一批数据    复的一批数据     记录场景     记录场景        的数据记录场景
            记录场景        记录场景
"""
"""
基于各类容器的特点，它们的应该场景如下：
列表：一批数据，可修改，可重复的储存场景
元组：一批数据，不可修改，可重复的储存场景
字符串：一串字符串的储存场景
集合：一批数据，去重储存场景
字典：一批数据，可用Key检索Value的储存场景
"""


"""
演示数据容器的通用功能
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, }

# len元素个数
print(f"列表 元素的个数有：{len(my_list)}")
print(f"元组 元素的个数有：{len(my_tuple)}")
print(f"字符串 元素的个数有：{len(my_str)}")
print(f"集合 元素的个数有：{len(my_set)}")
print(f"字典 元素的个数有：{len(my_dict)}")
# max最大元素
print(f"列表 最大的元素个数有：{max(my_list)}")
print(f"元组 最大的元素个数有：{max(my_tuple)}")
print(f"字符串最大的元素个数有：{max(my_str)}")
print(f"集合 最大的元素个数有：{max(my_set)}")
print(f"字典 最大的元素个数有：{max(my_dict)}")
# min最小元素
print(f"列表 最小的元素个数有：{min(my_list)}")
print(f"元组 最小的元素个数有：{min(my_tuple)}")
print(f"字符串最小的元素个数有：{min(my_str)}")
print(f"集合 最小的元素个数有：{min(my_set)}")
print(f"字典 最小的元素个数有：{min(my_dict)}")
# 类型转换：容器转列表
print(f"列表 转列表的结果是：{list(my_list)}")
print(f"元组 转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合 转列表的结果是：{list(my_set)}")
print(f"字典 转列表的结果是：{list(my_dict)}")
# 类型转换：容器转元组
print(f"列表 转元组的结果是：{tuple(my_list)}")
print(f"元组 转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合 转元组的结果是：{tuple(my_set)}")
print(f"字典 转元组的结果是：{tuple(my_dict)}")
# 类型转换：容器转字符串
print(f"列表 转字符串的结果是：{str(my_list)}")
print(f"元组 转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合 转字符串的结果是：{str(my_set)}")
print(f"字典 转字符串的结果是：{str(my_dict)}")
# 类型转换：容器转集合
print(f"列表 转集合的结果是：{set(my_list)}")
print(f"元组 转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是：{set(my_str)}")
print(f"集合 转集合的结果是：{set(my_set)}")
print(f"字典 转集合的结果是：{set(my_dict)}")
# 容器不能转字典  缺少键值对，反之字典可以转其他容器
# sorted排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5, }
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
# 反向排序 reverse
print(f"列表对象的排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象的排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的排序结果：{sorted(my_dict, reverse=True)}")


"""
演示字符串大小比较
"""

# abc 比较 abd
print(f"abd大于abc,结果：{'abd' > 'abc'}")
# a 比较 ab
print(f"ab大于a,结果：{'ab' > 'a'}")
# a 比较 A
print(f"a大于A,结果：{'a' > 'A'}")
# key1 比较 key2
print(f"key2大于key1,结果：{'key2' > 'key1'}")