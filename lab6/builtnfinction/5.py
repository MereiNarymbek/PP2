def my_func(mytuple):
    return all(mytuple)

mytuple=tuple(map(eval, input().split()))
if my_func(mytuple):
    print(True)
else:
    print(False)