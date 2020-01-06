# 1.导包
import pymysql
# 2.建立连接
coon = pymysql.connect('localhost', 'root', 'root', 'books', autocommit=True)

# 3.获取游标
cursor=coon.cursor()
# 4.执行
# 删除三体这本书
delete_sql="delete from t_book where title='三体';"
cursor.execute(delete_sql)
# 查看删除结果
cursor.execute("select * from t_book")
print("删除后结果：",(cursor.fetchall()))
# 5.关闭游标
cursor.close()
# 6.关闭连接
coon.close()