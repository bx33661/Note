import hashlib
import random

def encrypt_md5(chars):
    """生成MD5哈希值"""
    return hashlib.md5(chars.encode('utf-8')).hexdigest()

def generate_random_number(length=8):
    """生成一个指定长度的随机数字字符串"""
    return str(random.randint(10 ** (length - 1), 10 ** length - 1))

def main():
    start = "8031b"  # 指定的MD5值开头字符
    num_length = 12  # 可以指定长度
    while True:
        random_number = generate_random_number(num_length)
        print(f"Test {random_number}")
        md5_value = encrypt_md5(random_number)
        if md5_value.startswith(start):
            print("Yes!")
            print(f"[+] {random_number} {md5_value}")
            break
        else:
            print("No!")

if __name__ == '__main__':
    main()
    print('完成！')
