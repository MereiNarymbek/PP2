import re 
x = str(input())
y = re.findall("^a(b{1,2})$", x)
if y:
    print("YES")
else:
    print("NO")
        
