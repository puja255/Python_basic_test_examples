def recursive_func(num):
    if num != 0:
        return num + recursive_func(num - 1)
    else:
        return 0


print(recursive_func(10))