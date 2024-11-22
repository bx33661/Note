import hashlib

# 假设你有一个原始字符串
original_string = "123456boss"

# 生成 SHA-1 哈希值
hash_object = hashlib.sha1(original_string.encode())
sha1_hash = hash_object.hexdigest()

print("Generated SHA-1 Hash:", sha1_hash)
