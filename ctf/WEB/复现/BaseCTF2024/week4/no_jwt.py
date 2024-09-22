from flask import Flask, request, jsonify
import jwt
import datetime
import os
import random
import string

app = Flask(__name__)

# 随机生成 secret_key
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# 登录接口
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # 其他用户都给予 user 权限
    token = jwt.encode({
            'sub': username,
            'role': 'user',  # 普通用户角色
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.secret_key, algorithm='HS256')
    return jsonify({'token': token}), 200

# flag 接口
@app.route('/flag', methods=['GET'])
def flag():
    token = request.headers.get('Authorization')
    
    if token:
        try:
            decoded = jwt.decode(token.split(" ")[1], options={"verify_signature": False, "verify_exp": False})
            # 检查用户角色是否为 admin
            if decoded.get('role') == 'admin':
                with open('/flag', 'r') as f:
                    flag_content = f.read()
                return jsonify({'flag': flag_content}), 200
            else:
                return jsonify({'message': 'Access denied: admin only'}), 403
            
        except FileNotFoundError:
            return jsonify({'message': 'Flag file not found'}), 404
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
    return jsonify({'message': 'Token is missing'}), 401

if __name__ == '__main__':
    app.run(debug=True)
