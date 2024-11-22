import time
while True:
    #输出年月日时分秒
    print(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(5)
