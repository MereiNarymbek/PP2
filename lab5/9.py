import re
x=str(input("Enter the string: "))
pattern=r"(?<!^)(?=[A-Z])"
if re.search(pattern,x):
    result=re.sub(pattern," ",x)
    print(result)