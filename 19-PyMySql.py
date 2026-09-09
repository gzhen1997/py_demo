"""
什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2 中则使用 mysqldb。
PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
PyMySQL 安装
在使用PyMySQL 之前，我们需要确保 PyMySQL 已安装。
PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL。
如果还未安装，我们可以使用以下命令安装最新版的 PyMySQL：
$ pip3 install PyMySQL
"""

"""  
数据库连接
连接数据库前，请先确认以下事项：

您已经创建了数据库 TESTDB.
在TESTDB数据库中您已经创建了表 EMPLOYEE
EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
连接数据库TESTDB使用的用户名为 root ，密码为 root,你可以可以自己设定或者直接使用root用户名及其密码，Mysql数据库用户授权请使用Grant命令。
在你的机子上已经安装了 Python pymysql 模块。

以下实例链接 Mysql 的 TESTDB 数据库：
"""
import pymysql


# 打开数据库连接
db = pymysql.connect(
    host="192.168.56.100", port=13306, user="root", password="root", database="TESTDB"
)

# 使用游标
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 获取查询结果
version = cursor.fetchone()
print("数据库版本 : ", version[0])
cursor.execute("SELECT * FROM EMPLOYEE")
# 获取所有记录
results = cursor.fetchall()
for row in results:
    print(row)
    pass


# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE_NEW (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
# cursor.execute(sql)
# 提交事务
db.commit()
# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE_NEW(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
sql = (
    "INSERT INTO EMPLOYEE_NEW(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)"
    % ("Mac", "Mohan", 20, "M", 2000)
)
sql = "INSERT INTO EMPLOYEE_NEW(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ({0}, {1},  {2},  {3},  {INCOME})".format(
    "Mac", "Mohan", 20, "M", INCOME=2000
)
print(sql)
try:
    # 执行sql语句
    #    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
# except Exception as e:
except:
    # 如果发生错误则回滚
    db.rollback()
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE_NEW \
       WHERE INCOME > %s" % (1000)
try:
   #执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")
   
# SQL 更新语句
sql = "UPDATE EMPLOYEE_NEW SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误时回滚
   db.rollback()


# SQL 删除语句
sql = "DELETE FROM EMPLOYEE_NEW WHERE AGE > %s" % (20)
try:
   # 执行SQL语句
#    cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 如果发生错误时回滚
   db.rollback()   
db.close()

"""  
执行事务
事务机制可以确保数据一致性。
事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
"""

"""  
错误处理
DBAPI中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:

异常	描述
Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
Error	警告以外所有其他错误类。必须是 StandardError 的子类。
InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
以下为异常的继承结构：

Exception
|__Warning
|__Error
   |__InterfaceError
   |__DatabaseError
      |__DataError
      |__OperationalError
      |__IntegrityError
      |__InternalError
      |__ProgrammingError
      |__NotSupportedError
"""