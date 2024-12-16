def f(date, k):
    """
    :param date:
    :param k: 当前位置
    :return:
    """
    date = list(date)
    if k ==len(date):
        for i in range(len(date)):
            print(date[i],end="")
        print()
    for i in range(k,len(date)):
        date[i], date[k] = date[k], date[i] #试探
        f(date,k+1)
        date[i], date[k] = date[k], date[i]   #回溯

date = "ABC"
f(date,0)