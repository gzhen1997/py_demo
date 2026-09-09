"""
操作系统接口
os模块提供了不少与操作系统相关联的函数。
"""

import os
from sqlite3 import Time

print("当前工作目录:", os.getcwd())  # 返回当前的工作目录
# os.chdir('test')  # 切换到指定目录
print("切换到 test 目录后:", os.getcwd())  # 返回当前的工作目录
# os.system('mkdir today')  # 创建目录
print("-----------------")


"""  
建议使用 “import os” 风格而非 “from os import *”。这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。
在使用os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:

"""
# dir(os) # 查看 os 模块的所有函数
# help(os) # 查看 os 模块的详细文档
print("-----------------")


# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:

import shutil

print(dir(shutil))
print("-----------------")
# shutil.copy('test/test.txt', 'test/test_copy.txt')  # 复制文件
# shutil.move('test/test_copy.txt', 'test/test_move.txt')  # 移动文件

# 删除目录  不会判断目录是否为空目录
# shutil.rmtree('test/today')  # 删除目录

# 删除文件
# if os.path.exists("test/test_move.txt"):
#     os.remove("test/test_move.txt")

# 打包文件
# shutil.make_archive('test', 'zip', 'test')  # 打包 test 目录下的所有文件
# shutil.make_archive('test', 'tar', 'test')  # 打包 test 目录下的所有文件，根目录为 test
# shutil.make_archive('test', 'gztar', 'test')  # 打包 test 目录下的所有文件，根目录为 test，压缩格式为 tar.gz

# shutil.unpack_archive('test.zip', 'test2')  # 解压 test.zip 文件到 test2 目录

"""  
文件通配符
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
"""
import glob

print(glob.glob("test/*.txt"))  # 返回 test 目录下所有 .txt 文件的列表

"""  
命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 “python demo.py one two three” 后可以得到以下输出结果:
"""
import sys

print(sys.argv)  # ['demo.py', 'one', 'two', 'three']
print("-----------------")


"""     
错误输出重定向和程序终止
sys还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
"""
sys.stderr.write("Warning, log file not found starting a new one\n")
# sys.exit(1)  # 退出程序，返回 1 表示错误
print("-----------------")


"""  
字符串正则匹配
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案
"""
import re

print(re.findall(r"\d+", "a1b2c3d"))  # ['1', '2', '3']
print(dir(re))
print("-----------------")

m = re.search(r"(\d+)-(\d+)", "日期 2026-0908 号")
print(m.group())  # '2026-0908'（整个匹配）
print(m.group(1))  # '2026'（第 1 个括号分组）
print(m.group(2))  # '0908'（第 2 个分组）
print(m.start())  # 3（匹配起点下标）
print(m.end())  # 12（匹配终点下标）
print(m.span())  # (3, 12)

print("-----------------")
# 转义特殊符号
print(re.escape("a.b*c"))  # 'a\\.b\\*c'
pat = re.compile(r"\d{3,4}-\d{7,8}")  # 预编译一次
print(pat.findall("tel:010-12345678, 021-87654321"))  # ['010-12345678', '021-87654321']
# 分割字符串
print(re.split(r"[,\s]+", "apple, banana  cherry"))  # ['apple', 'banana', 'cherry']
# s1 = "hello,world"
# print(s1.split(","))

# 替换字符串
print(re.sub(r"\d+", "X", "a1b2c3d"))  # 'aXbXcX'
print(re.sub(r"\d", "X", "a1b2c3d"))  # 'aXbXcX'
print(re.subn(r"\d", "X", "a1b2c3d"))  # ('aXbXcX', 3) （多一个替换次数）
print(re.sub(r"\d", lambda x: x.group() * 2, "a1b2c3d"))  # 'a2b4c6d'
print(re.sub(r"\d", lambda x: x.group() * 2, "a1b2c3d", count=2))  # 'a2b4c3d'

log = "err 12 ok 34 err 56"

