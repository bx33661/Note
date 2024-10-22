#读取二进制文件
#这个图片是用于文件上传漏洞的

with open("工程学习\Pyhton\基本\基本库学习\IO编程\muma.jpg",'rb') as f:
    print(f.read())


#with open("工程学习\Pyhton\基本\基本库学习\IO编程\mylogo.jpg",'rb') as f:
#    print(f.read())