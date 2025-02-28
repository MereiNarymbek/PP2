import re
x=str(input())
y=re.search("^a.*b$",x)
if y:
    print("YES")
else:
    print("NO")