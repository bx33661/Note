import jwt

# 你的 JWT 字符串
jwt_token = ".eJwtjEEOgyAUBa9i39qFQoHgGXoDY4yB_21TIokfVsa7l0VXk1nMXFg5bfImwTRf6EoDpIZAIujxyvvn6P7ONT2w3EuPICevJX_pwAQd_NMry5titjp6ZwaOUY_GKTOMzNpFS16HtjtzolbslaTg_gHfzScW.ZyBClA.J_S7l04koMThze113bY_yrqTPSA"

# 解码 JWT（不带验证）
try:
    decoded_token = jwt.decode(jwt_token, options={"verify_signature": False})
    print("Decoded Token:", decoded_token)
except jwt.DecodeError as e:
    print("Decode Error:", e)
