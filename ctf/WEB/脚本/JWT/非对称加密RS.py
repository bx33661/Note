import jwt
from jwt.exceptions import InvalidTokenError

# 原始JWT,这里填写你的jwt
original_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidXNlciIsImlhdCI6MTczODQ3NjMwNX0.j30UimIQuskPL-e2kCy0DZLSdI3f-MPITzP0UTpxhRStDa1-sINp-flfFkaoflKp28tnA0RulclINWsKwRMi1fO0M4CVyRqXK143TbsffxbLoILtEI2k5nu-Co56Vo66Bx6dap1v852-FPBh7xuCvYge-Lv_WPQpLFaifokSveo"

# 加载密钥
with open("private.key", "rb") as f:
    private_key = f.read()

with open("public.key", "rb") as f:
    public_key = f.read()

try:
    # 解码原始JWT
    decoded = jwt.decode(original_jwt, public_key, algorithms=["RS256"], options={"verify_signature": True})
    
    # 修改claims（根据需要调整）
    decoded["user"] = "admin"
    
    # 生成新JWT
    new_jwt = jwt.encode(
        payload=decoded,
        key=private_key,
        algorithm="RS256",
        headers={"alg": "RS256", "typ": "JWT"}
    )
    
    print(f"New JWT: {new_jwt}")

except InvalidTokenError as e:
    print(f"Invalid token: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
