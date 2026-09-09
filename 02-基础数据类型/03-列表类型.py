# List（列表）
"""
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
"""
l1 = [123, "hello", 123.10, 3 + 4j, True, [1, 2, 3]]
print(l1)
print("=================")

"""
列表截取的语法格式如下：
变量[头下标:尾下标]
"""
print(l1[0:3])
print(l1[2:5])
print(l1[2:])
print(l1[:5])
print(l1[2:5:2])
print(l1[::-1])

# 列表拼接
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1 + l2)

# 列表中的元素是可以改变的
l1[2:5] = ["替换元素1", "替换元素2"]
print(l1)
# 删除列表中的元素
del l1[2:5]
print("删除元素后的列表为：", l1)

#  * 号可以将列表中的元素展开，每个元素之间用空格隔开。
print(*l1)
print("=================")


"""  
Python列表脚本操作符
列表对+ 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：
表达式	结果	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
[‘Hi!’] * 4	[‘Hi!’, ‘Hi!’, ‘Hi!’, ‘Hi!’]	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
"""
print(l1 * 4)
x = [str(x) + "_" for x in l1]
print("列表中的元素添加下划线后的结果为：", x)

# 拼接列表
y = ["123", "123"]
y += x
print("拼接列表为：", y)


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    """
    假设列表 list = [1,2,3,4], list[0]=1, list[1]=2 而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    inputWords[-1::-1] 有三个参数
    第一个参数 -1 表示最后一个元素
    第二个参数为空，表示移动到列表末尾
    第三个参数为步长，-1 表示逆向
    """
    # inputWords = inputWords[-1::-1]
    inputWords = inputWords[::-1]
    # 重新组合字符串
    output = " ".join(inputWords)
    return output


print(__name__)

if __name__ == "__main__":
    input = "I like caiyua"
    rw = reverseWords(input)
    print(rw)


print("=================")

import operator

# 列表比较
l1 = [123,234]
l2 = [123,234]
l3 = [234,123]
print(l1 == l2)
print(operator.eq(l1, l2))
print("-----------------")
print(l1 == l3)
print(operator.eq(l1, l3))
