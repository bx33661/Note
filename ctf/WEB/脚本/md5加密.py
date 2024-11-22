import hashlib
def md5_encode(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()
    return md5_digest

# md5(cookie_secret+md5(filename))
data = "123456boss"
md5_encoded = md5_encode(data)

print(f"原始数据: {data}")
print(f"MD5 编码: {md5_encoded}")