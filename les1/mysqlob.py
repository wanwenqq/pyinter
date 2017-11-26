#coding   = utf-8

import mysql.connector




# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='bookan', database='bookan')
cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Anders'])
# 提交事务:

print  (cursor.rowcount)
conn.commit()

cursor  = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
cursor.execute('select * from user ')
values = cursor.fetchall()
print (values)


cursor.close()
