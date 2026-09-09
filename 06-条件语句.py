"""
条件控制
Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
"""

from itertools import count


x = 1

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
else:
    print("x is other")
""" 
注意：
1、 每个条件后面要使用冒号:，表示接下来是满足条件后要执行的语句块；
2、 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块；
3、 在Python中没有switch…case语句，但在Python3.10版本添加了match…case，功能也类似，详见match语句。
"""
sum = 0
counter = ""
while x < 10:
    if x % 2 == 1:
        sum += x
        counter += str(x) + " + "
    x += 1
    if x == 10 and len(counter) > 0:
        counter = counter[0:-3]
        
print(sum)
print(f"{counter} = {sum}")
print("=================")


# x = int(input("请输入一个整数："))

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


"""  
操作符	描述
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较两个值是否相等
!=	不等于
"""

# if 嵌套
# 在嵌套if 语句中，可以把 if…elif…else 结构放在另外一个 if…elif…else 结构中。
# num=int(input("输入一个数字："))
num=23
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

"""  
match…case
Python 3.10 增加了 match…case 的条件判断，不需要再使用一连串的 if-else 来判断了。
match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_ 可以匹配一切。
case _: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功。
"""

mystatus=400
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(mystatus))

# 一个case 也可以设置多个匹配条件，条件使用 ｜ 隔开，例如：
def match_type(type):
    match type:
        case "狗" | "猫":
            return "动物"
        case _:
            return "其他"
print(match_type("狗"))
print(match_type("猫"))
print(match_type("人"))