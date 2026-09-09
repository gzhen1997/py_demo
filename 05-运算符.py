"""
什么是运算符？
本章节主要说明 Python 的运算符。
举个简单的例子:
4 + 5 = 9
例子中，4 和 5 被称为操作数，+ 称为运算符。

Python 语言支持以下类型的运算符:
1. 算术运算符
2. 比较（关系）运算符
3. 赋值运算符
4. 逻辑运算符
5. 位运算符
6. 成员运算符
7. 身份运算符
"""

""" 
1. 算术运算符
+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 向下取接近商的整数	>>> 9//2
"""
from ast import If


a = 9
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a**b)
print(a // b)
print("-----------------")

""" 
2. 比较（关系）运算符
>	大于 - 返回x是否大于y	x > y 输出结果 True
<	小于 - 返回x是否小于y	x < y 输出结果 False
>=	大于等于 - 返回x是否大于等于y	x >= y 输出结果 True
<=	小于等于 - 返回x是否小于等于y	x <= y 输出结果 True
==	等于 - 返回x是否等于y	x == y 输出结果 True
!=	不等于 - 返回x是否不等于y	x != y 输出结果 False
"""
a = 9
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print("-----------------")


""" 
3. 赋值运算符
=	赋值 - 将y赋值给x	xx = y 输出结果 2
+=	加法赋值 - 将y加到x	x += y 输出结果 4
-=	减法赋值 - 将y减去x	x -= y 输出结果 0
*=	乘法赋值 - 将y乘以x	x *= y 输出结果 10
/=	除法赋值 - 将y除以x	x /= y 输出结果 2.5
%=	取模赋值 - 将y取模x	x %= y 输出结果 1
**	幂赋值 - 将y的x次幂赋值给x	x **= y 输出结果 100
//=	取整除赋值 - 将y取整除x	x //= y 输出结果 4
:= 海象运算符，可在表达式内部为变量赋值。Python3.8 版本新增运算符。
这个示例中，赋值表达式可以避免调用 len() 两次:
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
"""
x = 5
y = 0
y += x
print(y)
y = 100
y -= x
print(y)
y = 100
y *= x
print(y)
y = 100
y /= x
print(y)
y = 100
y %= x
print(y)
y = 2
y **= x
print(y)
y = 100
y //= x
print(y)

# 海象运算符
a = [1, 2, 3]
if (n := len(a)) > 2:
    print(f"List is too long ({n} elements, expected <= 2)")
print("-----------------")

"""  
4. 逻辑运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：

下表中变量 a 为 60，b 为 13二进制格式如下：
a= 0011 1100
b= 0000 1101

&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
或	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a 或 b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>“左边的运算数的各二进位全部右移若干位，”>>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
"""
a = 60
b = 13
w1 = a & b
print(w1)
w2 = a | b
print(w2)
w3 = a ^ b
print(w3)
w4 = ~a
print(w4)
w5 = a << 2
print(w5)
w6 = a >> 2
print(w6)
print("-----------------")

"""  
5. 逻辑运算符
and	与 - 返回x和y是否都为True	x and y 输出结果 True
or	或 - 返回x或y是否为True	x or y 输出结果 True
not	非 - 返回x的逻辑反	(not x) 输出结果 False
"""
a = 10
b = 20
if a and b:
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")
if a or b:
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")
print("-----------------")
# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")
if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")
print("-----------------")

"""  
成员运算符
in	成员运算符 - 检查一个元素是否在另一个元素中	x in y 输出结果 True
not in	成员运算符 - 检查一个元素是否不在另一个元素中	x not in y 输出结果 False
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5]
if a in list:
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")
if b not in list:
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")
# 修改变量 a 的值
a = 2
if a in list:
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")
print("-----------------")

"""   
身份运算符
is	身份运算符 - 检查两个变量是否引用同一个对象	x is y 输出结果 True
is not	身份运算符 - 检查两个变量是否引用不同的对象	x is not y 输出结果 False
"""
a = 20
b = 20
if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")
if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")
# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")
if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
print("-----------------")
# id()函数表示内存中对象的唯一标识
print(id(a))
print(id(b))

"""  
运算符优先级
运算符	描述
(expressions…),
[expressions…], {key: value…}, {expressions…}	圆括号的表达式
x[index], x[index:index], x(arguments…), x.attribute	读取，切片，调用，属性引用
await x	await 表达式
**	乘方(指数)
+x, -x, ~x	正，负，按位非 NOT
*, @, /, //, %	乘，矩阵乘，除，整除，取余
+, -	加和减
<<, >>	移位
&	按位与 AND
^	按位异或 XOR
或	按位或 OR
in,not in, is,is not, <, <=, >, >=, !=, ==	比较运算，包括成员检测和标识号检测
not x	逻辑非 NOT
and	逻辑与 AND
or	逻辑或 OR
if – else	条件表达式
lambda	lambda 表达式
:=	赋值表达式
"""

a = 20
b = 10
c = 15
d = 5
e = 0
e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)
e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)
e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)
e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)


# and拥有更高优先级:
x = True
y = False
z = False
if x or y and z:
    print("yes")
else:
    print("no")