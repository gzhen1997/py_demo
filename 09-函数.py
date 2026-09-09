"""
函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：
1. 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
2. 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
3. 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4. 函数内容以冒号 : 起始，并且缩进。
5. return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
"""


def max(a, b):
    if a > b:
        return a
    else:
        return b


print(max(1, 2))


"""  
语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
函数体
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
"""


def hello():
    print("Hello World!")


hello()


"""  
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
如下实例调用了 printme() 函数：
"""


def printme(str):
    #    打印任何传入的字符串
    print(str)
    return


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


"""  
参数传递
在python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：
a=[1,2,3]
a=“Caiyuan”
以上代码中，[1,2,3] 是 List 类型，“Caiyuan” 是 String 类型，而变量 a 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
可更改(mutable)与不可更改(immutable)对象
在python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，
则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


# python 传不可变对象实例
def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)


# 传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)
print("=" * 20)

"""  
参数
以下是调用函数时可使用的正式参数类型：
1. 必需参数
2. 关键字参数
3. 默认参数
4. 不定长参数
"""


# 必需参数
# 须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
def test(a, b):
    print(a)
    print(b)


test(1, 2)
test(2, 1)
# 错误：test(1)
print("=" * 20)


# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def test(a, b):
    print(a)
    print(b)


test(b=2, a=1)
test(a=1, b=2)
test(1, 2)
# 错误：test(1, 2, 3)
print("=" * 20)


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
def test(name, age=18):
    print(name, age)


test("张三")
test("李四", 20)
print("=" * 20)


# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
def test(*args):
    print(args)


def test2(*args, **kwargs):
    print(args)
    print(kwargs)


# test(1, 2, 3, 4, 5)
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
test2(
    1,
    2,
    3,
    4,
    5,
    a=1,
    b=2,
    c=3,
)
print("=" * 20)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)
print("=" * 20)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)
print("=" * 20)


# 加了两个星号 ** 的参数会以字典的形式导入
def test(*args, **kwargs):
    print(args)
    print(kwargs)


test(1, 2, 3, a=1, b=2, c=3)
print("=" * 20)


# 声明函数时，参数中星号 * 可以单独出现
def f(a, b, *, c):
    return a + b + c


# 报错
# f(1,2,3)
# *号后面的参数必须用关键字参数传入
f(1, 2, c=3)
print("=" * 20)

"""  
匿名函数
Python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,…argn]]:expression
"""
x = lambda a, b: a + b
y = lambda a, b, c: a * b % c
print(x(1, 2))
print(y(2, 5, 3))
print("=" * 20)


"""  
return 语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的 return 语句返回 None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：
"""


def sum(arg1, arg2):
    #    返回2个参数的和
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)
print("=" * 20)


# 强制位置参数 / 关键字前面的参数必须使用位置参数
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)
# b 不能使用关键字参数的形式
# f(10, b=20, c=30, d=40, e=50, f=60)
f(10, 20, 30, 40, e=50, f=60)
