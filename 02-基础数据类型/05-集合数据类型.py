"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
集合中数据是无序的，不能使用索引访问集合中的元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式
parame = {value01,value02,…}
或者
set(value)
"""

s1 = {1213, 1213.10, True, "hello", (12, 13)}
print(s1)
print("=================")


sites = {"Google", "Taobao", "dyf", "Facebook", "Zhihu", "Baidu", "Google"}
print(sites)

# 成员测试
if "dyf" in sites:
    print("dyf在集合中")

# set可以进行集合运算
a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print("a 和 b 的差集", a - b)  # 集合中a包括的b不包括的
print("a 和 b 的并集", a | b)  # 集合中a和b包括的
print("a 和 b 的交集", a & b)  # 集合中a和b都包括的
print("a 和 b 的对称差集", a ^ b)  # 集合中a和b不同时存在的元素


# 创建空集合
emptySet = set()
print(emptySet)
print(type(emptySet))

s1 = set(("hello", "world"))
print(s1)

# print(id(emptySet))
# 添加元素
emptySet.add(1)
emptySet.add(2)
emptySet.add(3)
print(emptySet)
# print(id(emptySet))

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
emptySet.update({4, 5, 6})
emptySet.update([7, 8, 9])
print(emptySet)

# 移除元素
emptySet.remove(1)
# 移除的元素不存在会报错
# emptySet.remove(10)
# 移除的元素不存在不会报错
emptySet.discard(10)
print(emptySet)

# 随机删除集合中的一个元素
# set集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。
thisset = set(("Google", "Baidu", "Taobao", "Facebook"))
print(thisset)
x = thisset.pop()
print(thisset)
print(x)

# 集合中都 len
print(len(emptySet))
# 清空集合
emptySet.clear()
print(emptySet)

# 判断集合中是否存在某个元素
x = {1, 2, 3}
print(1 in x)
print(4 in x)
