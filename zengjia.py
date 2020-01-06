# 通过pymasql完成操作mysql数据的本质是什么？
# 本质就是通过游标执行sql语句，例如：cursor.execute(sql)
# 执行插入操作本质上就是执行insert sql语句
# 所以我们可以先按照需求，把插入语句构造好，然后通过pymysql来执行
# 1.导包
import pymysql
# 2.建立连接
coon=pymysql.connect(host="localhost", user="root", password="root", database="books", port=3306, autocommit=True)

# 3.获取游标
cursor=coon.cursor()

# 4.执行

insert_sql="insert into t_book(id,title,pub_date) values(15,'红楼梦','1996-4-16')"
cursor.execute(insert_sql)
# 注意：写入语句不能通过fetchone和fetchall来查看
cursor.execute("select * from t_book")
print(cursor.fetchall())
# 5.断开游标
cursor.close()
# 6.断开连接
coon.close()