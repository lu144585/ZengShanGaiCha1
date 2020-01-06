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
book_list=cursor.fetchall()    #这里算是执行了一次

print("查询全部的结果：",book_list)   #直接打印赋值后的变量即可

# 只打出笑傲江湖书籍信息
print("只打出笑傲江湖书籍信息",book_list[2])
# 只打出笑傲江湖
print("只打出笑傲江湖",book_list[2][1])
# 使用for循环遍历可以打印更加整洁,依次的遍历出每本书
for book_b in book_list:
    print("依次打印每本书",book_b)
#     可以使用索引遍历出书名
for book in book_list:
    print("书名为",book[1])




# 5.关闭游标
cursor.close()
# 6.关闭连接
coon.close()