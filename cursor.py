def simple_recursive_function(n):
    if n <= 0:
        return
    else:
        print(n)
        simple_recursive_function(n - 1)

simple_recursive_function(5)
