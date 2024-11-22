import jwt

# JWT密钥
secret_key = ""

# JWT令牌
jwt_token = ""

try:
    # 解密JWT
    decoded_payload = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])
    print("解密后的载荷:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("JWT已过期")
except jwt.InvalidTokenError:
    print("无效的JWT")