"""
输出格式美化
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
- `str(x)` 调用 `x.__str__()`；`repr(x)` 调用 `x.__repr__()`。
-  回退规则（单向）：类没定义 `__str__` 时，`str()` 会自动用 `__repr__`；
但只定义 `__str__`、没定义 `__repr__` 时，`repr()` 不会用它，而是显示 `<...object at 0x...>` 之类的默认值。
所以**建议优先实现 `__repr__`**，`str()` 通常就够用了。
"""

import datetime

a = 10
print(a)
print(str(a))
print(repr(a))
print("-----------------")
b = 0.1
print(b)
print(str(b))
print(repr(b))
print("-----------------")
c = datetime.datetime.now()
print(c)
print(str(c))
print(repr(c))
print("-----------------")

import test.a as a_module
import test.b as b_module

print(str(a_module))
# print(repr(a_module))
# print(str(b_module))
# print(repr(b_module))
print("-----------------")

"""  
注意：在第一个例子中, 每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
"""
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x).rjust(3))
print("-----------------")
for x in range(1, 11):
    # print("{0:<2d} {1:<3d} {2:<4d}".format(x, x * x, x * x * x))
    print(f"{x:<2d} {x*x:<3d} {x*x*x:<4d}")
print("-----------------")
# 宽度是**最小**宽度，超了不截断
print("{0:2d}".format(12345))
print("-----------------")

# 方法 zfill(), 它会在数字的左边填充 0
print("12345".zfill(10))
# 注意负数会保留在最左边
print("-3.14".zfill(7))

# str.format() 的基本使用如下:
print("Hello, {}!".format("World"))

# 在括号中的数字用于指向传入对象在 format() 中的位置
print("{0} 和 {1}".format("Google", "Baidu"))

# 如果在format() 中使用了关键字参数
print("{name}网址： {site}".format(name="三只小菜猿", site="www.dyf.com"))
d1 = dict([("name", "三只小菜猿"), ("site", "www.dyf.com")])
print("{name}网址： {site}".format(**d1))

# 位置及关键字参数可以任意的结合:
print("站点列表 {0}, {1}, 和 {other}。".format("Google", "Baidu", other="Taobao"))

print("-----------------")
# 在:后传入一个整数, 可以保证该域至少有这么多的宽度
print("{0:10}=>".format("Hello"))
# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值
table = {"Google": 1, "Baidu": 2, "Taobao": 3}
print("Baidu:{0[Baidu]:d};Google:{0[Google]:d};Taobao:{0[Taobao]:d}".format(table))
table = {"Google": 1, "Baidu": 2, "Taobao": 3}
print("Baidu:{Baidu:d};Google:{Google:d};Taobao:{Taobao:d}".format(**table))
print("{0}->{1}".format([1, 2], ["a", "b"]))
print("-----------------")
# 旧式字符串格式化
# %操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串
print("Hello, %s!" % "World")


# 读取键盘输入
# name = input("请输入您的姓名：")
name = "三只小菜猿"
print("您的姓名是：" + name)

"""  
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
filename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读®。
x   写模式，新建一个文件，如果该文件已存在则会报错。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

注意：r+ 不能创建文件文件如果文件不存在会报错
"""
# with open("test/test.txt", "w") as f:
#     f.write("Hello, World!")
# f.write()
# with open("test/test.txt", "a") as f:
#     f.write("Hello, World!\n")

"""
with expression和finally语句类似

f = open("test/test.txt", "r")
try:
    f.write("Hello, World!\n")
finally:
    f.close() 
"""


"""  
f.read()
为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
"""
with open("test/test.txt", "r") as f:
    content = f.read()
    print(content)
print("-----------------")
"""  
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 ‘\n’。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
"""
with open("test/test.txt", "r") as f:
    line = f.readline()
    print(line, end="")
print("-----------------")

with open("test/test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
print("-----------------")

# 另一种方式是迭代一个文件对象然后读取每行:
with open("test/test.txt", "r") as f:
    for line in f:
        print(line, end="")
print()
print("-----------------")

with open("test/foo.txt", "rb+") as f:
    f.write(b"0123456789abcdef")
    # 从文件的第6个字节开始读取1个字节
    print(f.seek(5))
    print(f.read(1))
    # 移动到文件的倒数第三字节
    print(f.seek(-3, 2))
    print(f.read(1))
print("-----------------")


"""  
pickle 模块
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
基本接口：
pickle.dump(obj, file, [,protocol])
有了pickle 这个对象, 就能对 file 以读取的形式打开:
x= pickle.load(file)
注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。
"""
import pickle

data1 = {"a": [1, 2.0, 3, 4 + 6j], "b": ("string", "Unicode string"), "c": None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('test/data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()


import pprint

#使用pickle模块从文件中重构python对象
pkl_file = open('test/data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()