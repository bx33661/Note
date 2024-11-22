import hashlib

#MD5是最常见的哈希算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示

md5 = hashlib.md5()
#md5.update("bx33661".encode('utf-8'))
#378bcfb0e678edb44e462cb2fd3fe6ef
md5.update("bx33662".encode('utf-8'))
#3a4870ae20c769f46ff254d8db803b2c
print(md5.hexdigest())