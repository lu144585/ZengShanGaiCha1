# 1.导包
import pymysql

# 2.建立连接
conn = pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, autocommit=False)

# 3.获取游标(游标是指针指向数据的地址)
cursor = conn.cursor()

# 4.执行
# 查看数据库的版本
cursor.execute("select version()")
# fetchone(): 获取下一个查询结果集，结果集是一个对象 fetchall(): 获取全部的返回结果行 rowcount: 获取execute()方法执行后影响的行数
#
# 注意使用游标执行sql语句后，不会返回执行结果。返回执行结果必须通cursor.fetchone（）或cursor.fetchall的方式来获取
print("数据库的版本号为：",cursor.fetchall())
# 5.关闭游标‘
cursor.close()
# 6.关闭连接
conn.close()
