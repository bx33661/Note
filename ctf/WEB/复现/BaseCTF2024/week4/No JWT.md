### No JWT

---

阅读源码：

```python
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
```

进入login页面，传json参数

```json
{
  "username": "admin",
  "password": "123456"
}
```



![image-20240922212217813](https://gitee.com/bx33661/image/raw/master/path/image-20240922212217813.png)



接着继续看代码

```python
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
```

修改user 为 admin

![image-20240922213630882](https://gitee.com/bx33661/image/raw/master/path/image-20240922213630882.png)

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTcyNzAxNDgzM30.hDo3TZwLEkLihU8NYMJkMuUtq7JjY4W0nJhRiT43-EI
```



**request.headers.get('Authorization')**

注意这个是从http头中获取这个值，然后jwt解码

> 在HTTP请求中，`Authorization`头部用于提供访问受保护资源所需的凭证。`Bearer`是认证的一种方式，它表示该请求中包含一个访问令牌（access token），这个令牌用于授权用户访问受保护的资源。
>
> 具体来说，`Authorization`头部的格式为：
>
> ```
> `Authorization: Bearer <access_token> 
> ```
>
> 
>
> 其中，`Bearer`关键字告诉服务器，接下来的 `<access_token>` 是一个令牌，用于授权请求。`Bearer` 认证方式是OAuth 2.0标准的一部分，用于实现无状态的访问控制，令牌通常由身份验证服务器颁发，并在请求中传递，用于验证用户身份和权限。
>
> 总的来说，`Bearer`前缀的作用是明确标识令牌的类型，告诉服务器如何处理和验证这个令牌。

![image-20240922213119575](https://gitee.com/bx33661/image/raw/master/path/image-20240922213119575.png)

![image-20240922213946986](https://gitee.com/bx33661/image/raw/master/path/image-20240922213946986.png)