
"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
内置的type() 函数可以用来查询变量所指的对象类型。
"""
x, y, z, m = 1213, 1213.10, True, 1213 + 10j
print(x)
print(y)
print(z)
print(m)
print(type(x))
print(type(y))
print(type(z))
print(type(m))

# 使用isinstance()函数判断变量是否是某种类型
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(z, bool))
print(isinstance(m, complex))
print("=================")

"""
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""


class A:
    pass


class B(A):
    pass


b = B()
print(type(b))
print(isinstance(b, A))
print(isinstance(b, B))
print("=================")

# 注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True1、False0 会返回 True，但可以通过 is 来判断类型。
# 在Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
print(isinstance(True, int))
print(isinstance(False, int))
print(issubclass(bool, int))
print("=================")

# 使用del语句删除一些对象引用
del x
# print(x)

# 数值运算
x = 2
y = 5
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x / y = ", x / y)
print("x // y = ", x // y)
print("y // x = ", y // x)
print("x ** y = ", x**y)
print("x % y = ", x % y)
print("x + y / x = ", x + y / x)
print("=================")

"""
1、 Python可以同时为多个变量赋值，如a,b=1,2；
2、 一个变量可以通过赋值指向不同类型的对象；
3、 数值的除法包含两个运算符：/返回一个浮点数，//返回一个整数；
4、 在混合计算时，Python会把整型转换成为浮点数；
"""