"""
面向对象
Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。
如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，
这样有助于你更容易的学习Python的面向对象编程。
接下来我们先来简单的了解下面向对象的一些基本特征。
面向对象技术简介

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
     例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
"""

"""  
类定义
语法格式如下：
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""


class Animal:
    msg = "这是一个Animal类"
    """  
    动物类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.msg + "，我的名称是：" + self.name + "，我年龄是：" + str(self.age)


"""  
类对象
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:
"""
x = Animal("长颈鹿", 10)
print(str(x))
print(x.msg)
print(x.name)
print(x.age)

"""  
类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
def __init__(self, name, age):
        self.name = name
        self.age = age
类定义了 init() 方法，类的实例化操作会自动调用 init() 方法。如下实例化类 MyClass，对应的 init() 方法就会被调用:
Animal("长颈鹿", 10)
"""


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __repr__(self) -> str:
        return f"Complex({self.real}, {self.imag})"


x = Complex(3.4, 5.6)
print(x)
print(repr(x))
print("-----------------")

"""  
self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
"""


class Test:
    def prt(self, name):
        print(self)
        print(self.__class__)


t = Test()
print(t)
# t.prt()
t.prt("caiyuan")
print("-----------------")


"""  
注意：
self 不是 python 关键字，我们把他换成 caiyuan也是可以正常执行的:
"""


class Test:
    def prt(caiyuan):
        print(caiyuan)
        print(caiyuan.__class__)


t = Test()
print(t)
t.prt()


"""  
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
"""


class People:
    age = 0
    name = ""
    weight = 0
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__weight = weight

    def speak(self):
        # x = "%s 说我%s岁了体重是%s" % (self.name, self.age, self.__weight)
        x = f"{self.name}说我{self.age}岁了体重是{self.weight}KG"
        print(x)


people = People("caiyuan", 18, 70)
people.speak()

"""  
继承
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
class DerivedClassName(modname.BaseClassName):
"""


class Student(People):
    grade = 0

    def __init__(self, name, age, weight, grade):
        # super().__init__(name, age, weight)
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print(
            f"{self.name} 说 {self.age} 岁了体重是 {self.weight}KG，成绩是 {self.grade}分"
        )


s = Student("caiyuan", 18, 70, 90)
s.speak()


"""  
多继承
Python同样有限的支持多继承形式。多继承的类定义形如下例:
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
"""


class people:
    #    定义基本属性
    name = ""
    age = 0
    #    定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    #    定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ""

    def __init__(self, n, a, w, g):
        #    调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    #    覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker:
    topic = ""
    name = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ""

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法


"""  
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
"""


class Parent:  # 定义父类
    def myMethod(self):
        print("调用父类方法")


class Child(Parent):  # 定义子类
    def myMethod(self):
        print("调用子类方法")


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
# super() 函数是用于调用父类(超类)的一个方法。
super(Child, c).myMethod()  # 对象调用父对象调用父类已被覆盖的方法
print("-----------------")
"""  
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
"""


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


j = JustCounter()
j.count()
# 不能直接访问私有属性
# print(j.__secretCount)
print(j.publicCount)
print("-----------------")


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print("name  : ", self.name)
        print("url : ", self.__url)

    def __foo(self):  # 私有方法
        print("这是私有方法")

    def foo(self):  # 公共方法
        print("这是公共方法")
        self.__foo()


x = Site("菜猿", "www.dyf.com")
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错


"""  
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
"""

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(5,-2)
print (v1 + v2 + v3)
