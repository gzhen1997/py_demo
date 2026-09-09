"""
循环语句
Python 中的循环语句有 for 和 while。
"""



# while 循环
i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()
print("================")

# 无限循环
# var = 1
var = 2
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)
print("Good bye!")

# while 循环使用 else 语句
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    # 循环正常结束，没有异常发生，如果循环被 break 语句中断，else 子句不会执行
    print(count, " 大于或等于 5")

"""  
简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

#!/usr/bin/python
flag = 1
while (flag): print ('欢迎访问三只小菜猿!')
print ("Good bye!")
"""


# for 语句
sites = ["Baidu", "Google", "Caiyuan", "Taobao"]
for site in sites:
    if site == "Caiyuan":
        print("三只小菜猿!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


# range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(3):
    print(i)
print("=" * 20)
# 你也可以使用range指定区间的值：
for i in range(5, 9):
    print(i)
print("=" * 20)   
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做’步长’):
for i in range(5, 10, 2):
    print(i)
print("=" * 20)
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做’步长’):
for i in range(-10, -100, -30) :
    print(i)
print("=" * 20)
for i in range(-100, -10, 30) :
    print(i)
print("=" * 20)
a = ['Google', 'Baidu', 'Caiyuan', 'Taobao', 'QQ']
for i in range(len(a)) :
    print(a[i])
print("=" * 20)

# 还可以使用range()函数来创建一个列表：
print(list(range(10)))
print("=" * 20)


# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')
print("=" * 20)
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
print("=" * 20)

# pass 语句 Python pass是空语句，是为了保持程序结构的完整性。
# pass 语句可以用来占位，或者作为临时占位符。
# 最小的类:
class MyEmptyClass:
    pass

for letter in 'Caiyuan': 
   if letter == 'a':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
print ("Good bye!")
print("=" * 20)