from io import BytesIO

# 创建 BytesIO 对象
f = BytesIO()

f.write('理想'.encode('utf-8'))
print(f.getvalue())  
# b'\xe7\x90\x86\xe6\x83\xb3'

print(f.getvalue().decode('utf-8'))
# 理想
