"""  
JSON 数据解析
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
json.dumps(): 对数据进行编码。 生成 JSON 字符串。
json.loads(): 对数据进行解码。 从 JSON 字符串中恢复 Python 数据结构。
"""

"""  
在json 的编解码过程中，Python 的原始类型与 json 类型会相互转换，具体的转化对照如下：
Python 编码为 JSON 类型转换对应表：
Python	Json
dict	object
list, tuple	array
str	string
int, float, int- & float-derived Enums	number
True	true
False	false
None	null
"""

"""  
JSON 解码为 Python 类型转换对应表：
Json	Python
object	dict
array	list
string	str
number (int)	int
number (real)	float
true	True
false	False
null	None
"""

"""  
json.dumps 与 json.loads 实例
以下实例演示了 Python 数据结构转换为JSON：
"""

import json
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'dyf',
    'url' : 'http://www.dyf.com'
}
json_str = json.dumps(data)
print ("Python 原始数据：", str(data))
print ("JSON 对象：", json_str)

# JSON 字符串转换为 Python 字典
data = json.loads(json_str)
print ("JSON 字符串：", type(json_str))
print ("Python 字典：", type(data))

