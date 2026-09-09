import keyword
import sys

print(keyword.kwlist)
print(keyword.kwlist.__len__())

print("hello world")

# 单行注释
'''
多行注释
'''
"""
多行注释
"""

flag = False
# 行与缩进
if flag:
    print("It's true")
    print("It's false")
else:
    print("It's false")

"""
数值类型：
   - 整数 int
   - 浮点数 float
   - 复数 complex
   - 布尔 bool
字符串：
python中使用  ' 或者 " 使用完全相同
转义符： \ 反斜杠    使用r可以使反斜杠不再转移 r"It is a line with \n"   
python中字符串的索引有两种方式，方式一：从左往右以0开始，方式二：从右往左以-1开始
python中的字符串不能改变
python中没有单独的字符，一个字符就是一个字符串
字符串的截取方式   格式：字符串[开始索引:结束索引:步长]
"""
content = "helloworld"
print("第一个字符为：", content[0])
print("最后一个字符为：", content[-1])
print("截取第一个字符到第五个字符为：", content[0:5])
print("截取第一个字符到第五个字符的偶数字符为：", content[0:5:2])
print("反转后的字符串为：", content[::-1])
print("截取第一个字符到倒数第二个字符为：", content[0:-1])
print("输出字符串两次为：", content * 2)
print("拼接字符串：" + "hello" + "world")
print("反斜杠转义为：", "hello\ndyfn")
print("禁止反斜杠转义为：", r"hello\ndyfn")


# 等待用户输入
# input("\n按下 enter 键后退出。")


# 同一行显示多条语句
a=10;b=20;c=a+b;
print(c)

x = 'hello world';sys.stdout.write(x)

# print打印默认换行，如果不进行换行需要添加end函数
print("hello world", end="")
print("hello world", end="")
print("")
# import与 from ... import 区别
'''
import 会导入整个模块，而 from ... import 会导入指定的函数或类
整个模块导入 import somemodule
导入该模块下指定方法 from somemodule import somefunction
'''
from sys import path
print("path:", path)

print("====================")
args = sys.argv

for arg in args:
    print(arg)