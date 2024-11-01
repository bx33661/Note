def string_to_hex(s):
    # 将字符串编码为十六进制形式，每个字符被转为两个十六进制数
    return s.encode('ascii').hex()

def hex_to_string(s):
    # 将十六进制字符串解码回普通字符串
    return bytes.fromhex(s).decode('ascii')

# 示例
normal_string = "admin"
hex_string = string_to_hex(normal_string)
print(f"Original: {normal_string}")
print(f"Hex: {hex_string}")

# 转换回来以验证
decoded_string = hex_to_string(hex_string)
print(f"Decoded: {decoded_string}")

# 输出处理成类似 \x 格式
def string_to_hex_with_slashes(s):
    return ''.join(f'\\x{ord(c):02x}' for c in s)

# 测试
print("Hex with slashes:", string_to_hex_with_slashes(normal_string))
