# 1.导包
import pymysql

# 2.建立连接
coon = pymysql.connect('localhost', 'root', 'root', 'books', autocommit=True)
# 3.获取游标
cursor = coon.cursor()
# 4.执行
# 需要将三体的阅读量增1'read'
update_sql = "update t_book set `read` = `read`+ 1 where title = '三体';"
cursor.execute(update_sql)
# 查看结果
cursor.execute("select * from t_book;")
print("所有书：", cursor.fetchall())
# 5.关闭游标
cursor.close()
# 6.关闭连接
coon.close()
