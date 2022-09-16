"""
演示对文件的读取
"""

# 打开文件
import time

# f = open("E:/Python/测试.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read读取全部字节的结果：{f.read()}")
print("--------------------------------")
# 读取文件 - readlines()
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容的：{lines}")
# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的数据是：{line1}")
# print(f"第二行的数据是：{line2}")
# print(f"第三行的数据是：{line3}")
# for循环读取文件行
# i = 0
# for line in f:
#     i += 1
#     print(f"第{i}行数据是：{line}")
# # 文件的关闭
# time.sleep(5)
# f.close()
# with open 语法操作文件  操作完会自动关闭文件
# with open("E:/Python/测试.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         i += 1
#         print(f"第{i}行数据是：{line}")


"""
演示读取文件，课后练习题
"""

# 打开文件，以读取模式打开
# f = open("E:/python/测试.txt", "r", encoding="UTF-8")
# 方式1：读取全部内容，通过字符串count方法统计itheima 单词数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima在文件中出现了：{count}次")
# 方式2：读取内容，一行一行读取
# count = 0
# for line in f:
#     line = line.strip()  # 去除开题和结尾的空格以及换行符
#     words = line.split(" ")
#     for word in words:
#         if word == "itheima":
#             count += 1  # 如果单词是itheima,进行数量的累加加1
# 判断单词出现次数并累计
# print(f"itheima出现的次数是：{count}")

# 关闭文件
# f.close()


"""
演示文件的写入
"""

# 打开文件，不存在的文件
import time

# f = open("D:/test.txt", "w", encoding="UTF-8")
# # write写入
# f.write("hello world!!!")  # 将内容写入到内存中
# # flush刷新
# f.flush()   # 将内存中积攒的内容写入到硬盘文件中
# time.sleep(20)
# # close关闭
# f.close()   # 内置了flush的功能的
# 打开一个存在的文件
# f = open("D:/test.txt", "w", encoding="UTF-8")
# # write写入，flush刷新
# f.write("张瀚")
# # close关闭
# f.close()

# 打开一个存在的文件
# f = open("D:/test.txt", "a", encoding="UTF-8")
# # write写入，flush刷新
# f.write("\n月薪过万")
# # close关闭
# f.close()


fr = open("D:/test.txt", "r", encoding="UTF-8")
fw = open("D:/test.txt.bak", "w", encoding="UTF-8")

for line in fr:
    line = line.strip()
    # line = line.split(",")
    # print(line)
    if line.split("，")[3] == "消费":
        continue   # continue进入下一次循环，这一次后面的内容就跳过了
    # 将内容写出去
    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()    # 写出文件调用close()会自动flush()