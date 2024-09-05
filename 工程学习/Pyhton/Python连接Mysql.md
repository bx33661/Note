## Python连接Mysql

环境配置

```python
pip install pymysql -i  https://pypi.tuna.tsinghua.edu.cn/simple
```

连接数据库

```python
import pymysql
arg_kwargs={
    'host':"localhost",
    'port':3306,
    'user':'root',
    'password':"123456",
    'database':"test",
    'charset':'utf8'
}
db=pymysql.connections.Connection(**arg_kwargs)#pymysql.connections.Connection对象
cur = db.cursor()
```

调用数据库

```python
import pymysql
arg_kwargs={
    'host':"localhost",
    'port':3306,
    'user':'root',
    'password':"123456",
    'database':"test",
    'charset':'utf8'
}
db=pymysql.connections.Connection(**arg_kwargs)#pymysql.connections.Connection对象
cur = db.cursor()

sql = "SELECT * FROM users"

try:
    cur.execute(sql)
    all = cur.fetchall()
    print(all)
except Exception as e:
    print(e)
else:
    print("sql执行成功")
finally:
    cur.close()
    db.close()
```

```
# 分别获取一条记录数据、多条记录、所有记录
one=cur.fetchone()
many=cur.fetchmany(2)
all=cur.fetchall()
```

