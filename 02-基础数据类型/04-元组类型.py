"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
"""

tuple1 = (1213, 1213.10, "hello", True, [12, 13], (12, 13))
print("输出完整元组", tuple1)
print("输出元组的第一个元素", tuple1[0])
print("输出从第二个元素开始到第三个元素", tuple1[1:3])
print("输出从第三个元素开始的所有元素", tuple1[2:])
tinytuple = (123, "caiyuan")
print("输出两次元组", tinytuple * 2)
print("连接元组", tuple1 + tinytuple)
print("输出元组的长度", len(tuple1))
print("元组反转", tuple1[::-1])
print("元组解包", *tuple1)


"""
1、 与字符串一样，元组的元素不能修改；
2、 元组也可以被索引和切片，方法一样；
3、 注意构造包含0或1个元素的元组的特殊语法规则；
4、 元组也可以使用+操作符进行拼接；
"""

# 成员测试
if "hello" in tuple1:
    print("hello在元组中")


# 元组内置函数
r"""  
Python元组包含了以下内置函数
序号	结果描述	实例
1	len(tuple)
计算元组元素个数。	>>> tuple1 = (‘Google’, ‘Caiyua’, ‘Taobao’)
>>> len(tuple1)
3
>>>
2	max(tuple)
返回元组中元素最大值。	>>> tuple2 = (‘5’, ‘4’, ‘8’)
>>> max(tuple2)
‘8’
>>>
3	min(tuple)
返回元组中元素最小值。	>>> tuple2 = (‘5’, ‘4’, ‘8’)
>>> min(tuple2)
‘4’
>>>
4	tuple(iterable)
将可迭代系列转换为元组。	>>> list1= [‘Google’, ‘Taobao’, ‘Caiyua’, ‘Baidu’]
>>> tuple1=tuple(list1)
>>> tuple1
(‘Google’, ‘Taobao’, ‘Caiyua’, ‘Baidu’)
"""
x = (10, 12, 5)
print("最大元素:", max(x))
print("最小元素:", min(x))
# print("元组转换为列表:", list(x))
y = [12, 10, 5]
print("打印输出：", tuple(y))
print("未修改前x元组内存地址：", id(x))
x = (4, 5, 5)
print("修改后x元组内存地址：", id(x))
