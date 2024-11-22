import sys

def caesar_encrypt(plaintext, shift_value):
    """
    使用凯撒密码加密给定的明文，指定移位值。
    
    :param plaintext: 要加密的明文。
    :param shift_value: 每个字母移动的位置数。
    :return: 加密后的密文。
    """
    encrypted_text = []
    for ch in plaintext:
        if 'a' <= ch <= 'z':
            # 计算移位后的字符，必要时进行循环处理
            new_ch = chr(((ord(ch) - ord('a') + shift_value) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            new_ch = chr(((ord(ch) - ord('A') + shift_value) % 26) + ord('A'))
        else:
            # 非字母字符保持不变
            new_ch = ch
        encrypted_text.append(new_ch)
    
    return ''.join(encrypted_text)

def caesar_decrypt(cipher, shift_value):
    """
    使用凯撒密码解密给定的密文，指定移位值。
    
    :param cipher: 要解密的密文。
    :param shift_value: 每个字母移动的位置数。
    :return: 解密后的明文。
    """
    decrypted_text = []
    for ch in cipher:
        if 'a' <= ch <= 'z':
            # 计算移位后的字符，必要时进行循环处理
            new_ch = chr(((ord(ch) - ord('a') - shift_value) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            new_ch = chr(((ord(ch) - ord('A') - shift_value) % 26) + ord('A'))
        else:
            # 非字母字符保持不变
            new_ch = ch
        decrypted_text.append(new_ch)
    
    return ''.join(decrypted_text)

def main():
    # 设置标准输出的编码为 UTF-8
    sys.stdout.reconfigure(encoding='utf-8')

    choice = input("请选择操作（1-加密，2-解密）: ")
    
    if choice == '1':
        plaintext = input("请输入明文: ")
        shift_value = int(input("请输入移位值（0-25）: "))
        encrypted_text = caesar_encrypt(plaintext, shift_value)
        print(f'加密后的密文: {encrypted_text}')
    elif choice == '2':
        ciphertext = input("请输入密文: ")
        for shift_value in range(26):
            decrypted_text = caesar_decrypt(ciphertext, shift_value)
            print(f'ROT{shift_value}: {decrypted_text}')
        print("解码完成！")
    else:
        print("无效的选择！")

if __name__ == '__main__':
    main()
