"""
错误和异常
作为Python 初学者，在刚学习 Python 编程时，经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
Python 有两种错误很容易辨认：语法错误和异常。
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
"""

# 语法错误 缺少冒号
# while True print('Hello world')

#  0 不能作为除数，触发异常  ZeroDivisionError
# 10 * (1/0)
#  int 不能与 str 相加，触发异常  TypeError
# '2' + 2
# spam 未定义，触发异常  NameError
# 4 + spam*3


"""  
异常处理
try/except
异常捕捉可以使用 try/except 语句。
try语句按照如下方式工作；
首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
如果没有异常发生，忽略 except 子句，try 子句执行后结束。
如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
一个try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
"""

try:
    10 * (1 / 0)
except ZeroDivisionError:
    print("除数不能为 0")
except TypeError:
    print("类型错误")
except NameError:
    print("变量未定义")

"""  
try/except…else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
else 子句将在 try 子句没有发生任何异常的时候执行。
"""
try:
    10 * (1 * 20)
except ZeroDivisionError:
    print("除数不能为 0")
except TypeError:
    print("类型错误")
except NameError:
    print("变量未定义")
else:
    print("没有异常发生，else 子句不会执行")
print("================")


"""  
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
"""

try:
    10 * (1 * 20)
except ZeroDivisionError:
    print("除数不能为 0")
except TypeError:
    print("类型错误")
except NameError:
    print("变量未定义")
else:
    print("没有异常发生，else 子句不会执行")
finally:
    print("finally 子句会执行")


"""  
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
raise语法格式如下：
raise [Exception [, args [, traceback]]]
"""
x = 10
if x > 5:
    # raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
    pass

"""  
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
"""
try:
    raise NameError("HiThere")  # 模拟一个异常。
except Exception:
    print("An exception flew by!")
    # raise
    pass

"""  
用户自定义异常
你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承
"""


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print("My exception occurred, value:", e.value)

"""  
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。
"""


"""  
定义清理行为
finally 子句
finally 子句无论是否发生异常都将执行最后的代码。
如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。
"""
try:
    raise KeyboardInterrupt
except:
    pass    
finally:
    print("Goodbye, world!")


"""  
预定义的清理行为
一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
for line in open("myfile.txt"):
    print(line, end="")
以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
关键词with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
"""    
