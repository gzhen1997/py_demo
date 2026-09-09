"""  
日期和时间
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳
"""

import time

# 获取当前时间戳
print("当前时间戳：", time.time())
# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。


"""  
很多Python函数用一个元组装起来的9组数字处理时间:

序号	字段	值
0	4位数年	2008
1	月	1 到 12
2	日	1到31
3	小时	0到23
4	分钟	0到59
5	秒	0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	-1, 0, 1, -1是决定是否为夏令时的标识

上述也就是 struct_time 元组。这种结构具有如下属性：

序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0 到 6 (0是周一)
7	tm_yday	一年中的第几天，1 到 366
8	tm_isdst	是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1
"""

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
localtime.tm_year
print ("年份：", localtime.tm_year)
localtime.tm_mon
# 不够2为左补0
print ("月份%02d：" % localtime.tm_mon)
localtime.tm_mday
print ("日%02d：" % localtime.tm_mday)
# 不够2为左补0
print ("小时%02d：" % localtime.tm_hour  )
localtime.tm_min
print ("分钟%02d：" % localtime.tm_min)
localtime.tm_sec
print ("秒%02d：" % localtime.tm_sec)

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

"""  
python中时间日期格式化符号：
%y两位数的年份表示（00-99）
%Y四位数的年份表示（000-9999）
%m月份（01-12）
%d月内中的一天（01-31）
%H24小时制小时数（0-23）
%I12小时制小时数（01-12）
%M分钟数（00=59）
%S秒（00-59）
%a本地简化星期名称
%A本地完整星期名称
%b本地简化的月份名称
%B本地完整的月份名称
%c本地相应的日期表示和时间表示
%j年内的一天（001-366）
%p本地A.M.或P.M.的等价符
%U一年中的星期数（00-53）星期天为星期的开始
%w星期（0-6），星期天为星期的开始
%W一年中的星期数（00-53）星期一为星期的开始
%x本地相应的日期表示
%X本地相应的时间表示
%Z当前时区的名称
%%%号本身
"""
print("-------------------")

"""  
序号	函数及描述
1	calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的 year 年年历，3 个月一行，间隔距离为 c。 每日宽度间隔为w字符。每行长度为 21W+18+2 C。l 是每星期行数。
2	calendar.firstweekday( )返回当前每周起始日期的设置。默认情况下，首次载入 calendar 模块时返回 0，即星期一。
3	calendar.isleap(year)是闰年返回 True，否则为 False。
4	calendar.leapdays(y1,y2)返回在Y1，Y2两年之间的闰年总数。
5	calendar.month(year,month,w=2,l=1)返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
6	calendar.monthcalendar(year,month)返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
7	calendar.monthrange(year,month)返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。
8	calendar.prcal(year, w=0, l=0, c=6, m=3)相当于 print (calendar.calendar(year, w=0, l=0, c=6, m=3))。
9	calendar.prmonth(theyear, themonth, w=0, l=0)相当于 print(calendar.month(theyear, themonth, w=0, l=0))。
10	calendar.setfirstweekday(weekday)设置每周的起始日期码。0（星期一）到6（星期日）。
11	calendar.timegm(tupletime)和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
12	calendar.weekday(year,month,day)返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
"""


import calendar
cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)

# 2016年1月1日是星期几
print ("2016年1月1日是星期几：", calendar.weekday(2016, 1, 1))

# 2016年的年历
# print (calendar.calendar(2016))




"""  """
