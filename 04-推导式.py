"""
推导式
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
Python 支持各种数据结构的推导式：
列表(list)推导式
字典(dict)推导式
集合(set)推导式
元组(tuple)推导式
"""

# 列表推导式
"""
列表推导式格式为：
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]
或者
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。
过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
"""
names = ["Bob", "Tom", "alice", "Jerry", "Wendy", "Smith"]
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

# 计算30 以内可以被 3 整除的整数：
l1 = [n for n in range(1, 31) if n % 3 == 0]
print("30 以内可以被 3 整除的整数为：", l1)

# 字典推导式
"""
字典推导基本格式：
{ key_expr: value_expr for value in collection }
或 
{ key_expr: value_expr for value in collection if condition }
"""

# 使用字符串及其长度创建字典：
listdemo = ["Google", "Runoob", "Taobao"]
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
dict1 = {d: len(d) for d in listdemo}
print(dict1)
listdemo2 = {2, 4, 6}
dict2 = {str(d) + "的平方": d**2 for d in listdemo2}
print(dict2)


# 集合推导式
"""
集合推导基本格式：
{ expr for value in collection }
或 
{ expr for value in collection if condition }
"""
s1 = {x for x in range(1, 10)}
print(s1)

s2 = {x for x in (1, 2, 3)}
print(s2)


s3 = {x for x in "abracadabra" if x not in "abc"}
print(s3)


# 元组推导式（生成器表达式）
"""
元组推导基本格式：
(expr for value in collection)
或 
(expr for value in collection if condition)
"""
t1 = (x for x in range(1, 10))
# 输出生成器对象 <generator object <genexpr> at 0x0000023276C26740>
print(t1)
# 输出元组 (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple(t1))