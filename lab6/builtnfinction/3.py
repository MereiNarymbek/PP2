def my_func(str):
    str=str.lower()
    if str==''.join(reversed(str)):
        return True
    else:
        return False
str_input=input()
if my_func(str_input):
    print("YES")
else:
    print("NO")