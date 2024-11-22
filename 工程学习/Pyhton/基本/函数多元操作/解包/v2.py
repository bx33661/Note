# **
def great(name,age,phone):
    print(f"姓名：{name}，年龄：{age}，电话：{phone}")

dx33661 = {"name":"dx33661","age":18,"phone":"123456789"}
great(**dx33661)  # 姓名：dx33661，年龄：18，电话：123456789
