"""
演示变量的类型注释
"""
import json
import random

# 基础数据类型注释
var_1: int = 18
var_2: str = "zhanghan"
var_3: bool = True


# 类对象类型注释
class Student:
    pass


stu: Student = Student()
# 基础容器类型注释
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"zhanghan": 666}
# 容器类型详细注释
my_list1: list[int] = [1, 2, 3]
my_tuple2: tuple[int, str, bool] = (1, "zhanghan", True)
my_dict3: dict[str, int] = {"zhanghan": 666}
# 在注释中进行类型注释
var_4 = random.randint(1, 10)  # type: int
var_5 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]


def func():
    return 10


var_6 = func()  # type: int
# 类型注释的限制

"""
演示对函数（方法）进行类型注释
"""


# 对形参进行类型注释
def add(x: int, y: int):
    return x + y


# 对返回值进行类型注释
def func(data: list) -> list:
    return data


print(func(1))

"""
演示Union联合型注释
"""

# 使用Union类型，必须先导包
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func()
