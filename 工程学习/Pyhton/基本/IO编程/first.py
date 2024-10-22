try:
    f = open('工程学习\Pyhton\基本\基本库学习\IO编程\demo.txt','r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()