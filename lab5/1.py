import re
x=str(input())
y=re.search("^ab*$" , x)
if y:
    print("YES")
else:
    print("NO")
