import jwt


jwt_payload={
  "user": "admin",
  "iat": 1732026296
}

pub=open("public.key","rb").read()
jwt_headers={
  "alg": "HS256",
  "typ": "JWT"
}

jwt_token=jwt.encode(jwt_payload,key=pub,algorithm='HS256',headers=jwt_headers,)

print(jwt_token)