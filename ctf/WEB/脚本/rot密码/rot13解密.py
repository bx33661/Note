def caesar_decrypt(cipher, shift_value=13):
    """
    使用凯撒密码解密给定的密文，指定移位值。
    
    :param cipher: 要解密的密文。
    :param shift_value: 每个字母移动的位置数。默认为13（ROT13）。
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
    ciphertext = input("请输入密文: ")
    decrypted_text = caesar_decrypt(ciphertext)
    print(f'解密后的明文: {decrypted_text}')
    print("解密完成！")

if __name__ == '__main__':
    main()
