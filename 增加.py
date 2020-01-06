# 1.导包
import pymysql
# 2.建立连接
conn=pymysql.connect("localhost","root","root","books")#注意，如果没有设置autocommit,那么自动提交事务是关闭状态

# 3.获取游标
cursor=conn.cursor()

# 需求新增一本书2.增加这本书中的一个人物
# 新增一本书的sql
add_book_sq="insert into t_book(id,title,pub_date)values(5,'西游记','1998-2-6');"
# 新增一个人物的sql
add_hero="insert into t_hero(id,`name`,`gender`,`book_id`)values(7,'孙悟空',1,5);"
# 4.执行
cursor.execute(add_book_sq)
cursor.execute(add_hero)
# 查看结果
cursor.execute('select * from t_book')
print("查看添加书之后结果 ",cursor.fetchall())
cursor.execute('select * from t_hero')
print("查看新增任务后结果",cursor.fetchall())
# 如果自动提交事务没有开启那么需要手动提交事务
# 否则在代码中的操作不会真正的把数据提交到数据库
# 所以我们需要手动提交事务，提交方法就是：conn.commit（）
conn.commit()
# 5.断开游标
cursor.close()
# 6.断开连接
conn.close()