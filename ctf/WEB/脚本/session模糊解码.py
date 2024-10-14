import base64
import json

def decode_session(session_data):
    try:
        # 分割session数据
        parts = session_data.split('.')
        if len(parts) != 3:
            raise ValueError("Session data should have three parts separated by dots.")

        # 尝试Base64解码第一个部分
        decoded_data = base64.urlsafe_b64decode(parts[0])
        print("Base64 Decoded Data:", decoded_data)

        # 尝试解析JSON
        json_data = json.loads(decoded_data.decode('utf-8'))
        print("Parsed JSON Data:", json_data)
    except Exception as e:
        print("Error decoding or parsing session data:", e)

# 示例session数据
session_data = "eyJoaXN0b3J5IjpbeyJjb2RlIjoiMSArIDEifV19.X98yeg.YggVMibcD6Bh8ZqORv4BMRBfNS0"

# 解码session数据
decode_session(session_data)
