#coding=utf-8

'''
#SQLite
#是一种嵌入式数据库，它的数据库就是一个文件，
#数据库连接称为：Connection
#连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后获得执行结果
#Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只要提供符合Python标准的数据库驱动即可
#SQLite的驱动内置在Python标准库中，所以可以直接来操作SQLite数据库

#导入SQLite驱动：
import sqlite3
#连接到数据库。如果数据库文件不存在，会自动在当前目录创建：
conn = sqlite3.connect('test.db')
#创建一个Cursor:
cursor = conn.cursor()
#执行一条SQL语句，创建user表：
cursor.execute('create table user(id varchar(20) primary key , name varchar(20))')
#继续执行一条sql语句，插入一条记录
cursor.execute('insert into user(id,name) values (\'1\',\'Michael\')')
#通过rowcount获得插入的行数
cursor.rowcount
#关闭cursor
cursor.close()
#提交事物：
conn.commit()
#关闭connection
conn.close()
'''

#查询记录
import sqlite3
#连接数据库
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询语句：
cursor.execute('select * from user where id=?',('1',))
#获得查询结果集
values = cursor.fetchall()
print(values)
#关闭cursor和connection
cursor.close()
conn.close()




#MySQL
#MySQL是Web世界中使用最广泛的数据库服务器。
#此外MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB
#用法同sqlite3，连接的时候要带用户名和密码
#