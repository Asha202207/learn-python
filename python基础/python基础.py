print("Hello World!!!")
# 我是单行注释
"""
我是多行注释
  张瀚
  19970421
"""
"""
演示Python中变量的相关操作
"""

# 定义一个变量，用来记录钱包余额
money = 50
# 通过print语句，输出变量记录的内容
print("钱包还有：",money)

# 买了一个冰激凌，花费10元
money = money - 10
print("买了冰激凌花费10元，还剩余：",money,"元")

# 假设，每隔一小时，输出一下钱包的余额
print("现在是下午1点，钱包余额剩余：",40)
print("现在是下午2点，钱包余额剩余：",40)
print("现在是下午3点，钱包余额剩余：",money)
print("现在是下午4点，钱包余额剩余：",money)

# 数据类型 type(变量)可以输出类型，这是查看数据类型
# 方式1：使用print直接输出类型信息
print(type("张瀚"))
print(type(666))
print(type(11.345))
# 方式2：使用变量存储type()语句结果
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)
# 方式3：使用type()语句，查看变量中存储的数据类型信息
name = "张瀚"
name_type =type(name)
print(name_type)


"""
数据类型转换
int(x)       将x转换为一个整数
float(x)     将x转换为一个浮点数
str(x)       将对象x转换为字符串
"""
# 将数字类型转换成字符串
num_str=str(11)
print(type(num_str),num_str)
float_str = str(11.345)
print(type(float_str),float_str)
# 将字符串转换成数字
num = int("11")
print(type(num),num)
num2 = float("11.345")
print(type(num2),num2)
# 错误提示，想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int("张瀚")
# print(type(num3),num3)

# 整数转浮点数
int_num = int(11.345)
print(type(int_num),int_num)

# 标识符
# 规则1：内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能以数字作为开头
# 1_name="张三"
# name_!="张三"   错误的代码示范
name_ = "张三"
_name = "张三"
name_1 = "张三"
# 规则2：大小写敏感
Itheima = "张瀚"
itheima = 666
print(Itheima)
print(itheima)
# 规则3：不可使用关键字
# 错误的示例，使用了关键字：class = 1
# 错误的示例，使用了关键字：def = 1
Class = 1

# 运算符
# 算术(数学)运算符
print("1+1=",1+1)  # 加法
print("2-1=",2-1)  # 减法
print("3*3=",3*3)  # 乘法
print("4/2=",4/2)  # 除法
print("11//2=",11//2) # 整除
print("9%2=",9%2)     # 取余
print("2**2=",2**2)   # 幂运算
# 赋值运算符
num = 1 + 2 * 3
# 复合赋值运算符
# +=
num = 1
num += 1 # num = num + 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 4
print("num *= 4:",num)
num /= 2
print("num /= 2:",num)
num = 3
num %= 2
print("num %= 2:",num)

num **= 2
print("num **= 2:",num)

num = 9
num //= 2
print("num //= 2:",num)

"""
字符串三种定义法：
单引号定义法
双引号定义法
三引号定义法
"""
# 单引号定义法
name = '张瀚'
print(type(name))
# 双引号定义法
name = "张瀚"
print(type(name))
# 三引号定义法，写法和多行注释是一样的
name = """
我是
张瀚
"""
print(type(name))
# 在字符串内，包含双引号
name = '"张瀚"'
print(name)
# 在字符串内，包含单引号
name = "'张瀚'"
print(name)
# 使用转义字符 \ 解除引号的效用
name = "\"张瀚\""
print(name)
name = '\'张瀚\''
print(name)
# 字符串字面量之间的拼接
print("学IT来黑马"+"月薪过万")
# 字符串字面量和字符串变量的拼接
name = "张瀚"
adress = "文萃路94号"
tel = "4484785"
print("我是：" + name + "，我的地址是：" + adress + "，我的电话是：" + tel) # 只能完成字符串的拼接，不能拼接字符串和其他类型
# 字符串格式化
# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num,avg_salary)
print(message)
# %s占位字符串 %d占位整数 %f占位浮点数
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s,成立于：%d,我今天的股价是：%f" % (name,setup_year,stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

"""
演示第二种字符串格式化的方式：f"{占位}"
"""
name = "传智教育"
set_up_year = 2006
stock_price = 19.99
# f:format
print(f"我是{name},我成立于：{set_up_year}年，我今天的股价是：{stock_price}")

"""
演示对表达式进行字符串格式化
"""
print("1*1的结果是：%d" % (1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type("字符串"))

name = "传智播客"
stock_price = 19.99
stock_code = "003032"
# 股票价格每日增长系数
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数：%.1f,经过%d天的增长后，股价达到了：%.2f" %(stock_price_daily_growth_factor,growth_days,finally_stock_price))

"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)

# 输入数字类型
num = input("请高速我你的银行卡密码：")
num = int(num)

print("你的银行卡密码的类型是：", type(num))
print("hello world")

"""
比较运算符
== 判断内容是否相等，满足为True，不满足为False
!= 判断内容是否不相等，满足为True，不满足为False
>  判断运算符左侧内容是否大于右侧，满足为True，不满足为False
<  判断运算符左侧内容是否小于于右侧，满足为True，不满足为False
>= 判断运算符左侧内容是否大于等于右侧，满足为True，不满足为False
<= 判断运算符左侧内容是否小于等于右侧，满足为True，不满足为False
"""
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")
num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")
name1 = "itcuihua"
name2 = "itzhanghan"
print(f"itcuihua == itzhanghan的结果是：{name1 == name2}")

"""
演示布尔类型的定义
以及比较运算符的应用
"""
# 定义变量储存布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool变量的内容是：{bool_2},类型是：{type(bool_2)}")