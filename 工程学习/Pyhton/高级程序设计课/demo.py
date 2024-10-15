def f(num):
    res = 0
    while num>0:
        last_num = num%10
        res += last_num
        num //= 10
    return res

integer = input("Enter an integer between 0 and 1000:")
ress = f(integer)
print("The sum of all digits in {} is {}".format(integer,ress))