print(re.search(r"err \d+", log))  # 第一个匹配 → Match('err 12')；找不到返回 None
print(re.findall(r"err \d+", log))  # 所有匹配 → ['err 12', 'err 56']
print("-----------------")
re.match(r"he", "hello 2026")  # Match，匹配到 'he'（开头）
re.match(r"20", "hello 2026")  # None，开头不是 20
re.fullmatch(r"hello 2026", "hello 2026")  # Match，整个串都匹配
re.fullmatch(r"he", "hello 2026")  # None，只匹配开头一部分不算 fullmatch
print("-----------------")


# 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
print("tea for too".replace("too", "two"))  # 'tea for two'
print("-----------------")


"""  
数学
math模块为浮点运算提供了对底层C函数库的访问:
"""
import math

print(math.sqrt(9))  # 3.0
print(math.pow(2, 3))  # 8.0
print(math.log(10))  # 2.302585092994046
print(math.pi)  # 3.141592653589793
print("-----------------")


# 随机数
import random

print(random.randint(1, 10))  # 1 到 10 之间的随机整数
print(random.uniform(1, 10))  # 1 到 10 之间的随机浮点数
print(random.choice(["a", "b", "c"]))  # 随机选择一个元素
print(random.sample(range(100), 10))  # 随机选择 10 个不同的元素
s1 = [1, 5, 6, 10, 3]
print(s1)
# 随机打乱列表
random.shuffle(s1)
print(s1)

# 随机生成指定范围的随机数
print(random.randrange(100))  # 0 到 99 之间的随机整数
print(random.randrange(100, 200))  # 100 到 199 之间的随机整数
print("-----------------")

"""  
访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
"""
import urllib.request
import smtplib
from urllib.request import urlopen

with urllib.request.urlopen("http://www.baidu.com") as response:
    for line in response:
        line = line.decode("utf-8")  # Decoding the binary data to text.
        print(line)

# server = smtplib.SMTP("localhost")
# server.sendmail(
#     "sooth@example.org",
#     "jcae@example.org",
#     """To: jcae@example.org
#  From: sooth@example.org

#  Beware the Ides of March.
# """,
# )
# server.quit()

"""  
日期和时间
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理:
"""
from datetime import datetime, date

print(date.today())
print("-----------------")

currentTime = datetime.now()
print(currentTime.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
print(currentTime.strftime("%Y-%m-%d %H:%M:%S"))
print(date(2023, 2, 3))
print("-----------------")


"""  
数据压缩
以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
"""
import zlib

# b 表示二进制数据  如果s中存在中文必须先进行 encode("utf-8")
s = b"witch which has which witches wrist watch"
print(type(s))
print("原始数据:", s)
print("原始数据长度:", len(s))
compressed = zlib.compress(s)
print("压缩数据:", compressed)
print("压缩数据长度:", len(compressed))
print("解压数据:", zlib.decompress(compressed))
print("解压数据长度:", len(zlib.decompress(compressed)))
print("-----------------")


"""  
性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
"""
from timeit import Timer

# 测试不同方法的性能
print(Timer(lambda: "a" * 100).timeit())
print(Timer(lambda: "a" * 100).timeit())


def t1(a):
    print("t1")
    return int(a) * 100


def t2(a):
    return int(a) * 1000


print("-----------------")
# print(Timer(lambda: t1(10)).timeit())
# print(Timer(lambda: t2(10)).timeit())
print(Timer("a=a+b;lambda a: t1(a)", "a=1; b=2").repeat(repeat=5, number=10000))
print(Timer("t=a+b;lambda a: t2(a)", "a=1; b=2").repeat(repeat=5, number=10000))


"""  
测试模块
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
"""


def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()  #  自动验证嵌入测试?
# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:

import unittest


class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


# unittest.main()  # Calling from the command line invokes all tests


os.chdir("../")
print(os.getcwd())
shutil.make_archive("py_demo", "zip", "py_demo")
