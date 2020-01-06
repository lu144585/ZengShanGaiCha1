# 1.导包
import pymysql
# 2.建立连接                                                                                      查询可以不用写事务
coon=pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, autocommit=False)
# 3.获取游标
cursor=coon.cursor()
# 4.执行sql语句
select_sql = "select `id`,`title`,`read`,`comment` from t_book;"
cursor.execute(select_sql)
print("查询结果的总记录数据为",cursor.rowcount)

# 查询结果的第一条数据
print("查询结果的第一条数据为：",cursor.fetchone())
# 查询全部结果
# 注意如果之前使用过fetchone或fetchall后续再使用fetchall时，会从上一个的指针位置读取数据
# 要获取全部的查询结果，需要重新再执行查询语句
# print("查询全部结果：", cursor.fetchall())
cursor.execute(select_sql)

print("第二次查询全部结果：",cursor.fetchall())   #并且再次打印



# 5.关闭游标
cursor.close()
# 6.关闭连接
coon.close()