"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
d= {key1 : value1, key2 : value2, key3 : value3 }
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。
"""

dict1 = {}
dict1["one"] = "1 - python教程"
dict1[2] = "2 - php教程"
print(dict1)
tinydict = {"name": "dyf", "code": 1, "site": "www.dyf.com"}
print("输出键为 'one' 的值", dict1["one"])
print("输出键为 2 的值", dict1[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
d11 = dict([("a", 1), ("b", 2), ("c", 3)])
print(d11)
d13 = dict(a=1, b=2, c=3)
print(d13)
# 访问字典里的值
print(d11["a"])  # {x: x**2 for x in (2, 4, 6)} 该代码使用的是字典推导式
# 修改自定里的值
d11["a"] = 100
print("修改d11中key为a的值：", d11)
d12 = {x: x**2 for x in (2, 4, 6)}
print(d12)
# 字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。
"""
1、 字典是一种映射类型，它的元素是键值对；
2、 字典的关键字必须为不可变类型，且不能重复；
3、 创建空字典使用{}
"""

print("=" * 20)
# 使用大括号 {} 来创建空字典
emptyDict = {}
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))


"""  
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""
tinydict = {
     'Name': 'Caiyuan', 'Age': 7, 'Name': '小菜猿'}
print ("tinydict['Name']: ", tinydict['Name'])

r"""  
字典内置函数&方法
序号	函数及描述	实例
1	len(dict)
计算字典元素个数，即键的总数。	>>> tinydict = {‘Name’: ‘Caiyuan’, ‘Age’: 4, ‘Class’: ‘First’}
>>> len(tinydict)
3
2	str(dict)
输出字典，可以打印的字符串表示。	>>> tinydict = {‘Name’: ‘Caiyuan’, ‘Age’:4, ‘Class’: ‘First’}
>>> str(tinydict)
“{‘Name’: ‘Caiyuan’, ‘Class’: ‘First’, ‘Age’: 4}”
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	>>> tinydict = {‘Name’: ‘Caiyuan’, ‘Age’: 4, ‘Class’: ‘First’}
>>> type(tinydict)
<class ‘dict’>
"""
print("=" * 20)
print(len(tinydict))
print(str(tinydict))
print(type(tinydict))
