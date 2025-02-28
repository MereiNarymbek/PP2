import re
x=str(input())
y=re.findall("^[a-z]+_[a-z]+$" , x)
if y:
    print("YES")
else:
    print("NO")