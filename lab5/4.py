import re
x=str(input())
y=re.findall("^[A-Z]+[a-z]+$" , x)
if y:
    print("YES")
else:
    print("NO")